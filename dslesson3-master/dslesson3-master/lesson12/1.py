from myutils import *
arr=[1,2,3,4,5]
find=100
otvet = ifexists(arr,find)
if otvet == 1:
    print("we find this number")
else:
    print("Not found")