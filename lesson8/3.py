n = int(input())
products=[]
for i in range(n):
    line = input()
    id,name,price = line.split(" ")
    d={}
    d['id']=int(id)
    d['name']=name
    d['price']=int(price)
    products.append(d)
for i in products:
    print(i)

# {
#     "id":1,
#     "name":"jsjsj",
#     "price":1000
# }
# INPUT
# 3
# 1 jsjsj 1000
# 2 product2 100
# 3 product3 200

# OUT
# [
#     {
#        "id":1,
#         "name":"jsjsj",
#         "price":1000  
#     },
#       {
#        "id":2,
#         "name":"product2",
#         "price":100  
#     },
#       {
#        "id":1,
#         "name":"product3",
#         "price":200  
#     },
# ]