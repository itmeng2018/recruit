# import requests
# from lxml import etree

# url = "https://search.51job.com/list/170200,000000,0000,00,9,99,python,2,1.html"
# url = "https://jobs.51job.com/guanchenghuizuqu/109386637.html?s=01&t=0"
# url = "https://jobs.51job.com/jinshuiqu/107794982.html?s=01&t=0"
# html_str = requests.get(url).content.decode('gbk')

# print(response)

# fp = open('detail.html')
# html_str = fp.read()
# fp.close()
#
# html = etree.HTML(html_str)
#
# div_list = html.xpath('//div[@id="resultList"]/div[@class="el"]')
# for div in div_list:  #
#     # detail_url = div.xpath('./p[@class="t1"]//a/@href')
#     detail_url = div.xpath('./p[starts-with(class, t1)]//a/@href')
#     print(detail_url)

# job_name = html.xpath('//div[@class="cn"]/h1/@title')[0]  # ok
# salary = html.xpath('//div[@class="cn"]/strong/text()')[0]  # ok
# company_name = html.xpath('//div[@class="cn"]//a[@class="catn"]/@title')[0]  # ok
# edu_and_year = html.xpath('//div[@class="cn"]/p[@class="msg ltype"]/@title')[0].split('|')  # 郑州-管城回族区  |  无工作经验  |  大专  |  招若干人  |  12-29发布
# welfare = html.xpath('//div[@class="cn"]//span[@class="sp4"]/text()') # ['五险一金', '绩效奖金', '年终奖金', '补充医疗保险', '补充公积金', '员工旅游', '出国机会', '专业培训', '弹性工作', '股票期权']
# addr = html.xpath('//div[@class="tCompany_main"]//p[@class="fp"]/text()')[-1].strip()
# job_detail = html.xpath('//div[@class="tCompany_main"]//div[@class="bmsg job_msg inbox"]/p/text()')
# print('job_name: ',job_name)
# print('salary: ', salary)
# print('company_name', company_name)
# print('edu_and_year', edu_and_year)
# print('welfare', welfare)
# print('addr', addr)
# print('job_detail', job_detail)

# salary = html.xpath('//div[@class="cn"]/strong/text()')[0].split('-')
# min_salary = str(float(salary[0]) * 1000)
# max_salary = str(float(''.join([i for i in salary[1] if i.isdigit() or i == '.'])) * 1000)  # 6千/月
#
# print(min_salary, max_salary)
#
# work_years = edu_and_year[1].strip()
# education = edu_and_year[2].strip()
# print(work_years, education)

# str1 = '''</div>
#
#                     <p class="dw_nmsg">对不起，没有找到符合你条件的职位！</p>
#             <!--列表表格 END-->
#         <div class="dw_line"></div>
# '''
# import re
# s = re.search('<p class="dw_nomsg">', str1)
# print(s)
