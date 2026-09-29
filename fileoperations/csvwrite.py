import csv
f=open("data.csv","w",newline="")
content=[["name","age"],["fathima",22],["sana",23]]
w=csv.writer(f)
w.writerows(content)
f.close()