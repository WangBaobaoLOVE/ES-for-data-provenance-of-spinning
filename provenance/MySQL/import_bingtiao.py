import pandas as pd
import pymysql
import random

data_bingtiao = pd.read_csv('../data/JWF1312B_bingtiao.csv')
a = data_bingtiao['record_timestamp']
b = pd.to_datetime(a)
print(min(b))
print(max(b))
data_bingtiao['record_timestamp'] = b
data_bingtiao = data_bingtiao[data_bingtiao['record_timestamp']>pd.to_datetime('2018-06-30')]
data_bingtiao = data_bingtiao[data_bingtiao['record_timestamp']<pd.to_datetime('2019-03-30')]
data_bingtiao = data_bingtiao.sort_values('record_timestamp')

# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

tables = ['JWF1312B_bingtiao1', 'JWF1312B_bingtiao2','JWF1312B_bingtiao3','JWF1312B_bingtiao4','JWF1312B_bingtiao5','JWF1312B_bingtiao6']
labels_num = {'JWF1312B_bingtiao1':1, 'JWF1312B_bingtiao2':2,'JWF1312B_bingtiao3':3,'JWF1312B_bingtiao4':4,'JWF1312B_bingtiao5':5,'JWF1312B_bingtiao6':6}

columns_name = ''
for column in data_bingtiao.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name + 'record_id_shumian'

sql = "select min(record_id) from JWF1211_shumuan"
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
min_id = cursor.fetchone()[0]

sql = "select max(record_id) from JWF1211_shumuan"
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
max_id = cursor.fetchone()[0]

for table in tables:
	for row in range(data_bingtiao.shape[0]):
		for label_num in range(labels_num[table]):
			values = ''
			for i in range(data_bingtiao.shape[1]):
				if i == 1:
				    values = values + '\'' + str(data_bingtiao.iloc[row,i]) + '\''+ ','
				else: 
				    values = values + str(data_bingtiao.iloc[row,i]) + ','
			record_id_shumian = random.randint(min_id,max_id)
			values = values + str(record_id_shumian)
			values = values.replace('nan','0')

			print(table + '-' + str(row) + '-' + str(label_num))
			# SQL 插入语句
			sql = "INSERT INTO {}({}) VALUES ({})".format(table, columns_name, values)
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
