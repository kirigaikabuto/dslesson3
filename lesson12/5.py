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
find_key="name"
find_value="yerassyl2"
update_key="age"
update_value=18
arr = set_data_to_dict(arr,find_key,find_value,update_key,update_value)
for i in arr:
    print(i)
# def set_data_to_dict(arr,find_key,find_value,update_key,update_value):
#     #code 
#     return arr
