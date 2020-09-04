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

table = 'JWF1312B_bingtiao'

columns_name = ''
for column in data_bingtiao.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name.strip(',')

for row in range(data_bingtiao.shape[0]):
	values = ''
	for i in range(data_bingtiao.shape[1]):
		if i == 1:
		    values = values + '\'' + str(data_bingtiao.iloc[row,i]) + '\''+ ','
		else: 
		    values = values + str(data_bingtiao.iloc[row,i]) + ','
	values = values.strip(',')
	values = values.replace('nan','0')

	print(table + '-' + str(row))
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

data_cusha = pd.read_csv('../data/JWF1418_cusha.csv')
a = data_cusha['record_timestamp']
b = pd.to_datetime(a)
print(min(b))
print(max(b))
data_cusha['record_timestamp'] = b
data_cusha = data_cusha[data_cusha['record_timestamp']>pd.to_datetime('2018-06-30')]
data_cusha = data_cusha[data_cusha['record_timestamp']<pd.to_datetime('2019-03-30')]
data_cusha = data_cusha.sort_values('record_timestamp')

# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

table = 'JWF1418_cusha'

columns_name = ''
for column in data_cusha.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name.strip(',')

for row in range(data_cusha.shape[0]):
	values = ''
	for i in range(data_cusha.shape[1]):
		if i == 1:
		    values = values + '\'' + str(data_cusha.iloc[row,i]) + '\''+ ','
		else: 
		    values = values + str(data_cusha.iloc[row,i]) + ','
	values = values.strip(',')
	values = values.replace('nan','0')

	print(table + '-' + str(row))
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

data_xisha = pd.read_csv('../data/JWF1562_xisha.csv')
a = data_xisha['record_timestamp']
b = pd.to_datetime(a)
print(min(b))
print(max(b))
data_xisha['record_timestamp'] = b
data_xisha = data_xisha[data_xisha['record_timestamp']>pd.to_datetime('2018-06-30')]
data_xisha = data_xisha[data_xisha['record_timestamp']<pd.to_datetime('2019-03-30')]
data_xisha = data_xisha.sort_values('record_timestamp')

# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

table = 'JWF1562_xisha'

columns_name = ''
for column in data_xisha.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name.strip(',')

for row in range(data_xisha.shape[0]):
	values = ''
	for i in range(data_xisha.shape[1]):
		if i == 0:
		    values = values + '\'' + str(data_xisha.iloc[row,i]) + '\''+ ','
		else: 
		    values = values + str(data_xisha.iloc[row,i]) + ','
	values = values.strip(',')
	values = values.replace('nan','0')

	print(table + '-' + str(row))
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

table = 'SMARO_E_luotong'

columns_name = ''
for column in data_luotong.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name.strip(',')

for row in range(data_luotong.shape[0]):
	values = ''
	for i in range(data_luotong.shape[1]):
		if i == 0:
		    values = values + '\'' + str(data_luotong.iloc[row,i]) + '\''+ ','
		else: 
		    values = values + str(data_luotong.iloc[row,i]) + ','
	values = values.strip(',')
	values = values.replace('nan','0')

	print(table + '-' + str(row))
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
