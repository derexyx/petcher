import re
import json
import os

class Venue:
    def __init__(self, info):
        self.info = info

    def print_info(self):
        print(self.info)
        
    def get_name(self):
        return self.info.get("name", "")

    def get_dblp(self):
        return self.info.get("dblp", "")
    
    def get_type(self):
        return self.info.get("type", "")

    def get_official_acronym(self):
        return self.info.get("acronyms", ["No acronym found"])[0]

class VenueMapper:
    def __init__(self, map_folder='components/venue_map/'):
        self.map_folder = map_folder
        self.map = self.load_map()

    def load_map(self):
        all_maps = []
        for filename in os.listdir(self.map_folder):
            if filename.endswith('.json'):
                file_path = os.path.join(self.map_folder, filename)
                with open(file_path, 'r') as file:
                    file_data = json.load(file)
                    if isinstance(file_data, list):
                        all_maps.extend(file_data)
                    else:
                        print(f"Warning: {filename} does not contain a list of dictionaries.")
        return all_maps
    
    def list(self):
        for entry in self.map:
            print(entry.get("name", "Unnamed venue"))

    def get_venue(self, acronym):
        formatted_acronym = self.format_acronym(acronym)
        for entry in self.map:
            acronyms = entry.get("acronyms", [])
            if formatted_acronym in [self.format_acronym(acr) for acr in acronyms]:
                return Venue(entry)
        return None

    def get_all_venues(self):
        return [Venue(entry) for entry in self.map]

    def format_acronym(self, acronym):
        return re.sub(r'[^a-zA-Z0-9]', '', acronym).lower()

class VenueManager:
    def __init__(self, acronyms):
        self.acronyms = acronyms
        self.mapper = VenueMapper()

    def get_venues(self):
        venue_list = []
        for venue in self.acronyms:
            _venue = self.mapper.get_venue(venue)
            if _venue:
                venue_list.append(_venue)
            else:
                print(f"Cannot find {venue}")
        return venue_list
