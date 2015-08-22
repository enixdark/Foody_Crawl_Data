# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodyItem(scrapy.Item):
    list = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    lane = scrapy.Field()
    city = scrapy.Field()
    phone = scrapy.Field()
    price_start = scrapy.Field()
    price_end = scrapy.Field()
    time_start = scrapy.Field()
    time_end = scrapy.Field()
    image = scrapy.Field()

    total_write_review = scrapy.Field()
    total_upload_images = scrapy.Field()
    total_check_in = scrapy.Field()
    total_save_to_love_collection = scrapy.Field()
    total_save_to_wish_collection = scrapy.Field()
    total_save_to_custom_collections = scrapy.Field()


    score_space = scrapy.Field()
    score_quality = scrapy.Field()
    score_price = scrapy.Field()
    score_service = scrapy.Field()
    score_location = scrapy.Field()

    total_score_comment_for_excellent = scrapy.Field()
    total_score_comment_for_good = scrapy.Field()
    total_score_comment_for_avg = scrapy.Field()
    total_score_comment_for_bad = scrapy.Field()
    avg_score_comment = scrapy.Field()

    geo_latitude = scrapy.Field()
    geo_longitude = scrapy.Field()

    types = scrapy.Field()
    dining_time = scrapy.Field()
    last_order = scrapy.Field()
    waiting_time =scrapy.Field()
    holiday = scrapy.Field()
    capacity = scrapy.Field()
    cuisine_style  = scrapy.Field()
    good_for = scrapy.Field()
    typical_dishes  = scrapy.Field()
    website = scrapy.Field()

    is_reservation_required = scrapy.Field()
    is_delivery_service  = scrapy.Field()
    is_takeaway_service = scrapy.Field()
    is_wifi = scrapy.Field()
    is_playground_for_kid = scrapy.Field()
    is_outdoor_seat = scrapy.Field()
    is_private_room = scrapy.Field()
    is_air_conditioner = scrapy.Field()
    is_credit_card_available = scrapy.Field()
    is_karaoke_service = scrapy.Field()
    is_free_bike_park = scrapy.Field()
    is_tip_for_staff = scrapy.Field()
    is_car_park = scrapy.Field()
    is_smoking_zone = scrapy.Field()
    is_member_card = scrapy.Field()
    is_tax_invoice_available = scrapy.Field()
    is_conference_support = scrapy.Field()
    is_heat_conditioner = scrapy.Field()
    is_disabled_person_support = scrapy.Field()
    is_live_sport_tv = scrapy.Field()
    is_live_music = scrapy.Field()
