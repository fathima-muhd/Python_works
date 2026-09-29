f=open("data.json","w")
import json
content=[{"name":"Fathima","age":22},{"name":"Fasila","age":23}]
json.dump(content,f)
f.close()