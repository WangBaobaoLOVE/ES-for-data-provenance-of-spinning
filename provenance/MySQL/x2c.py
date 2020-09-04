import pandas as pd
import pymysql
import random

# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

tables = ['x2c1', 'x2c2','x2c3','x2c4','x2c5','x2c6']
labels_num = {'x2c1':1, 'x2c2':2,'x2c3':3,'x2c4':4,'x2c5':5,'x2c6':6}

columns_name = 'record_id_xisha, record_id_cusha'

sql = "select min(record_id) from JWF1418_cusha"
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
min_id = cursor.fetchone()[0]

sql = "select max(record_id) from JWF1418_cusha"
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
max_id = cursor.fetchone()[0]

for table in tables:
    sql = "select record_id from JWF1562_xisha"
    cursor.execute(sql)
    db.commit()
    results = cursor.fetchall()
    for record_id in results: 
        for i in range(labels_num[table]):
            values = ''
            values = str(record_id[0]) + ',' + str(random.randint(min_id, max_id))
            values = values.replace('nan','0')
            
            # SQL 插入语句
            sql = "INSERT INTO {}({}) VALUES ({})".format(table, columns_name, values)
            print(sql)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                db.rollback()
print('Over')
# 关闭数据库连接
db.close()
