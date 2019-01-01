# # -*- coding: utf-8 -*-
# import re
# import logging
# import scrapy
# from recruit_spider.items import RecruitSpiderItem
# from recruit_spider.city_by_wy import CITY_DICT
#
#
# class MakeURL(object):
#
#     def __init__(self):
#         self.domain = 'https://search.51job.com'
#
#     def format_url(self, city_code, page):
#         template = self.domain + '/list/{},000000,0000,00,9,99,python,2,{}.html'
#         return template.format(city_code, page)
#
#
# class BossSpider(scrapy.Spider):
#     """Boss直聘爬虫, 一共371个城市, 每个城市都有10个页面"""
#     name = 'wuyou'
#     allowed_domains = ['51job.com']
#     count = 0
#     url_list = []
#
#     def start_requests(self):
#         """定义起始请求页"""
#
#         make_url = MakeURL()
#         for city_code in CITY_DICT:
#             start_url = make_url.format_url(city_code, 1)
#             yield scrapy.Request(url=start_url, callback=self.parse, dont_filter=True)
#
#     @staticmethod
#     def parse_page(response):
#
#         if re.search('<p class="dw_nomsg">', response.text) is None:
#             page_html = response.xpath('//div[@id="resultList"]//span[@class="og_but"]/@onclick').extract_first()
#             if page_html is not None and page_html != '' and page_html != '0':
#                 return page_html.split("'")[1]
#
#     @staticmethod
#     def extract_detail_url(response):
#         div_list = response.xpath('//div[@id="resultList"]/div[@class="el"]')
#         for div in div_list:
#             detail_url = div.xpath('./p[starts-with(class, t1)]//a/@href').extract_first()
#             yield detail_url
#
#     def parse(self, response):
#         make_url = MakeURL()
#         result = self.parse_page(response)
#         if result is not None:
#             total_page = int(result)
#         else:
#             total_page = 0
#
#         url_list = self.extract_detail_url(response)
#         for url in url_list:
#             yield scrapy.Request(url=url, callback=self.parse_detail, dont_filter=True)
#         if total_page > 2:
#             for i in range(2, int(total_page) + 1):
#                 url = make_url.format_url(response.url[30:36], i)
#                 yield scrapy.Request(url=url, callback=self.parse_html, dont_filter=True)
#         elif total_page == 2:
#             url = make_url.format_url(response.url[30:36], 2)
#             yield scrapy.Request(url=url, callback=self.parse_html, dont_filter=True)
#
#     def parse_html(self, response):
#         url_list = self.extract_detail_url(response)
#         for url in url_list:
#             yield scrapy.Request(url=url, callback=self.parse_detail, dont_filter=True)
#
#     def parse_detail(self, response):
#         item = RecruitSpiderItem()
#         item['info_source'] = '1'
#
#         try:
#             item['job_name'] = response.xpath('//div[@class="cn"]/h1/@title').extract_first().strip()
#             salary = response.xpath('//div[@class="cn"]/strong/text()').extract_first().split('-')
#             if '千' in salary[-1]:
#                 money = 1000
#             else:
#                 money = 10000
#
#             item['min_salary'] = str(float(salary[0]) * money)
#             item['max_salary'] = str(float(''.join([i for i in salary[1] if i.isdigit() or i == '.'])) * money)
#             item['company_name'] = response.xpath('//div[@class="cn"]//a[@class="catn"]/@title').extract_first()
#             edu_and_year = response.xpath('//div[@class="cn"]/p[@class="msg ltype"]/@title').extract_first().split('|')
#             item['city'] = edu_and_year[0].strip()
#             item['work_years'] = edu_and_year[1].strip()
#             item['education'] = edu_and_year[2].strip()
#             item['welfare'] = ','.join(response.xpath('//div[@class="cn"]//span[@class="sp4"]/text()').extract())
#             address = response.xpath('//div[@class="tCompany_main"]//p[@class="fp"]/text()').extract()[-1].strip()
#             # print(address)
#             item['address'] = address
#             job_detail = response.xpath('//div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/p/text()')
#             item['job_detail'] = '\n'.join(job_detail.extract())
#             yield item
#         except Exception as e:
#             logging.debug(e)
