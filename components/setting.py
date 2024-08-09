from fake_useragent import UserAgent
class ScrapySetting():
    def __init__(self, output):
        self.output = output
        
    def generate(self):
        return {
            "FEEDS": {self.output: {"format": "jsonl"}},
            "USER_AGENT": UserAgent().random,
            "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7",
            "FEED_EXPORT_ENCODING": "utf-8",
            "DNS_TIMEOUT": 120,
            "ROBOTSTXT": False,
            "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
            # "CONCURRENT_REQUESTS": 1,  # Maximum number of concurrent requests
            # "CONCURRENT_REQUESTS_PER_DOMAIN": 1,  # Maximum number of concurrent requests per domain
            # "DOWNLOAD_DELAY": 2,  # Delay in seconds between requests
            # "AUTOTHROTTLE_ENABLED": True,  # Enable AutoThrottle
            # "AUTOTHROTTLE_START_DELAY": 1,  # Initial download delay
            # "AUTOTHROTTLE_MAX_DELAY": 10,  # Maximum download delay
            # "AUTOTHROTTLE_TARGET_CONCURRENCY": 1.0  # Target concurrency
        }