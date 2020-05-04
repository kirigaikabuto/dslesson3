import json
file = open("products.json","r")
data = file.read()
users = json.loads(data)
file.close()
print("[1]добавление")
print("[2]удалить")
num = input()
n = len(users)
if num == "1":
    name = input("введите название продукта:")
    price = int(input("введите цену продукта:"))
    user={}
    user['product_name']=name
    user['product_price']=price
    user['product_id']=1
    if n>0:
        last_user=users[n-1]
        user['product_id']=last_user['product_id']+1
    users.append(user)
    
elif num == "2":
    print("--Удалить--")
    for i in users:
        print(i['product_id'],i['product_name'],i['product_price'])
    id = int(input("Введите id:"))
    remove_index=-1
    for i in range(n):
        if users[i]['product_id']==id:
            remove_index=i
    if remove_index==-1:
        print("Not found")
    else:
        users.pop(remove_index)


file_write = open("products.json","w")
json_array = json.dumps(users,indent=4)
file_write.write(json_array)
file_write.close()