users=[
    {
        "id":1,
        "name":"yerassyl",
    },
     {
        "id":2,
        "name":"kirito",
    }
]

def remove_element(id=0,name=""):
    n = len(users)
    if name!="" and id!=0:
        remove_index=-1
        for i in range(n):
            if users[i]['name']==name and users[i]['id']==id:
                remove_index=i
                break
        if remove_index!=-1:
            users.pop(remove_index)
    elif name!="":
        remove_index=-1
        for i in range(n):
            if users[i]['name']==name:
                remove_index=i
                break
        if remove_index!=-1:
            users.pop(remove_index)
    elif id!=0:
        remove_index=-1
        for i in range(n):
            if users[i]['id']==id:
                remove_index=i
                break
        if remove_index!=-1:
            users.pop(remove_index)
    else:
        print("default values")

for i in users:
    print(i)
print("after delete")
remove_element(name="yerassyl",id=2)
for i in users:
    print(i)