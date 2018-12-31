# import random
#
# import requests
#
# # https://www.xicidaili.com/nn/2
#
# from headers import UserAgent
# from requests import ConnectTimeout
#
#
# class Utils(object):
#
#     @staticmethod
#     def get_ip():
#         ips = [
#             {'https': '60.169.126.222:58692'},
#             {'https': '123.55.101.108:22908'},
#             {'https': '125.72.232.150:41171'},
#             {'https': '115.202.226.179:39583'},
#             {'https': '114.228.133.202:26230'},
#             {'https': '220.163.67.16:19884'},
#             {'https': '175.174.83.192:4250'},
#             {'https': '117.45.217.251:17263'},
#             {'https': '175.43.85.119:19299'},
#             {'https': '27.152.124.210:54821'},
#             {'https': '119.101.112.109:9999'}
#         ]
#         return random.choice(ips)
#
#     @staticmethod
#     def get_ua():
#         ua = UserAgent()
#         return ua.get_headers()
#
#     @staticmethod
#     def check_ip(ip, agr):
#         user_agent = {
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36'}
#         if agr not in ['http', 'https']:
#             return False
#
#         if agr == 'http':
#             url = 'http://www.itmeng.top'
#         else:
#             url = 'https://www.baidu.com'
#         try:
#             requests.get(url=url, proxies=ip, headers=user_agent, timeout=5, verify=False)
#             result = True
#         except ConnectTimeout:
#             result = False
#         return result
#
#
# class ProxySpider(Utils):
#     def __init__(self):
#         self.url_template = "https://www.xicidaili.com/wn/{}"
#
#     def download(self, url):
#         ua = self.get_ua()
#         ip = self.get_ip()
#         try:
#             response = requests.get(url=url, headers=ua, verify=False, timeout=5)
#         except ConnectTimeout:
#             print('----over----')
#             response = None
#             self.download(url)
#
#         return response
#
#     def run(self):
#         url = "https://www.xicidaili.com/"
#         response = self.download(url)
#         print(response.content.decode())
#
#
# spider = ProxySpider()
# spider.run()

