# -*- coding: utf-8 -*-
import json
import re

from scrapy import Spider, Request

from recruit_spider.city_by_zhilian import CITY_LIST
from recruit_spider.items import RecruitSpiderItem


class ZhilianSpider(Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    temp = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=100&cityId={}&kw=python&kt=3'

    @staticmethod
    def extract_url(data):
        result = data['data']['results']
        if result:
            for item in result:
                yield item.get('positionURL')

    def start_requests(self):
        for city in CITY_LIST:
            for i in range(11):
                start_url = ZhilianSpider.temp.format(i * 100, city.get('code'))
                yield Request(url=start_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        data = json.loads(response.body.decode(), encoding='utf-8')
        result = self.extract_url(data)
        for url in result:
            yield Request(url=url, callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        item = RecruitSpiderItem()
        html_str = response.text
        item['info_source'] = '2'
        regex = re.compile(
            r'<meta name="description" content="(?P<cname>.*?)诚聘(?P<job_name>.*?)\d+人，工作地点位于(?P<city>.*?)，薪资待遇(?P<sal>.*?)，学历要求(?P<edu>.*?)或以上，工作经验(?P<exp>.*?)等更多招聘')
        item['company_name'], item['job_name'], item['city'], money, item['education'], item['work_years'] = \
        regex.findall(html_str)[0]
        if '面议' not in money:
            item['min_salary'] = money.split('-')[0]
            item['max_salary'] = money.split('-')[1][:-3]
        else:
            item['min_salary'] = money
            item['max_salary'] = money
        item['address'] = response.xpath('//p[@class="add-txt"]/text()').extract_first()
        item['welfare'] = re.findall("var JobWelfareTab\s=\s['\"](.*?)['\"];", html_str)[0]
        job_detail_result = response.xpath('//div[@class="pos-ul"]//text()').extract()
        item['job_detail'] = ''.join([i for i in job_detail_result if not i.isspace() and i != '展开'])
        yield item
