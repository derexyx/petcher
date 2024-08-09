from components.filter import FilterEngine
from components.range import YearRange
from components.venue import VenueManager
from components.scraper import Scraper
from components.argsparser import ArgumentParser


def main():
    args = ArgumentParser.parse_arguments()
    
    output = args.output if args.output else "data/publications.jsonl"
    keywords = args.keywords if args.keywords else []
    
    venue_manager = VenueManager(args.venue)
    venue_list = venue_manager.get_venues()
    
    filter_engine = FilterEngine(method=args.method, keywords=keywords)
    year_range = YearRange(start=args.start, end=args.end)
    
    scraper = Scraper(output)
    scraper.start_crawling(venue_list, year_range, filter_engine)
    scraper.sort_output()

if __name__ == '__main__':
    main()
