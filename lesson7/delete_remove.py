import json
#1)
file_name="main.json"
file = open(file_name,"r")
data = file.read()
file.close()
#2)
users = json.loads(data)
#3)delete element
username = "user1"
delete_element={}
for i in users:
    if i['username']==username:
        delete_element=i
users.remove(delete_element)
#4)
file = open(file_name,"w")
json_users = json.dumps(users,indent=4)
file.write(json_users)
file.close()