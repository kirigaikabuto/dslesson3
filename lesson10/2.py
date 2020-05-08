# 3
# yerassyl,4 5 3 4 2
# kirito,3 4 5
# anel,4 5 3 2 4 3 4
# 1
# zhina,2 5 5 
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


for i in arr:
    name = i['name']
    marks = i['marks']
    sumi=0
    n_marks = len(marks)
    for j in marks:
        sumi = sumi + j
    avg = sumi/n_marks
    print(name,avg)
#find max min
for i in 
#yerassyl 3.6
# kirito 4.0
# anel 3.5714285714285716
# arr=[
#     {
#         "name":"",
#         "marks":[1,2,3,4,5]
#     },
#      {
#         "name":"",
#         "marks":[1,2,3,4,5]
#     },
#      {
#         "name":"",
#         "marks":[1,2,3,4,5]
#     },
# ]
    