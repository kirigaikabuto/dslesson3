#find min
n = int(input())
arr=[]
for i in range(n):
    num = int(input())
    arr.append(num)
mini=arr[0]
for i in range(n):
    if arr[i] < mini:
        mini = arr[i]
print(f"Min={mini}")