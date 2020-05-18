import math
n = int(input())#4
points=[]
for i in range(n):
    x,y = input().split()#0 0
    d={}
    d['x'] = int(x)
    d['y'] = int(y)
    points.append(d)
distance=[]
for i in points:
    for j in points:
        part1 = math.pow(i['x']-j['x'],2)
        part2 = math.pow(i['y']-j['y'],2)
        length=math.sqrt(part1+part2)
        if length!=0.0:
            distance.append(length)
print(set(distance))
# 0 0
# 1 1
# 1 0
# 0 1
# #calculcation1 0 0 
# 0 0 -> 0 0
# 0 0 -> 1 1
# 0 0 -> 1 0
# 0 0 -> 0 1
# #calculcation2 1 1 
# 1 1 -> 0 0
# 1 1 -> 1 1
# 1 1 -> 1 0
# 1 1 -> 0 1