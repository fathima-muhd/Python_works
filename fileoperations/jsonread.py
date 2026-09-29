import json
f=open("data.json","r")
content=json.load(f)
print(content[0]['name'])
f.close()