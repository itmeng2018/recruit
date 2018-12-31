import sqlite3


class RecruitSpiderPipeline(object):
    count = 1

    def process_item(self, item, spider):
        connect = sqlite3.connect('recruit.db')
        cursor = connect.cursor()
        save_dict = {
            "info_source": item['info_source'],
            "job_name": item['job_name'],
            "min_salary": item['min_salary'],
            "max_salary": item['max_salary'],
            "city": item['city'],
            "company_name": item['company_name'],
            "welfare": item['welfare'],
            "work_years": item['work_years'],
            "education": item['education'],
            "address": item['address'],
            "job_detail": item['job_detail'],
        }
        sql_insert = """insert into recruit(
                            `info_source`, `job_name`, `min_salary`, `max_salary`, `city`, `compnay_name`, 
                            `welfare`, `work_years`, `education`, `address`, `job_detail`) 
                        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        param = (
            item['info_source'], item['job_name'], item['min_salary'],
            item['max_salary'], item['city'], item['company_name'],
            item['welfare'], item['work_years'], item['education'],
            item['address'], item['job_detail']
        )
        cursor.execute(sql_insert, param)
        connect.commit()
        print('插入第%d条数据' % RecruitSpiderPipeline.count)
        RecruitSpiderPipeline.count += 1
        return item
