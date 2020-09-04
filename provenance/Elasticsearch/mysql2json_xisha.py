import pandas as pd
import json
import numpy as np
import pymysql
import decimal
import os

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

table = 'JWF1562_xisha'

columns_name = []
sql = "desc {}".format(table)
cursor.execute(sql)
db.commit()
results = cursor.fetchall()
for result in results: 
    columns_name.append(result[0])
columns_name.append('before_record_id')
print(columns_name)

sql = "select * from {}".format(table)
cursor.execute(sql)
db.commit()
results = cursor.fetchall()

tables_join = ['x2c1','x2c2','x2c3','x2c4','x2c5','x2c6']

for table_join in tables_join:
	for result,num in zip(results,range(len(results))): 
		row = []
		for i in result:
		    if type(i) is decimal.Decimal:
		        row.append(float(i))
		    else:
		        row.append(i)
		#print(row)
		
		values = []
		sql = "select record_id_cusha from {} where record_id_xisha = {}".format(table_join, result[0])
		cursor.execute(sql)
		db.commit()
		before_record_ids = cursor.fetchall()
		for before_record_id in before_record_ids:
                    values.append(before_record_id[0])
	
		row.append(values)
		row = dict(zip(columns_name[1:], row[1:]))
		row['record_timestamp'] = str(row['record_timestamp'])
		        
		record_id = {"index": {"_id": str(result[0])}}
		with open(table_join+'.json', "a") as f:
		    json.dump(record_id, f, cls=NpEncoder)
		    f.write('\n')
		    json.dump(row, f, cls=NpEncoder)
		    f.write('\n')
		print(num)

for table_join in tables_join:
	os.system("curl -H \"Content-Type: application/json\" -XPOST \"localhost:9200/{}/_bulk?pretty&refresh\" --data-binary \"@{}\" ".format(table_join, table_join+'.json'))
