#1)read data from json
#2)convert json data to python data (loads)
#3)add new element list (append)
#4)write list to json file
import json
#1)
file_name="main.json"
file = open(file_name,"r")
data = file.read()
file.close()
#2)
users = json.loads(data)
element={
    "username":"user3",
    "password":"user3",
    "age":33
}
#3)
users.append(element)
#4)
file = open(file_name,"w")
json_users = json.dumps(users,indent=4)
file.write(json_users)
file.close()