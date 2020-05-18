# 3
# Yerassyl 22
# Anel 20
# Zhina 22
n = int(input())#3
arr=[]
for i in range(n):
    line = input().split()#['yerassyl', '22']
    name = line[0]
    age = int(line[1])
    d={}
    d['name']=name
    d['age']=age
    arr.append(d)
    # d={
    #     "name":name,
    #     "age":age
    # }
for i in arr:
    print(i)
tmp = arr[0]
arr[0]=arr[2]
arr[2]=tmp
print()
for i in arr:
    print(i)


# for i in arr:
#     if i['age']>21:
#         print(i['name'])

# [
#     {
#         "name":"yerassyl",
#         "age":22
#     },
#     {
#         "name":"yerassyl",
#         "age":22
#     },
#     {
#         "name":"yerassyl",
#         "age":22
#     }
# ]