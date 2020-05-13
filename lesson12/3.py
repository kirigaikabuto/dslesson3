from myutils import *
arr=[
    {
        "name":"yerassyl1",
        "age":16
    },
    {
        "name":"yerassyl2",
        "age":16
    },
    {
        "name":"yerassyl3",
        "age":16
    }
]
for i in arr:
    name = i['name']#name from arr
    symbol = "e"
    count = count_symbol(name,symbol)
    print(name,symbol,count)
#yerassyl1 e 1
#yerassyl2 e 1
#yerassyl3 e 1
