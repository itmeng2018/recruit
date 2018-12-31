# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class RecruitSpiderItem(scrapy.Item):
    """item"""
    info_source = scrapy.Field()
    job_name = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    city = scrapy.Field()
    company_name = scrapy.Field()
    welfare = scrapy.Field()
    work_years = scrapy.Field()
    education = scrapy.Field()
    address = scrapy.Field()
    job_detail = scrapy.Field()

# class DataClean(object):
#     """数据清洗类"""
#
#     @staticmethod
#     def info_source(value):
#         pass
#
#     @staticmethod
#     def job_name(value):
#         pass
#
#     @staticmethod
#     def min_salary(value):
#         pass
#
#     @staticmethod
#     def max_salary(value):
#         pass
#
#     @staticmethod
#     def city(value):
#         pass
#
#     @staticmethod
#     def company_name(value):
#         pass
#
#     @staticmethod
#     def job_name_clean(value):
#         pass
#
#     @staticmethod
#     def welfare(value):
#         pass
#
#     @staticmethod
#     def work_years(value):
#         pass
#
#     @staticmethod
#     def education(value):
#         pass
#
#     @staticmethod
#     def address(value):
#         pass
#
#     @staticmethod
#     def job_detail(value):
#         pass
#
#
# class RecruitItemLoader(ItemLoader):
#     """定义全局默认输出处理器"""
#     default_output_processor = TakeFirst()


# class RecruitSpiderItem(scrapy.Item):
#     """定义输入处理器: 映射到DataClean类的函数进行数据清洗"""
#     info_source = scrapy.Field(input_processor=MapCompose(DataClean.info_source))
#     job_name = scrapy.Field(input_processor=MapCompose(DataClean.job_name))
#     min_salary = scrapy.Field(input_processor=MapCompose(DataClean.min_salary))
#     max_salary = scrapy.Field(input_processor=MapCompose(DataClean.max_salary))
#     city = scrapy.Field(input_processor=MapCompose(DataClean.city))
#     company_name = scrapy.Field(input_processor=MapCompose(DataClean.company_name))
#     welfare = scrapy.Field(input_processor=MapCompose(DataClean.welfare))
#     work_years = scrapy.Field(input_processor=MapCompose(DataClean.work_years))
#     education = scrapy.Field(input_processor=MapCompose(DataClean.education))
#     address = scrapy.Field(input_processor=MapCompose(DataClean.address))
#     job_detail = scrapy.Field(input_processor=MapCompose(DataClean.job_detail))
