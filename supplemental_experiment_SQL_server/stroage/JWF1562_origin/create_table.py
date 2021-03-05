import pyodbc
import pandas as pd
# 连接
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost;'
    r'DATABASE=mashan;'
    r'UID=SA;'
    r'PWD=Wbb123456'
    )

# 获取内容
cursor = conn.cursor()
# cursor.execute("select * from Inventory")
#
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#     print(row.id, row.name)

dbname = 'mashan'
tables = ['xisha1', 'xisha10', 'xisha100', 'xisha1000', 'xisha10000', 'xisha100000']
nums = {'xisha1': 1, 'xisha10': 10, 'xisha100': 100, 'xisha1000': 1000, 'xisha10000': 10000, 'xisha100000': 100000}
data = pd.read_csv('JWF1562.csv')

columns_name = ''
for column in data.columns:
    columns_name = columns_name + column + ','
columns_name = columns_name.strip(',')

values = ''
for table in tables:
    if table == 'xisha100000':
        break
    for num in range(nums[table]):
        values = '\'2019-11-30 11:58:47\','
        for i in range(1, data.shape[1]):
            values = values + str(data.iloc[num, i]) + ','
        values = values.strip(',')
        values = values.replace('nan', '0')

        # SQL 插入语句
        sql = "INSERT INTO {}({}) VALUES ({})".format(table, columns_name, values)

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()

for cur in range(10):
    table == 'xisha100000'
    for num in range(10000):
        values = '\'2019-11-30 11:58:47\','
        for i in range(1, data.shape[1]):
            values = values + str(data.iloc[num, i]) + ','
        values = values.strip(',')
        values = values.replace('nan', '0')

        # SQL 插入语句
        sql = "INSERT INTO {}({}) VALUES ({})".format(table, columns_name, values)

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()

# 关闭数据库连接
conn.close()

