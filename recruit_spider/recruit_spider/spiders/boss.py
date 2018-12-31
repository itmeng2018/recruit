# # -*- coding: utf-8 -*-
# import scrapy
# from recruit_spider.city_by_boss import CITY_TUPLE
#
#
# class MakeURL(object):
#
#     def __init__(self):
#         self.domain = 'https://www.zhipin.com'
#
#     def format_url(self, city_code, page):
#         template = self.domain + '/c{}/?query=python&page={}'
#         return template.format(city_code, page)
#
#     def complement_url(self, route):
#         return self.domain + route
#
#
# class BossSpider(scrapy.Spider):
#     """Boss直聘爬虫, 一共371个城市, 每个城市都有10个页面"""
#     name = 'boss'
#     allowed_domains = ['zhipin.com']
#     count = 1
#
#     def start_requests(self):
#         """定义起始请求页"""
#         city_codes = ['100010000']
#         sub_list = [city.get('subLevelModelList') for city in CITY_TUPLE if city.get('subLevelModelList')]
#         city_codes.extend([i['code'] for j in sub_list for i in j if i.get('code')])
#         make_url = MakeURL()
#         for city_code in city_codes:
#             for page in range(1, 11):
#                 start_url = make_url.format_url(city_code, page)
#                 yield scrapy.Request(url=start_url, callback=self.parse, dont_filter=True)
#
#     def parse(self, response):
#
#         '''
#         https://www.zhipin.com/job_detail/748e99363f53f18f1XJ52Nq_ElA~.html?ka=search_list_1_blank&lid=1fVRFqT2N2k.search
#         href      ka  target     data-itemid  data-lid
#
#         /div[@class="info-primary"]//a/@href   /job_detail/748e99363f53f18f1XJ52Nq_ElA~.html
#         //div[@class="info-primary"]//a/@ka    search_list_1
#         //div[@class="info-primary"]//a/@target    _blank
#         //div[@class="info-primary"]//a/@data-lid
#         '''
#
#         if len(response.url) > 55:
#             input()
#         print(BossSpider.count, response.url)
#         BossSpider.count += 1
