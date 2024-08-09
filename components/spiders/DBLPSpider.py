import scrapy
from scrapy.loader import ItemLoader
from components.spiders.item import Publication
from components.mapper import TypeMapper
import requests
from bs4 import BeautifulSoup
from w3lib.html import remove_tags
import re

class DBLPSpider(scrapy.Spider):
    name = 'conferencespider'
    
    def start_requests(self):
        type_mapper = TypeMapper()
        url = f'https://dblp.org/db/{type_mapper.get(self.venue.get_type())}/{self.venue.get_dblp()}/index.html'
        if self.venue.get_type() == 'Conference':
            yield scrapy.Request(url=url, callback=self.parse_proceedings)
        elif self.venue.get_type() == 'Journal':
            yield scrapy.Request(url=url, callback=self.parse_volumes)
    
    def parse_proceedings(self, response):
        def is_starting_with(string, pattern):
            return bool(re.match(fr"^{pattern}", string, re.IGNORECASE))
        for proceeding in response.xpath('//cite[@class="data tts-content" and @itemprop="headline"]'):
            proceeding_year = proceeding.xpath('.//span[@itemprop="datePublished"]/text()').get()
            proceeding_url = proceeding.xpath('.//a[@class="toc-link"]/@href').get()
            proceeding_id = proceeding_url.rsplit('/', 1)[-1].rsplit('.', 1)[0]
            # if self.year_range.is_between(int(proceeding_year)) and is_starting_with(proceeding_id, self.venue.get_dblp()):
            if self.year_range.is_between(int(proceeding_year)):
                yield scrapy.Request(url=proceeding_url, callback=self.parse_publications, cb_kwargs={'year':proceeding_year, 'pcd_id': proceeding_id})
            else:
                continue
            

    def extract_years(self, text):
        return [year for year in re.findall(r'\b\d{4}\b', text)]
            
    def parse_volumes(self, response):
        for volume in response.xpath('//a[starts-with(@href, "https://dblp.org/db/journals/")]')[0].xpath('./parent::*/parent::*/li'):
            volume_year = self.extract_years(volume.xpath('.//a/text()').get())
            volume_url = volume.xpath('.//a/@href').get()
            if any(self.year_range.is_between(int(year)) for year in volume_year):
                converted_volume_year = '-'.join(volume_year)
                yield scrapy.Request(url=volume_url, callback=self.parse_publications, cb_kwargs={'year':converted_volume_year})
            else:
                continue
            
    def get_arxiv_url(self, title):
        def clean(sentence):
            pattern = r'[^A-Za-z0-9\s]'
            cleaned_sentence = re.sub(pattern, ' ', sentence)
            cleaned_sentence = ' '.join(cleaned_sentence.split())
            return cleaned_sentence
        params = {
            'query': clean(title),
            'searchtype': 'title',
            'size': '25',
        }
        response = requests.get('https://arxiv.org/search/', params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('li', class_ ="arxiv-result")
            titles = []
            for result in results:
                _title = result.find('p', class_='title is-5 mathjax').text
                if(clean(title) == clean(remove_tags(_title))):
                    p_tag = result.find('p', class_='list-title is-inline-block')
                    first_child = p_tag.findChildren(recursive=False)[0]
                    return first_child.get('href')
        return 'None'

    def parse_publications(self, response, year, pcd_id):
        for publication in response.xpath('//cite[@class="data tts-content" and .//span[@class="title"]]'):
            _title = str(publication.xpath('.//span[@class="title" and @itemprop="name"]/text()').get())
            if self.filter_engine.check(_title):
                loader = ItemLoader(item=Publication(), selector=publication)
                loader.add_value('title', _title)
                for author in publication.xpath('.//span[@itemprop="name" and @title]/text()').getall():
                    loader.add_value('authors', author)
                loader.add_value('venue', self.venue.get_official_acronym())
                loader.add_value('year', year)
                loader.add_value('proceeding_id', pcd_id)
                try: 
                    loader.add_value('arxiv_url', self.get_arxiv_url(_title))
                except: 
                    loader.add_value('arxiv_url', 'None')
                yield loader.load_item()
            else:
                continue
            
