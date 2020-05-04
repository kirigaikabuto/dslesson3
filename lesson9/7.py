#1 2 3 4 5 6 
def getAvg(arr):
    sumi=0
    n = len(arr)
    for i in arr:
        sumi = sumi + i
    print(sumi/n)

numbers=[int(i) for i in input().split()]
newnumbers=[-1,0,1,2,3,-4]
getAvg(arr=numbers)
getAvg(arr=newnumbers)