MAP = {
    'Conference':'conf',
    'Journal':'journals'
}

DEFAULT_TYPE = 'conf'

class TypeMapper():
    def __init__(self, map = MAP):
        self.map = map
        
    def get(self, venue_type):
        return self.map.get(venue_type, DEFAULT_TYPE)