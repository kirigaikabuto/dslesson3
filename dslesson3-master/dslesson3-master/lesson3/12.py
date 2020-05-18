n = int(input())
arr=[]
#помещаем элементы в массив
for i in range(n):
    num = int(input())
    arr.append(num)
#
sumi =0
for i in range(n):
    if arr[i]>0 and arr[i]%2==0:
        sumi = sumi + arr[i]
print(sumi)


# 6
# -1
# 2
# 4
# 5
# -4
# 8
#сумму четных положительных элементов