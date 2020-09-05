import time
import datetime
import pymysql
import random
from elasticsearch import Elasticsearch

# 打开数据库连接
db = pymysql.connect("localhost","root","","mashan" )
es = Elasticsearch(['localhost:9200'])
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

outfile ="4p_f1t6id.txt"
later_tables = ['SMARO_E_luotong', 'JWF1562_xisha', 'JWF1418_cusha', 'JWF1312B_bingtiao']
before_tables = ['JWF1562_xisha', 'JWF1418_cusha', 'JWF1312B_bingtiao', 'JWF1211_shumuan']
record_id_name = ['luotong', 'xisha', 'cusha', 'bingtiao', 'shumian']
base_tables = ['l2x', 'x2c', 'c2b', 'b2s', 'humua']

sql = "select min(record_id),max(record_id) from {}".format(later_tables[0])
cursor.execute(sql)
db.commit()
result = cursor.fetchone()
min_id = result[0]
max_id = result[1]
print(min_id,max_id)

# 选择10个要进行追溯的络筒数据
nums = 10
later_idss = []
for num in range(nums):
    later_idss.append(random.randint(min_id, max_id))

print(later_idss)

with open(outfile, 'a') as f:
    f.write('{}\n'.format('#'*70))
    f.write('# datetime:{}\n'.format(datetime.datetime.now()))
    f.write('# the process from luotong to shumian.\n')
    f.write('{}\n'.format('#'*70))

################################
def provenance(later_ids,table_num):
    if table_num >= len(base_tables)-1:
        return 1
    total_time = []
    for later_id in later_ids:
        start = time.process_time()
        
        # 拿到相应的后到工序数据
        result = es.search(
                index="{}{}".format(base_tables[table_num], id_num),
                body={
                    "query": {"match": {
                        "_id": "{}".format(later_id)
                        }}
                    }
                )
        result = result['hits']['hits'][0]['_source']
        
        with open(outfile, 'a') as f:
            f.write('要追溯的数据：\n')
            f.write(str(result)+'\n')	
                
        # 与后道数据相关联的前道工序数据id
        results = result['before_record_id']
        
        # 拿到与后道数据相关联的前道工序数据
        later_id_before_ids = []
        for result in results:
            later_id_before_ids.append(result)
            if table_num == len(base_tables)-2:
                before_data = es.search(
                        index="{}".format(base_tables[table_num+1]),
                        body={
                            "query": {"match": {
                                "_id": "{}".format(result)
                                }}
                            }
                        )
            else:
                before_data = es.search(
                        index="{}{}".format(base_tables[table_num+1], id_num),
                        body={
                            "query": {"match": {
                                "_id": "{}".format(result)
                                }}
                            }
                        )
            before_data = before_data['hits']['hits'][0]['_source']
            
            with open(outfile, 'a') as f:
                f.write('被追溯的数据：')
                f.write(str(before_data)+'\n')
            
        provenance(later_ids = later_id_before_ids, table_num=table_num+1)
        
        end = time.process_time()
        total_time.append(end - start)
            
    # 共10个数据，每个10次追溯，将耗时平均作为该过程追溯的平均耗时
    with open(outfile, 'a') as f:
        f.write('{} End {}\n'.format('*'*35,'*'*35))
        f.write('* {} with ids of {}:{},mean_time:{}\n'.format(base_tables[table_num], id_num, total_time, sum(total_time) / len(later_ids)))
        
for id_num in range(1,6+1):
    with open(outfile, 'a') as f:
        f.write('{} Start with {} ids in one sample data {}\n'.format('*'*15,id_num,'*'*15))
        total_num = len(base_tables)-1
    provenance(later_ids = later_idss,table_num=0)
