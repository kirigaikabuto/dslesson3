from myutils import *
arr=[
    {
        "name":"yerassyl1",
        "age":16,
        "marks":[1,2,3,4,5]
    },
    {
        "name":"yerassyl2",
        "age":16,
        "marks":[1,2,3,4,5]
    },
    {
        "name":"yerassyl3",
        "age":16,
        "marks":[1,2,3,4,5]
    }
]
#code
for i in arr:
    marks = i['marks']
    maxi = find_max(marks)
    print(i['name'],marks)
#yerassyl1 5
#yerassyl2 5
#yerassyl3 5