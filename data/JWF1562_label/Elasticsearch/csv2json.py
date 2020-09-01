import pandas as pd
import json
import numpy as np

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

filedir = '../../JWF1562_origin/CSV/'
csvfile = 'xisha10000.csv'
jsonfiles = ['xishalabel1.json','xishalabel2.json','xishalabel3.json','xishalabel4.json','xishalabel5.json','xishalabel6.json','xishalabel7.json','xishalabel8.json','xishalabel9.json','xishalabel10.json','xishalabel11.json','xishalabel12.json']
label_nums = {'xishalabel1.json':1,'xishalabel2.json':2,'xishalabel3.json':3,'xishalabel4.json':4,'xishalabel5.json':5,'xishalabel6.json':6,'xishalabel7.json':7,'xishalabel8.json':8,'xishalabel9.json':9,'xishalabel10.json':10,'xishalabel11.json':11,'xishalabel12.json':12}
originfile = '../../JWF1562_origin/MySQL/JWF1562.csv'
columns_name = ['record_id']
origindata = pd.read_csv(originfile)

for column_name in origindata.columns:
    columns_name.append(column_name)

data  = pd.read_csv(filedir+csvfile, names=columns_name)
  
for jsonfile in jsonfiles: 
    label_num = label_nums[jsonfile]
    for row in range(data.shape[0]):
        record_id = {"index": {"_id": str(data.iloc[row]['record_id'])}}
        with open(jsonfile, "a") as f:
            json.dump(record_id, f, cls=NpEncoder)
            f.write('\n')
            rowdata = dict(data.iloc[row,1:])
            rowdata['before_record_id'] = [500]*label_num
            json.dump(rowdata, f, cls=NpEncoder)
            f.write('\n')
