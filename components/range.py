from datetime import datetime
  
class YearRange():
    def __init__(self, start = 0, end = datetime.now().year):
        self.start = start
        self.end = end
        
    def is_between(self, year):
        return year >= self.start and year <= self.end