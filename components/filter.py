import re

class FilterEngine:
    def __init__(self, method='all', keywords=None):
        if method not in ['all', 'any']:
            method = 'all'
        else:
            self.method = method
        self.keywords = keywords or []

    def check(self, text):
        if not isinstance(text, str):
            raise ValueError("The 'text' parameter should be a string")
        
        def generate_keyword_pattern(keyword):
            escaped_keyword = re.escape(keyword)
            pattern = fr"\b{escaped_keyword}(s|es)?\b"
            return pattern

        if not self.keywords:
            return True

        patterns = [generate_keyword_pattern(keyword) for keyword in self.keywords]

        if self.method == 'all':
            return all(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)
        elif self.method == 'any':
            combined_pattern = '|'.join(patterns)
            return bool(re.search(combined_pattern, text, re.IGNORECASE))
