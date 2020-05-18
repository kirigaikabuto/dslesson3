from myutils import *

arr=[
    {
        "name":"yerassyl",
        "year":1998
    },
    {
         "name":"yerassyl",
        "year":2000
    },
    {
         "name":"yerassyl",
        "year":2006
    },
]
ages=list(map(find_real_age,arr))

for i in arr:
    some_find(i,"price")
print(ages)
# ages=[]
# for i in arr:
#     real_age = find_real_age1(i['year'])
#     ages.append(real_age)
# print(ages)
# printarr(arr)
# maxi123 = find_max(arr)
# print(maxi123+1)