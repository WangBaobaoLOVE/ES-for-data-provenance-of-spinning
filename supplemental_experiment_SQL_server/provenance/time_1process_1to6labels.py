import time
import datetime
import random
import pyodbc

# 连接
db = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost;'
    r'DATABASE=mashan;'
    r'UID=SA;'
    r'PWD=Wbb123456'
    )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

outfile = "1p_f1t6id.txt"
xisha_table = 'JWF1562_xisha'
cusha_table = 'JWF1418_cusha'
base_table= 'x2tc'

sql = "select min(record_id),max(record_id) from {}".format(xisha_table)
cursor.execute(sql)
# db.commit()
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
            sql = "select * from {} where record_id = {}".format(xisha_table, xisha_id)
            cursor.execute(sql)
            # db.commit()
            result = cursor.fetchone()
            if num == 0:
                with open(outfile, 'a') as f:
                    f.write('要追溯的细纱数据：\n')
                    f.write(str(result)+'\n')

            # 与细纱数据相关联的粗纱数据id
            sql = "select record_id_cusha from {}{} where record_id_xisha = {}".format(base_table, id_num, xisha_id)
            print(sql)
            cursor.execute(sql)
            # db.commit()
            results = cursor.fetchall()
   
            # 拿到粗纱数据
            for result in results:
                sql = "select * from {} where record_id = {}".format(cusha_table, result[0])
                cursor.execute(sql)
                # db.commit()
                cusha_data = cursor.fetchone()
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


