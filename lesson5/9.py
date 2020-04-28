# INPUT:
# 4
# fruit-banana
# person-yerassyl
# car-bmw
# home-iitu
n = int(input())
d={}
for i in range(n):
   
    word = input().split("-")
     #[fruit,banana]
    d[word[0]]=word[1]
    # d['fruit']='banana'
print(d)
# [
#     [
#         banana,yerassyl,bmw,bmw
#     ]
# ]
# OUT:
# {
#     "fruit":"banana",
#     "person":"yerassyl",
#     "car":"bmw",
#     "home":"iitu"
# }