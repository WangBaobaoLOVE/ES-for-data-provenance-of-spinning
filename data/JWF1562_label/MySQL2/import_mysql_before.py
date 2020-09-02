import pymysql
import pandas as pd
 
# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

table = 'cusha'
data = pd.read_csv('./JWF1418.csv')

columns_name = 'record_id,'
for column in data.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name.strip(',')


for cpnum in range(12):
    values = '{},'.format(501+cpnum)
    for i in range(data.shape[1]):
        if i == 1:
            values = values + '\''+ str(data.iloc[cpnum,i]) + '\''+ ','
        else:
            values = values + str(data.iloc[cpnum,i]) + ','
    values = values.strip(',')
    values = values.replace('nan','0')

    print(table+'-'+str(cpnum))
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

