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

tables = ['JWF1211_shumuan']
jsonfile = 'shumuan.json'

columns_name = []
sql = "desc JWF1211_shumuan"
cursor.execute(sql)
db.commit()
results = cursor.fetchall()
for result in results: 
    columns_name.append(result[0])
# print(columns_name)

for table in tables:
    sql = "select * from JWF1211_shumuan"
    cursor.execute(sql)
    db.commit()
    results = cursor.fetchall()

    for result,num in zip(results,range(len(results))): 
        row = []
        for i in result:
            if type(i) is decimal.Decimal:
                row.append(float(i))
            else:
                row.append(i)
        #print(row)
        
        row = dict(zip(columns_name[1:], row[1:]))
        row['record_timestamp'] = str(row['record_timestamp'])
                
        record_id = {"index": {"_id": str(result[0])}}
        with open(jsonfile, "w") as f:
            json.dump(record_id, f, cls=NpEncoder)
            f.write('\n')
            json.dump(row, f, cls=NpEncoder)
            f.write('\n')
        os.system("curl -H \"Content-Type: application/json\" -XPOST \"localhost:9200/{}/_bulk?pretty&refresh\" --data-binary \"@{}\" ".format(jsonfile.strip('.json'), jsonfile))
        print(num)
