# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags, replace_escape_chars

class BikeAccessoryItem(scrapy.Item):
    title = scrapy.Field(
        input_processor = MapCompose(remove_tags, replace_escape_chars),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(remove_tags, replace_escape_chars),
        output_processor = TakeFirst()
    )    
    image_url = scrapy.Field(
        input_processor = MapCompose(remove_tags, replace_escape_chars),
        output_processor = TakeFirst()
    )
    serial_num = scrapy.Field(
        input_processor = MapCompose(remove_tags, replace_escape_chars),
        output_processor = TakeFirst()
    )
    description = scrapy.Field(
        input_processor = MapCompose(remove_tags, replace_escape_chars),
        output_processor = TakeFirst()
    )