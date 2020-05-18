arr=[1,2,3,4,-5,6,7,8]
n = len(arr)
neg_index=0
for i in range(n):
    if arr[i]<0:
        neg_index = i
        break
    

numbers=arr[neg_index+1:]
print(numbers)
sumi = 0
for i in arr:
    sumi = sumi+i
print(sumi)