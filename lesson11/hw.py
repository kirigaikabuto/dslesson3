n = int(input())#3
arr=[]
for i in range(n):
    line = input().split(",")
    name = line[0]
    proc = [int(i) for i in line[1].split("/")]
    marks = proc[0]/proc[1]*100
    d={}
    d['name']=name
    d['marks']=marks
    arr.append(d)
for i in arr:
    mark=i["marks"]
    if mark>=50 and mark<60:
            print(i["name"], 'E')
    elif mark>=60 and mark<70:
            print(i["name"], 'D')
    elif mark>=70 and mark<80:
            print(i["name"], 'C')
    elif mark>=80 and mark<90:
            print(i["name"], 'B')
    elif mark>=90 and mark<=100:
            print(i["name"], 'A')

# 3
# yerassyl,3/4
# kirito,20/30
# era,50/60 