# 3
# yerassyl,4 5 3 4 2
# kirito,3 4 5
# anel,4 5 3 2 4 3 4
# 2
# zhina,2 5 5
# zhina2,1 1 1
n = int(input())#3
arr=[]
for i in range(n):
    line = input().split(",")#yerassyl,4 5 3 4 2 - > ["yerassyl","4 5 3 4 2"]
    name = line[0]#"yerassyl"
    marks = [int(i) for i in line[1].split(" ")]#int(i) for i in ["4","5","3","4","2"]
    d={}
    d['name']=name
    d['marks']=marks
    arr.append(d)
    
#calculate avg
for i in arr:
    name = i['name']
    marks = i['marks']
    sumi=0
    n_marks = len(marks)
    for j in marks:
        sumi = sumi + j
    avg = sumi/n_marks
    i['avg']=avg
    #end
    
#find max min
maxi_avg=arr[0]['avg']
mini_avg=arr[0]['avg']
for i in arr:
    if maxi_avg<i['avg']:
        maxi_avg = i['avg']
    if mini_avg>i['avg']:
        mini_avg = i['avg']

#add new element
m = int(input())
newelements=[]
for i in range(m):
    line = input().split(",")
    name = line[0]
    marks = [int(i) for i in line[1].split(" ")]
    d={}
    d['name']=name
    d['marks']=marks
    newelements.append(d)
for i in newelements:
    name = i['name']
    marks = i['marks']
    sumi=0
    n_marks = len(marks)
    for j in marks:
        sumi = sumi + j
    avg = sumi/n_marks
    i['avg']=avg
for i in newelements:
    if i['avg']>=mini_avg and i['avg']<=maxi_avg:
        print(i['name'],"YES")
    else:
        print(i['name'],"NO")
#yerassyl 3.6
# kirito 4.0
# anel 3.5714285714285716
# arr=[
#     {
#         "name":"",
#         "marks":[1,2,3,4,5],
 #         "avg":3.6
#     },
#      {
#         "name":"",
#         "marks":[1,2,3,4,5]
#         "avg":3.6
#     },
#      {
#         "name":"",
#         "marks":[1,2,3,4,5]
#         "avg":3.6
#     },
# {
#     "avg":3.6
# }
# ]
    