import math
n = int(input())#5
abonents=[]
#get data from keyboard
for i in range(n):
    name = input()#Megahorn
    line = input().split()#0 0 10 -> ['0','0','10']
    d={}
    d['name']=name
    d['x']=int(line[0])
    d['y']=int(line[1])
    d['r']=int(line[2])
    abonents.append(d)
data = input().split()#5 5 ['5','5']
x = int(data[0])
y = int(data[1])
#x1,y1 x2,y2 - > sqrt( (x1-x2)^2+(y1-y2)^2 )
# {
#     "name":
#     "r":
#     "length"
# }
abonents2=[]

for i in abonents:
    d={}
    d['name']=i['name']
    d['r']=i['r']
    part1 = math.pow(x-i['x'],2)
    part2 = math.pow(y-i['y'],2)
    d['length']=math.sqrt(part1+part2)
    abonents2.append(d)
print(n)
all_stations=[]#all station
stations=[]#
for i in abonents2:
    if i['name'] not in all_stations:
        all_stations.append(i['name'])
    if i['length']<=i['r']:
       stations.append(i['name'])

repeating=[]
for i in all_stations:
    counter=0
    for j in stations:
        if i == j:
            counter+=1
    repeating.append(counter)
n  = len(all_stations)
for i in range(n):
    print(all_stations[i],repeating[i])