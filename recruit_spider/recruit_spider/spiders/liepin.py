# # -*- coding: utf-8 -*-
# import re
#
# from scrapy import Request, Spider
# from recruit_spider.city_by_liepin import CITY_LIST
# from recruit_spider.items import RecruitSpiderItem
#
#
# class Factory(object):
#
#     def __init__(self):
#         self.domain = 'https://www.liepin.com'
#
#     def format_url(self, city_code, page):
#         template = self.domain + '/{}/zhaopin/pn{}?key=python'
#         return template.format(city_code, page)
#
#
# class LiepinSpider(Spider):
#     name = 'liepin'
#     allowed_domains = ['liepin.com']
#
#     @staticmethod
#     def get_max_page(response):
#         max_page = re.findall("\$pn=Math.min\(Math.max\(\$pn, 1\),(\d+)\);location.href", response.text)[0]
#         if max_page.isdigit():
#             return int(max_page)
#
#     @staticmethod
#     def get_detail_url(response):
#         def check_url(url):
#             if re.match('https://www.liepin.com', url):
#                 return url
#             return "https://www.liepin.com" + url
#
#         li_list = response.xpath('//div[@class="recruit-left"]//ul[@class="sojob-list"]/li')
#         for li in li_list:
#             url = li.xpath('.//span[@class="job-name"]/a/@href').extract_first()
#             if url is None or url == '#':
#                 continue
#             yield check_url(url)
#
#     def start_requests(self):
#         factory = Factory()
#         for city in CITY_LIST:
#             start_url = factory.format_url(city.get('code'), 0)
#             yield Request(url=start_url, callback=self.parse, dont_filter=True)
#
#     def parse(self, response):
#         factory = Factory()
#         max_page = self.get_max_page(response)
#         if max_page is None:
#             max_page = 0
#         if max_page > 2:
#             for i in range(1, max_page):
#                 url = factory.format_url(re.findall("https://www.liepin.com/(.*?)/zhaopin", response.url)[0], i)
#                 yield Request(url=url, callback=self.parse_html, dont_filter=True)
#         else:
#             self.parse_html(response)
#
#     count = 0
#
#     def parse_html(self, response):
#         for url in self.get_detail_url(response):
#             yield Request(url=url, callback=self.parse_detail, dont_filter=True)
#
#     def parse_detail(self, response):
#         item = RecruitSpiderItem()
#         html_str = response.text
#         if not re.findall('该职位已结束', html_str):
#             item['info_source'] = '3'
#             item['job_name'] = re.findall('var \$CONFIG = .*?"title": "(.*?)",', html_str, re.DOTALL)[0]
#             money = re.findall('var \$CONFIG = .*?"salary": "(.*?)",', html_str, re.DOTALL)[0]
#             item['min_salary'] = int(float(money.split('$')[0]) * 10000 / 12)
#             item['max_salary'] = int(float(money.split('$')[1]) * 10000 / 12)
#             city_result = re.findall('var \$CONFIG = .*?"dqName": "(.*?)",', html_str, re.DOTALL)[0]
#             if '-' in city_result:
#                 item['city'] = city_result.split('-')[0]
#             else:
#                 item['city'] = city_result
#             item['company_name'] = re.findall('var \$CONFIG = .*?"company": "(.*?)",', html_str, re.DOTALL)[0]
#             item['education'] = response.xpath('//div[@class="job-qualifications"]/span[1]/text()').extract_first()
#             item['work_years'] = response.xpath('//div[@class="job-qualifications"]/span[2]/text()').extract_first()
#             welfare_list = response.xpath('//ul[@class="comp-tag-list clearfix"]/li/span/text()').extract()
#             if ','.join(welfare_list) == '':
#                 item['welfare'] = None
#             else:
#                 item['welfare'] = ','.join(welfare_list)
#             job_detail_list = response.xpath('//div[@class="content content-word"]/text()').extract()
#             item['job_detail'] = ','.join([i for i in job_detail_list if not i.isspace()]).strip()
#             try:
#                 item['address'] = re.findall('<li>公司地址：(.*?)</li>', html_str)[0]
#             except IndexError:
#                 item['address'] = None
#             # print(item)
#             yield item
