arr=[100,2300,20]
sumi=0
n = len(arr)
# range(n)->range(3) -> 0 1 2 -> 0 + 1 +2
for i in range(n):
    sumi = sumi + arr[i]
print(sumi)
sumi = 0
for i in arr:
    sumi = sumi + i
print(sumi)