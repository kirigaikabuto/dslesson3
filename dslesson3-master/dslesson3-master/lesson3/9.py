arr=[100,-2,123,344,55,600]
n = len(arr)
print(arr)
# for i in range(n):
#     if arr[i]%2==0:
#         arr[i]=1
for i in range(0,n,2):
    arr[i]=1
print(arr)