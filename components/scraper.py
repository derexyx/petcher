from scrapy.crawler import CrawlerProcess
from components.spiders.DBLPSpider import DBLPSpider
from components.sorter import JSONLSorter
from components.setting import ScrapySetting

class Scraper:
    def __init__(self, output):
        self.output = output

    def create_process(self):
        return CrawlerProcess(settings=ScrapySetting(output=self.output).generate())

    def start_crawling(self, venue_list, year_range, filter_engine):
        process = self.create_process()
        for venue in venue_list:
            process.crawl(DBLPSpider, venue=venue, year_range=year_range, filter_engine=filter_engine)
        process.start()
    
    def sort_output(self):
        sorter = JSONLSorter(self.output)
        sorter.sort_jsonl()

