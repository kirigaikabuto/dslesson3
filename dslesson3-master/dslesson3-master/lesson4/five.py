arr=[0,2,-1,3,4,5,6,8]
n = len(arr)
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
start=maxi_index
end=mini_index
if maxi_index>mini_index:
    start=mini_index
    end=maxi_index

numbers=arr[start+1:end]
sumi=0
for i in numbers:
    sumi = sumi +i
print(arr)
print(numbers)
print(sumi)