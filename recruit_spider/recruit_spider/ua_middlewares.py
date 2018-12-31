# from random import choice
# from headers import UserAgent
# from scrapy.downloadermiddlewares import httpproxy, useragent
#
#
# class IPPOOLS(httpproxy.HttpProxyMiddleware):
#
#     @staticmethod
#     def get_ip():
#         ips = [
#             'https://60.169.126.222:58692',
#             'https://123.55.101.108:22908',
#             'https://125.72.232.150:41171',
#             'https://115.202.226.179:39583',
#             'https://114.228.133.202:26230',
#             'https://220.163.67.16:19884',
#             'https://175.174.83.192:4250',
#             'https://117.45.217.251:17263',
#             'https://175.43.85.119:19299',
#             'https://27.152.124.210:54821'
#         ]
#         return choice(ips)
#
#     def __init__(self):
#         super().__init__()
#         self.ip = None
#
#     def process_request(self, request, spider):
#         # print('当前使用的代理是: ', self.get_ip())
#         request.meta['proxy'] = self.get_ip()
#
#
# class UAPOOLS(useragent.UserAgentMiddleware):
#     def __init__(self):
#         super().__init__()
#         self.user_agent = None
#
#     def process_request(self, request, spider):
#         ua = UserAgent()
#         this_ua = ua.get_headers()
#         request.headers.setdefault('User-Agent', this_ua)
