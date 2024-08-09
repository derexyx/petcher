import json

class JSONLSorter:
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = []

    def read_data(self):
        with open(self.input_file, 'r', encoding='utf-8') as file:
            self.data = [json.loads(line) for line in file]

    def sort_data(self):
        self.data.sort(key=lambda x: (-int(x.get('year', 0)), x.get('venue', ''), x.get('proceeding_id', ''), x.get('title', '')))

    def write_data(self):
        with open(self.input_file, 'w', encoding='utf-8') as file:
            for entry in self.data:
                file.write(json.dumps(entry, ensure_ascii=False) + '\n')

    def sort_jsonl(self):
        self.read_data()
        self.sort_data()
        self.write_data()
