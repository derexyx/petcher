import argparse
from datetime import datetime

class ArgumentParser:
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description='Scrape publications from DBLP.ORG')
        parser.add_argument('-v', '--venue', required=True, nargs='+', help='Venue Acronyms')
        parser.add_argument('-s', '--start', type=int, default=0, help='Start Year (Default = 0)')
        parser.add_argument('-e', '--end', type=int, default=datetime.now().year, help='End Year (Default = Current Year)')
        parser.add_argument('-m', '--method', default='all', help='Filter Method (Default = "all")')
        parser.add_argument('-k', '--keywords', nargs='*', help='Filter Keywords (Default = [])')
        parser.add_argument('-o', '--output', help='Output Destination (Default = "data/publications.jsonl")')
        return parser.parse_args()