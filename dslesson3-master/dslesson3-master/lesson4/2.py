n = int(input())
#генараторы
arr = [i for i in range(n) if i%2==0]
# arr=[i*2 for i in range(1,n+1)]
# arr=[]
# for i in range(1,n+1):
#     arr.append(i)

print(arr)