import pymysql
import pandas as pd
 
# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

tables = ['xishalabel1','xishalabel2','xishalabel3','xishalabel4','xishalabel5','xishalabel6','xishalabel7','xishalabel8','xishalabel9','xishalabel10','xishalabel11','xishalabel12']
nums = {'xishalabel1':1,'xishalabel2':2,'xishalabel3':3,'xishalabel4':4,'xishalabel5':5,'xishalabel6':6,'xishalabel7':7,'xishalabel8':8,'xishalabel9':9,'xishalabel10':10,'xishalabel11':11,'xishalabel12':12}
data = pd.read_csv('../../JWF1562_origin/MySQL/JWF1562.csv')


columns_name = 'before_record_id,'
for column in data.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name.strip(',')


for table in tables:
    for cpnum in range(10000):
        for num in range(nums[table]):
            values = '{}, \'2019-11-30 11:58:47\','.format(501+num)
            for i in range(1,data.shape[1]):
                values = values + str(data.iloc[cpnum,i]) + ','
            values = values.strip(',')
            values = values.replace('nan','0')

            print(table+'-'+str(cpnum)+'-'+str(num))
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

