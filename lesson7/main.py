import json
#import name_of_library
users=[
    {
        "username":"user1",
        "password":"user1",
        "age":22
    },
    {
        "username":"user2",
        "password":"user2",
        "age":30
    },
]
file_name="main.json"
file = open(file_name,"w")
json_users = json.dumps(users,indent=4)
file.write(json_users)
file.close()