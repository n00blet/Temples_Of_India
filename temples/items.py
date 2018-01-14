# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst

class TemplesItem(Item):
    # define the fields for your item here like:
    # name = Field()
    temple_name = Field(output_processor=TakeFirst())
    temple_url = Field(output_processor=TakeFirst())
    temple_coordinates = Field(output_processor=TakeFirst())
    temple_country = Field(output_processor=TakeFirst())
    temple_state = Field(output_processor=TakeFirst())
    temple_district = Field(output_processor=TakeFirst())
    temple_locale =  Field(output_processor=TakeFirst())
    temple_summary = Field(output_processor=TakeFirst())
    temple_images = Field(output_processor=TakeFirst())
    temple_website= Field(output_processor=TakeFirst())
    temple_arch_style = Field(output_processor=TakeFirst())
    temple_imp_festivals = Field(output_processor=TakeFirst())
    temple_poets = Field(output_processor=TakeFirst())
