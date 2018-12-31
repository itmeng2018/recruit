# import random
#
# import requests
# from lxml import etree
# from requests import ConnectTimeout
#
# from recruit_spider.city_by_boss import CITY_TUPLE
#
# # fp = open('../test.html')
# # html_str = fp.read()
# # fp.close()
# #
# # html = etree.HTML(html_str)
# #
# # li_list = html.xpath('//div[@id="main"]//div[@class="job-list"]/ul/li')
# #
# # for li in li_list:
# #     s = li.xpath('.//div[@class="info-primary"]//a/@href')[0]
# #     print('https://www.zhipin.com' + s)
#
# # count = 0
# # for i in CITY_TUPLE:
# #     if i.get('subLevelModelList'):
# #         for j in i.get('subLevelModelList'):
# #             print(j, count)
# #             count += 1
#
# # city_list = [i for j in  for i in j]
#
# # sub_list = [city.get('subLevelModelList') for city in CITY_TUPLE if city.get('subLevelModelList')]
# # city_list = [i['code'] for j in sub_list for i in j]
# # print(len(city_list))
# # print(city_list)
#
# from headers import UserAgent
#
# ips = [
#     {'https': 'http://60.169.126.222:58692'},
#     {'https': '123.55.101.108:22908'},
#     {'https': '125.72.232.150:41171'},
#     {'https': '115.202.226.179:39583'},
#     {'https': '114.228.133.202:26230'},
#     {'https': '220.163.67.16:19884'},
#     {'https': '175.174.83.192:4250'},
#     {'https': '117.45.217.251:17263'},
#     {'https': '175.43.85.119:19299'},
#     {'https': '27.152.124.210:54821'},
#     {'https': '119.101.112.109:9999'},
#
# ]
#
# ua = UserAgent()
# url = 'http://www.baidu.com'
# # for ip in ips:
# #     try:
# #         res = requests.get(url, headers=ua.get_headers(), proxies={'https': '119.101.112.109:9999'}, timeout=5)
# #     except ConnectTimeout:
# #         print('1', ip)
# #         continue
# #     if res.status_code == 200:
# #         print(ip)
# #     else:
# #         print('2', ip)
#
# res = requests.get(url, proxies={'https': '119.101.112.109:9999'}, timeout=5, verify=False)
# print(res.status_code)

# s = 'https://search.51job.com/list/311100'
#
# print(s[30:36])
#
# def a():
#     for i in range(10):
#         yield i
#
#
# c = a()
# for i in c:
#     print(i)