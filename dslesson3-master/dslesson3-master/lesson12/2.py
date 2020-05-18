
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
find_key="name"
find_value="yerassyl1"
is_find = ifexists2(arr,find_key,find_value)
if is_find == 1:
    print("Ok")
else:
    print("error")