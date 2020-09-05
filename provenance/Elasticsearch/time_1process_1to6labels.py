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

outfile = "1p_f1t6id.txt"
xisha_table = 'JWF1562_xisha'
cusha_table = 'JWF1418_cusha'
base_table= 'x2c'

sql = "select min(record_id),max(record_id) from {}".format(xisha_table)
cursor.execute(sql)
db.commit()
result = cursor.fetchone()
min_id = result[0]
max_id = result[1]
print(min_id,max_id)

# 选择10个要进行追溯的细纱数据
nums = 10
xisha_ids = []
for num in range(nums):
    xisha_ids.append(random.randint(min_id, max_id)) 

print(xisha_ids)

with open(outfile, 'a') as f:
    f.write('{}\n'.format('#'*70))
    f.write('# datetime:{}\n'.format(datetime.datetime.now()))
    f.write('# the process from xisha to cusha.\n')
    f.write('{}\n'.format('#'*70))

################################
for id_num in range(1,6+1):
    with open(outfile, 'a') as f:
        f.write('{} Start with {} ids in one sample data {}\n'.format('*'*15,id_num,'*'*15))
    total_time = []
    for xisha_id in xisha_ids:
        times = []
        for num in range(nums):
            start = time.process_time()
            # 拿到相应的细纱数据
            result = es.search(
                    index="x2c{}".format(id_num),
                    body={
                        "query": {"match": {
                            "_id": "{}".format(xisha_id)
                            }}
                        }
                    )
            result = result['hits']['hits'][0]['_source']
            if num == 0:
                with open(outfile, 'a') as f:
                    f.write('要追溯的细纱数据：\n')
                    f.write(str(result)+'\n')

            # 与细纱数据相关联的粗纱数据id
            results = result['before_record_id'] 
   
            # 拿到粗纱数据
            for result in results:
                cusha_data = es.search(
                        index="x2c{}".format(id_num),
                        body={
                            "query": {"match": {
                                "_id": "{}".format(xisha_id)
                                }}
                            }
                        )
                cusha_data = cusha_data['hits']['hits'][0]['_source']
                if num ==0:
                    with open(outfile, 'a') as f:
                        f.write('被追溯的粗纱数据：')
                        f.write(str(cusha_data)+'\n')
                       
            end = time.process_time()
            times.append(end-start)
        mean_time = sum(times)/nums
        total_time.append(mean_time)
        # 该过程进行10次。
        with open(outfile, 'a') as f:
            f.write('* xisha_id={}:{},mean_time:{}\n'.format(xisha_id, times, mean_time))
    # 共10个数据，每个10次追溯，将耗时平均作为该过程追溯的平均耗时。
    with open(outfile, 'a') as f:
        f.write('{} End {}\n'.format('*'*35,'*'*35))
        f.write('* {} with ids of {}:{},mean_time:{}\n'.format(base_table,id_num,total_time,sum(total_time)/len(xisha_ids)))


