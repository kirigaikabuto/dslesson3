n = int(input())#7
numbers=[int(i) for i in input().split()]#1 1 5 3 1 5 1
#[1,1,5,3,1,5,1]
m = int(input())
replace=[]
for i in range(m):
    a,b = input().split()#5 1
    d={}
    d['before']=int(a)#5
    d['after']=int(b)#1
    replace.append(d)
memory=[]
for i in replace:
    for j in range(n):
        if i['before']==numbers[j] and j not in memory:
            numbers[j]=i['after']
            memory.append(j)
print(numbers)
# 1 1 5 3 1 5 1
# 5 1 
# 1 1 1 3 1 1 1
# 1 3
# 3 3 3 3 3 3 3