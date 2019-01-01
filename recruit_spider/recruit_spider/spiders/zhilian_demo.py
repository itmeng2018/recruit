import requests
import re
import json
from lxml import etree
from recruit_spider.city_by_zhilian import CITY_LIST


class ZhilianSpider(object):
    def __init__(self):
        self.temp = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=100&cityId={}&kw=python&kt=3'

    @staticmethod
    def extract_url(result):
        for item in result:
            yield item.get('positionURL')

    @staticmethod
    def check_data(data):
        result = data['data']['results']
        if result:
            return result

    def make_url(self):
        return self.temp.format(0, 535)

    def download(self, url):
        data = json.loads(requests.get(url).content.decode(), encoding='utf-8')
        return self.check_data(data)

    def parse_detail(self, url):
        html_str = requests.get(url).content.decode('utf-8')
        regex = re.compile(r'<meta name="description" content="(?P<cname>.*?)诚聘(?P<job_name>.*?)\d+人，工作地点位于(?P<city>.*?)，薪资待遇(?P<sal>.*?)，学历要求(?P<edu>.*?)或以上，工作经验(?P<exp>.*?)等更多招聘')
        item = dict()
        print(url)
        item['cname'], item['jname'], item['city'], item['sal'], item['edu'], item['exp'] = regex.findall(html_str)[0]
        print(item)


    def run(self):
        url_str = self.make_url()
        result = self.download(url_str)
        urls = self.extract_url(result)
        for url in urls:
            self.parse_detail(url)



# spider = ZhilianSpider()
# spider.run()
# str1 = '<meta name="description" content="文思海辉技术有限公司 Pactera Technology International Limited诚聘C++开发工程师（懂python）1人，工作地点位于北京，薪资待遇面议，学历要求本科或以上，工作经验1-3年等更多招聘'
# regex = re.compile(
#     r'<meta name="description" content="(?P<cname>.*?)诚聘(?P<job_name>.*?)\d人，工作地点位于(?P<city>.*?)，薪资待遇(?P<sal>.*?)，学历要求(?P<edu>.*?)或以上，工作经验(?P<exp>.*?)等更多招聘')
#
# result = regex.findall(str1)
# print(result)

# str3 = "var JobWelfareTab = '14薪,住房补贴,每年多次调薪,周末双休,五险一金,年底双薪,包住,房补';"
# str4 = """        var FootJuSubJobTypes = '[{"Link":"http://jobs.zhaopin.com/hot_cppkfrjgcs/","Text":"C++开发软件工程师招聘"},{"Link":"http://jobs.zhaopin.com/hot_dcjkrjgcs/","Text":"底层监控软件工程师招聘"},{"Link":"http://jobs.zhaopin.com/hot_linuxqrsrjgcs/","Text":"LINUX嵌入式软件工程师招聘"},{"Link":"http://jobs.zhaopin.com/hot_yspcprjgcs/","Text":"音视频产品软件工程师招聘"},{"Link":"http://jobs.zhaopin.com/hot_javarjgcssys/","Text":"JAVA软件工程师实训生招聘"},{"Link":"http://jobs.zhaopin.com/hot_zxrjgcs/","Text":"在线软件工程师招聘"},{"Link":"http://jobs.zhaopin.com/hot_qrszdrjgcs/","Text":"嵌入式终端软件工程师招聘"},{"Link":"http://jobs.zhaopin.com/hot_zrrjgcs/","Text":"主任软件工程师招聘"},{"Link":"http://jobs.zhaopin.com/hot_spqdrjgcs/","Text":"视频驱动软件工程师招聘"},{"Link":"http://jobs.zhaopin.com/hot_dzybrjgcs/","Text":"电子仪表软件工程师招聘"},{"Link":"http://jobs.zhaopin.com/hot_vcpprjgcscxy/","Text":"VC++软件工程师程序员招聘"},{"Link":"http://jobs.zhaopin.com/hot_ioskfrjgcs/","Text":"IOS开发软件工程师招聘"}]';
#         //周边城市
#         var FootCitys = '[{"link":"http://jobs.zhaopin.com/dalian/","Text":"大连人才网"},{"link":"http://jobs.zhaopin.com/fushun/","Text":"抚顺人才网"},{"link":"http://jobs.zhaopin.com/dandong/","Text":"丹东人才网"},{"link":"http://jobs.zhaopin.com/jinzhou/","Text":"锦州人才网"},{"link":"http://jobs.zhaopin.com/yingkou/","Text":"营口人才网"},{"link":"http://jobs.zhaopin.com/liaoyang/","Text":"辽阳人才网"},{"link":"http://jobs.zhaopin.com/panjin/","Text":"盘锦人才网"},{"link":"http://jobs.zhaopin.com/tieling/","Text":"铁岭人才网"}]';
#         var TravelOption = '0';
#
#         var SkillLabel = '';
#         var JobWelfareTab = '14薪,住房补贴,每年多次调薪,周末双休,五险一金,年底双薪,包住,房补';
#
#     </script>
# </head>
# <body>
# <div class="wrap">
# <div class="advertising">"""
# welfare = re.findall("var JobWelfareTab\s=\s['\"](.*?)['\"];", str4)[0]
# print(welfare)

# url = "https://jobs.zhaopin.com/120220260270263.htm"
# response = etree.HTML(requests.get(url).text)
# job_detail_result = response.xpath('//div[@class="pos-ul"]//text()')
# job_detail = ''.join([i for i in job_detail_result if not i.isspace() and i !='展开'])
# print(job_detail)