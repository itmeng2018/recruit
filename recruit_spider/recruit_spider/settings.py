# -*- coding: utf-8 -*-
from headers import UserAgent

# 爬虫名
BOT_NAME = 'recruit_spider'
SPIDER_MODULES = ['recruit_spider.spiders']
NEWSPIDER_MODULE = 'recruit_spider.spiders'

# 是否解析 robots.txt
ROBOTSTXT_OBEY = False

#  配置Scrapy执行的最大并发请求数 (默认: 16)
CONCURRENT_REQUESTS = 128

# 配置时间间隔
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# 禁用cookies (默认启用)
# COOKIES_ENABLED = False

# 禁用Telnet控制台 (默认启用)
# TELNETCONSOLE_ENABLED = False

# 覆盖默认请求头:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# 爬虫中间件
# SPIDER_MIDDLEWARES = {
#    'recruit_spider.middlewares.RecruitSpiderSpiderMiddleware': 543,
# }

# 下载中间件
DOWNLOADER_MIDDLEWARES = {
    'recruit_spider.middlewares.RecruitSpiderDownloaderMiddleware': 543,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 123,
    # 'modetest.middlewares.IPPOOlS': 125
}

# 启用或禁用扩展
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 配置 item pipelines
ITEM_PIPELINES = {
    'recruit_spider.pipelines.RecruitSpiderPipeline': 300,
}

# 配置log日志等级
# LOG_LEVEL = 'DEBUG'
# LOG_LEVEL = 'INFO'
LOG_LEVEL = 'ERROR'

# 启用和配置自动限速扩展
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# 启用和配置HTTP缓存 (默认禁用)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'