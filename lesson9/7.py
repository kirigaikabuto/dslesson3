n = int(input())
students=[]
for i in range(n):
    line = input().split(",")#["1","yerasyl","1 2 3 4 5"]
    d={}
    d['id']=int(line[0])
    d['name']=line[1]
    d['marks']=[int(i) for i in line[2].split()]
    students.append(d)
for i in students:
    sumi=0
    n = len(i['marks'])
    for mark in i['marks']:
        sumi = sumi + mark
    print(i['name'],sumi/n)
