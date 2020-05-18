#yerassyl
s = "hello yerassyl"
print(s)
arr=list(s)
print(arr)
for i in range(len(arr)):
    if arr[i] == "a":
        arr[i]="0"
print(arr)
to_st = "".join(arr)
print(to_st)