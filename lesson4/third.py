n = int(input())
arr=[]
for i in range(n):
    num = int(input())
    arr.append(num)
#find max
maxi=arr[0]
maxi_index=0
for i in range(n):
    if arr[i] > maxi:
        maxi = arr[i]
        maxi_index=i
#find min
mini=arr[0]
mini_index=0
for i in range(n):
    if arr[i] < mini:
        mini = arr[i]
        mini_index=i
print(f"Maxi = {maxi} and index={maxi_index}")
print(f"Mini = {mini} and index={mini_index}")
print(arr)
tmp = arr[maxi_index]
arr[maxi_index]=arr[mini_index]
arr[mini_index]=tmp
print(arr)