import os

jsonfiles = ['xisha1.json','xisha10.json','xisha100.json','xisha1000.json','xisha10000.json']

for jsonfile in jsonfiles:
    os.system("curl -H \"Content-Type: application/json\" -XPOST \"localhost:9200/{}/_bulk?pretty&refresh\" --data-binary \"@{}\" ".format(jsonfile.strip('.json')+'2', jsonfile))
