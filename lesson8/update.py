import json
#1)
file_name="main.json"
file = open(file_name,"r")
data = file.read()
file.close()
#2)
users = json.loads(data)
#3)update
condition_key="username"
condition_value="user1"
key = "age"
value = 100
for i in range(len(users)):
    if users[i][condition_key] == condition_value:
        users[i][key]=value
        break
#4)
file = open(file_name,"w")
json_users = json.dumps(users,indent=4)
file.write(json_users)
file.close()