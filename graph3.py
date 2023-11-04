import pandas as pd
import scipy.stats as states
import numpy as np
import matplotlib.pyplot as plt
import pymysql
k = np.arange(40)

params = [[20,0.5],[20,0.7],[40,0.5]]
style = ['o-b','d-r','s-g']
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='temp')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
db_settings = {
                     "host":'localhost',
                     "user":'root',
                     "password":'123456',
                     "db":'temp'

}
conn = pymysql.connect(**db_settings)

try:
    with conn.cursor() as cursor:
        command = f"INSERT INTO temp(timStamp ,temperature ,humidity ) values(%s,%s,%s)"

        cursor.execute(command,(11,"20","0.5"))

        print("資料新增完成")

        conn.commit()

except Exception as ex:
    print(ex)

# 使用 execute()  方法执行 SQL 查询
#cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
#data = cursor.fetchone()
