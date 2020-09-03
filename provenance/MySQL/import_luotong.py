import pandas as pd
import pymysql
import random

data_luotong = pd.read_csv('../data/SMARO-E_luotong.csv')
a = data_luotong['record_timestamp']
b = pd.to_datetime(a)
print(min(b))
print(max(b))
data_luotong['record_timestamp'] = b
data_luotong = data_luotong[data_luotong['record_timestamp']>pd.to_datetime('2018-06-30')]
data_luotong = data_luotong[data_luotong['record_timestamp']<pd.to_datetime('2019-03-30')]
data_luotong = data_luotong.sort_values('record_timestamp')

# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

tables = ['SMARO_E_luotong1', 'SMARO_E_luotong2','SMARO_E_luotong3','SMARO_E_luotong4','SMARO_E_luotong5','SMARO_E_luotong6']
labels_num = {'SMARO_E_luotong1':1, 'SMARO_E_luotong2':2,'SMARO_E_luotong3':3,'SMARO_E_luotong4':4,'SMARO_E_luotong5':5,'SMARO_E_luotong6':6}

columns_name = ''
for column in data_luotong.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name + 'record_id_xisha'

for table in tables:
	sql = "select min(record_id) from JWF1562_xisha{}".format(labels_num[table])
	# 执行sql语句
	cursor.execute(sql)
	# 提交到数据库执行
	db.commit()
	min_id = cursor.fetchone()[0]

	sql = "select max(record_id) from JWF1562_xisha{}".format(labels_num[table])
	# 执行sql语句
	cursor.execute(sql)
	# 提交到数据库执行
	db.commit()
	max_id = cursor.fetchone()[0]

	for row in range(data_luotong.shape[0]):
		for label_num in range(labels_num[table]):
			values = ''
			for i in range(data_luotong.shape[1]):
				if i == 0:
				    values = values + '\'' + str(data_luotong.iloc[row,i]) + '\''+ ','
				else: 
				    values = values + str(data_luotong.iloc[row,i]) + ','
			record_id_xisha = random.randint(min_id,max_id)
			values = values + str(record_id_xisha)
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
