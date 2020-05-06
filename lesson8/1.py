import json
file = open("users.json","r")
data = file.read()
users = json.loads(data)
file.close()
print("[1]добавление")
print("[2]удалить")
print("[3]обновить")
num = input()
n = len(users)
if num == "1":
    name = input("введите ваше имя:")
    user={}
    user['name']=name
    user['id']=1
    if n>0:
        last_user=users[n-1]
        user['id']=last_user['id']+1
    users.append(user)
    
elif num == "2":
    print("--Удалить--")
    for i in users:
        print(i['id'],i['name'])
    id = int(input("Введите id:"))
    remove_index=-1
    for i in range(n):
        if users[i]['id']==id:
            remove_index=i
    if remove_index==-1:
        print("Not found")
    else:
        users.pop(remove_index)
elif num == "3":
    print("--Обновить--")
    for i in users:
            print(i['id'],i['name'])
    id = int(input("Введите id:"))
    update_index=-1
    for i in range(n):
        if users[i]['id']==id:
            update_index=i
    if update_index==-1:
        print("Not found")
    else:
        newname=input("New Name:")
        users[update_index]['name']=newname


file_write = open("users.json","w")
json_array = json.dumps(users,indent=4)
file_write.write(json_array)
file_write.close()