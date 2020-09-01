import os

jsonfiles = ['xishalabel1.json','xishalabel2.json','xishalabel3.json','xishalabel4.json','xishalabel5.json','xishalabel6.json','xishalabel7.json','xishalabel8.json','xishalabel9.json','xishalabel10.json','xishalabel11.json','xishalabel12.json']
for jsonfile in jsonfiles:
    os.system("curl -H \"Content-Type: application/json\" -XPOST \"localhost:9200/{}/_bulk?pretty&refresh\" --data-binary \"@{}\" ".format(jsonfile.strip('.json'), jsonfile))
