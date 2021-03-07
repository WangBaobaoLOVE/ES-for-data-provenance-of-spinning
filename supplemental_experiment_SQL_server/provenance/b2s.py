import random
import pyodbc

# 连接
db = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost;'
    r'DATABASE=mashan;'
    r'UID=SA;'
    r'PWD=Wbb123456'
    )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

tables = ['b2s1', 'b2s2','b2s3','b2s4','b2s5','b2s6']
labels_num = {'b2s1':1, 'b2s2':2,'b2s3':3,'b2s4':4,'b2s5':5,'b2s6':6}

columns_name = 'record_id_bingtiao, record_id_shumian'

sql = "select min(record_id) from JWF1211_shumuan"
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
# db.commit()
min_id = cursor.fetchone()[0]

sql = "select max(record_id) from JWF1211_shumuan"
print(sql)
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
# db.commit()
max_id = cursor.fetchone()[0]

for table in tables:
    sql = "select record_id from JWF1312B_bingtiao"
    cursor.execute(sql)
    # db.commit()
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
