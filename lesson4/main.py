# 5
# 1
# -1
# -3
# 3
# 4
n = int(input())
arr=[]
for i in range(n):
    num = int(input())
    arr.append(num)
maxi=arr[0]
for i in arr:
    if i > maxi:
        maxi = i
print(f"Maxi={maxi}")
#1 i = 1 maxi =1 
#  if 1>1:
#     maxi =1
# #2 i = -1 maxi =1
#   if -1 > 1:
#       maxi = -1
# #3 i = -3 maxi =1
# #4 i =3 maxi =1
#  if 3>1:
#      maxi=3 
# #5 i = 4 maxi = 3
#    if 4>4:
#        maxi = 4
