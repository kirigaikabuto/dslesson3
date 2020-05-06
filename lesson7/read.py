import json
file_name="main.json"
file = open(file_name,"r")
data = file.read()
users = json.loads(data)
print(len(users))
for i in users:
    print(i['username'],i['password'],i['age'])