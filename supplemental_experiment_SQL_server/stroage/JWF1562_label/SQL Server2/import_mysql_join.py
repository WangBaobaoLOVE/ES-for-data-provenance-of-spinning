import pyodbc
import pandas as pd
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

tables = ['cusha_to_xisha1','cusha_to_xisha2','cusha_to_xisha3','cusha_to_xisha4','cusha_to_xisha5','cusha_to_xisha6','cusha_to_xisha7','cusha_to_xisha8','cusha_to_xisha9','cusha_to_xisha10','cusha_to_xisha11','cusha_to_xisha12']
labels_num = {'cusha_to_xisha1':1,'cusha_to_xisha2':2,'cusha_to_xisha3':3,'cusha_to_xisha4':4,'cusha_to_xisha5':5,'cusha_to_xisha6':6,'cusha_to_xisha7':7,'cusha_to_xisha8':8,'cusha_to_xisha9':9,'cusha_to_xisha10':10,'cusha_to_xisha11':11,'cusha_to_xisha12':12}

columns_name = 'record_id_xisha, record_id_cusha'

for table in tables:
    for cpnum in range(1,10001):
        for label_num in range(labels_num[table]):
            values = '{},{}'.format(cpnum, 1+label_num)
            
            print(table+'-'+str(cpnum)+'-'+str(label_num))
            
            # SQL 插入语句
            sql = "INSERT INTO {}({}) VALUES ({})".format(table, columns_name, values)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                print('error')
                db.rollback()

# 关闭数据库连接
db.close()

