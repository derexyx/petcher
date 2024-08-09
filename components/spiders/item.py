from itemloaders.processors import MapCompose, Join, TakeFirst
from scrapy.item import Item, Field

def clean(string):
    return string.strip().rstrip('.')

class Publication(Item):
    title = Field(
        input_processor=MapCompose(clean),
        output_processor=TakeFirst()
    )
    authors = Field(
        input_processor=MapCompose(clean),
        output_processor=Join(", ")
    )
    venue = Field(
        input_processor=MapCompose(clean),
        output_processor=TakeFirst()
    )
    year = Field(
        input_processor=MapCompose(clean),
        output_processor=TakeFirst()
    )
    proceeding_id = Field(
        input_processor=MapCompose(clean),
        output_processor=TakeFirst()
    )
    arxiv_url = Field(
        input_processor=MapCompose(clean),
        output_processor=TakeFirst()    
    )