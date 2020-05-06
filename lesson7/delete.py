import json
#1)
file_name="main.json"
file = open(file_name,"r")
data = file.read()
file.close()
#2)
users = json.loads(data)
#3)delete element
username = "user2"
delete_index=0
for i in range(len(users)):
    if users[i]['username']==username:
        delete_index=i
        break
users.pop(delete_index)
#4)
file = open(file_name,"w")
json_users = json.dumps(users,indent=4)
file.write(json_users)
file.close()