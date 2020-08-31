import os
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

filedir = '../CSV/'
csvfile = 'xisha100000.csv'

originfile = '../MySQL/JWF1562.csv'
columns_name = ['record_id']
origindata = pd.read_csv(originfile)

for column_name in origindata.columns:
    columns_name.append(column_name)

data  = pd.read_csv(filedir+csvfile, names=columns_name)
    
for row in range(data.shape[0]):
    record_id = {"index": {"_id": str(data.iloc[row]['record_id'])}}
    with open(csvfile.strip('.csv')+'.json', "w") as f:
        json.dump(record_id, f, cls=NpEncoder)
        f.write('\n')
        json.dump(dict(data.iloc[row,1:]), f, cls=NpEncoder)
        f.write('\n')
    os.system("curl -H \"Content-Type: application/json\" -XPOST \"localhost:9200/{}/_bulk?pretty&refresh\" --data-binary \"@{}\" ".format('xisha100000', 'xisha100000.json'))
