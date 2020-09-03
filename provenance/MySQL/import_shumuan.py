import pandas as pd
import pymysql

data_shumian = pd.read_csv('../data/JWF1211_shumian.csv')
a = data_shumian['record_timestamp']
b = pd.to_datetime(a)
print(min(b))
print(max(b))
data_shumian['record_timestamp'] = b
data_shumian = data_shumian[data_shumian['record_timestamp']>pd.to_datetime('2018-06-30')]
data_shumian = data_shumian[data_shumian['record_timestamp']<pd.to_datetime('2019-03-30')]
data_shumian = data_shumian.sort_values('record_timestamp')

# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

table = 'JWF1211_shumuan'

columns_name = ''
for column in data_shumian.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name.strip(',')

for row in range(data_shumian.shape[0]):
    print(row)
    values = ''
    for i in range(data_shumian.shape[1]):
        if i == 1:
            values = values + '\'' + str(data_shumian.iloc[row,i]) + '\''+ ','
        else: 
            values = values + str(data_shumian.iloc[row,i]) + ','
    values = values.strip(',')
    values = values.replace('nan','0')

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
