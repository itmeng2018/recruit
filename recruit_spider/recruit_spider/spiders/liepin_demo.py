# import re
# import requests
#
# urls = '''https://www.liepin.com/job/1916264273.shtml
# https://www.liepin.com/job/1915992827.shtml
# https://www.liepin.com/job/1916170227.shtml
# https://www.liepin.com/job/1914651502.shtml
# https://www.liepin.com/job/1914118025.shtml
# https://www.liepin.com/job/1916171285.shtml
# https://www.liepin.com/job/1916113567.shtml
# https://www.liepin.com/job/1915577937.shtml
# https://www.liepin.com/job/1915612897.shtml
# https://www.liepin.com/job/1913251008.shtml
# https://www.liepin.com/job/1915627832.shtml
# https://www.liepin.com/job/1915542030.shtml
# https://www.liepin.com/job/1915527750.shtml
# https://www.liepin.com/job/1915992829.shtml
# https://www.liepin.com/job/1915557273.shtml
# https://www.liepin.com/job/1914919328.shtml
# https://www.liepin.com/job/1916494277.shtml
# https://www.liepin.com/job/1916069419.shtml
# https://www.liepin.com/job/1915225111.shtml
# https://www.liepin.com/job/1915834314.shtml
# https://www.liepin.com/job/1916456585.shtml
# https://www.liepin.com/job/1916449903.shtml
# https://www.liepin.com/job/1916163161.shtml
# https://www.liepin.com/job/1912822886.shtml
# https://www.liepin.com/job/199913336.shtml
# https://www.liepin.com/job/1912650288.shtml
# https://www.liepin.com/job/1912650323.shtml
# https://www.liepin.com/job/1916117631.shtml
# https://www.liepin.com/job/199913341.shtml
# https://www.liepin.com/job/197350848.shtml
# https://www.liepin.com/job/199663051.shtml
# https://www.liepin.com/job/1915230989.shtml
# https://www.liepin.com/job/1916456685.shtml
# https://www.liepin.com/job/1916454109.shtml
# https://www.liepin.com/job/199310018.shtml
# https://www.liepin.com/job/1915557369.shtml
# https://www.liepin.com/job/1916415193.shtml
# https://www.liepin.com/job/1916034693.shtml
# https://www.liepin.com/job/1916347129.shtml
# https://www.liepin.com/job/1915610661.shtml
# https://www.liepin.com/job/1916337215.shtml
# https://www.liepin.com/job/1913095613.shtml
# https://www.liepin.com/job/1915462790.shtml
# https://www.liepin.com/job/1915859281.shtml
# https://www.liepin.com/job/1915343229.shtml
# https://www.liepin.com/job/194420253.shtml
# https://www.liepin.com/job/1915612907.shtml
# https://www.liepin.com/job/1915767916.shtml
# https://www.liepin.com/job/1915139756.shtml
# https://www.liepin.com/job/1915973347.shtml
# https://www.liepin.com/job/1912583876.shtml
# https://www.liepin.com/job/1912583874.shtml
# https://www.liepin.com/job/1912098742.shtml
# https://www.liepin.com/job/1915954653.shtml
# https://www.liepin.com/job/21412271200.shtml
# https://www.liepin.com/job/21412270368.shtml
# https://www.liepin.com/job/21412269235.shtml
# https://www.liepin.com/job/21412267139.shtml
# https://www.liepin.com/job/21412266027.shtml
# https://www.liepin.com/job/21412264720.shtml
# https://www.liepin.com/job/21412264719.shtml
# https://www.liepin.com/job/21412258485.shtml
# https://www.liepin.com/job/21412257939.shtml
# https://www.liepin.com/job/21412254662.shtml
# https://www.liepin.com/job/1912128214.shtml
# https://www.liepin.com/job/1916427871.shtml
# https://www.liepin.com/job/1916353319.shtml
# https://www.liepin.com/job/1915976489.shtml
# https://www.liepin.com/job/1915817546.shtml
# https://www.liepin.com/job/1914813826.shtml
# https://www.liepin.com/job/1915817378.shtml
# https://www.liepin.com/job/1915815157.shtml
# https://www.liepin.com/job/1915813740.shtml
# https://www.liepin.com/job/1915131063.shtml
# https://www.liepin.com/job/21412271200.shtml
# https://www.liepin.com/job/21412270368.shtml
# https://www.liepin.com/job/21412269235.shtml
# https://www.liepin.com/job/21412267139.shtml
# https://www.liepin.com/job/21412266027.shtml
# https://www.liepin.com/job/21412264720.shtml
# https://www.liepin.com/job/21412264719.shtml
# https://www.liepin.com/job/21412258485.shtml
# https://www.liepin.com/job/21412257939.shtml
# https://www.liepin.com/job/21412254662.shtml
# https://www.liepin.com/job/1916477951.shtml
# https://www.liepin.com/job/1914118024.shtml
# https://www.liepin.com/job/1915783084.shtml
# https://www.liepin.com/job/1915830854.shtml
# https://www.liepin.com/job/1915765103.shtml
# https://www.liepin.com/job/1912909611.shtml
# https://www.liepin.com/job/1916469051.shtml
# https://www.liepin.com/job/1915918003.shtml
# https://www.liepin.com/job/1915582358.shtml
# https://www.liepin.com/job/1915542028.shtml
# https://www.liepin.com/job/1916264273.shtml
# https://www.liepin.com/job/1915992827.shtml
# https://www.liepin.com/job/1916170227.shtml
# https://www.liepin.com/job/1914651502.shtml
# https://www.liepin.com/job/1914118025.shtml
# https://www.liepin.com/job/1916171285.shtml
# https://www.liepin.com/job/1916113567.shtml
# https://www.liepin.com/job/1915577937.shtml
# https://www.liepin.com/job/1915612897.shtml
# https://www.liepin.com/job/1913251008.shtml
# https://www.liepin.com/job/1915627832.shtml
# https://www.liepin.com/job/1915542030.shtml
# https://www.liepin.com/job/1915527750.shtml
# https://www.liepin.com/job/1915992829.shtml
# https://www.liepin.com/job/1915557273.shtml
# https://www.liepin.com/job/1913442846.shtml
# https://www.liepin.com/job/1915567885.shtml
# https://www.liepin.com/job/1915567981.shtml
# https://www.liepin.com/job/1915439764.shtml
# https://www.liepin.com/job/1915042347.shtml
# https://www.liepin.com/job/1912126014.shtml
# https://www.liepin.com/job/1915073430.shtml
# https://www.liepin.com/job/1916119219.shtml
# https://www.liepin.com/job/1915230995.shtml
# https://www.liepin.com/job/1915394999.shtml
# https://www.liepin.com/job/1916212167.shtml
# https://www.liepin.com/job/1915612905.shtml
# https://www.liepin.com/job/1915663830.shtml
# https://www.liepin.com/job/21412271200.shtml
# https://www.liepin.com/job/21412270368.shtml
# https://www.liepin.com/job/21412269235.shtml
# https://www.liepin.com/job/21412267139.shtml
# https://www.liepin.com/job/21412266027.shtml
# https://www.liepin.com/job/21412264720.shtml
# https://www.liepin.com/job/21412264719.shtml
# https://www.liepin.com/job/21412258485.shtml
# https://www.liepin.com/job/21412257939.shtml
# https://www.liepin.com/job/21412254662.shtml
# https://www.liepin.com/job/1916476573.shtml
# https://www.liepin.com/job/1915492176.shtml
# https://www.liepin.com/job/1913341112.shtml
# https://www.liepin.com/job/1913151885.shtml
# https://www.liepin.com/job/1911219861.shtml
# https://www.liepin.com/job/1914657521.shtml
# https://www.liepin.com/job/1915886151.shtml
# https://www.liepin.com/job/1915752396.shtml
# https://www.liepin.com/job/1914523484.shtml
# https://www.liepin.com/job/1916401819.shtml
# https://www.liepin.com/job/1916240885.shtml
# https://www.liepin.com/job/1916155431.shtml
# https://www.liepin.com/job/1914641057.shtml
# https://www.liepin.com/job/1914680866.shtml
# https://www.liepin.com/job/1913531854.shtml
# https://www.liepin.com/job/1916478287.shtml
# https://www.liepin.com/job/1915792718.shtml
# https://www.liepin.com/job/1915536758.shtml'''
# url_list = [i for i in urls.split('\n')]
# count = 1
# for url in url_list:
#     try:
#         html_str = requests.get(url).content.decode()
#         job_name = re.findall('var \$CONFIG = .*?"title": "(.*?)",', html_str, re.DOTALL)[0]
#         money = re.findall('var \$CONFIG = .*?"salary": "(.*?)",', html_str, re.DOTALL)[0]
#         city = re.findall('var \$CONFIG = .*?"dqName": "(.*?)",', html_str, re.DOTALL)[0]
#         company = re.findall('var \$CONFIG = .*?"company": "(.*?)",', html_str, re.DOTALL)[0]
#         print(job_name, money, city, company)
#     except Exception as e:
#         print(url, e)
#         count += 1
# print(len(url_list), count)


# money = '22.0$36.0'
# min_salary = int(float(money.split('$')[0]) * 10000 / 12)
# max_salary = int(float(money.split('$')[1]) * 10000 / 12)
# print(min_salary, max_salary)
# print(int(min_salary), int(max_salary))