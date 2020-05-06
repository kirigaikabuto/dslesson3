# #main.py
# -id
# -name
# -price
# {
# 1 
# "product1",
# 100,
# },
# {
#     2
#     "product2",
#     200
# }
import json
file = open("main.json","r")
data =file.read()
users = json.loads(data)
sumi=0
for i in users:
    sumi = sumi + i['age']
n = len(users)
print(sumi/n)