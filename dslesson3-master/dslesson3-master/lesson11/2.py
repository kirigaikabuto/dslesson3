n=int(input())
arr=[]
for i in range(n):
    line=input().split(',')
    product_id=line[0]
    product_name=line[1]
    prices=[int(i) for i in line[2].split(' ')]
    request=line[3]
    d={}
    d['product_id']=product_id
    d['product_name']=product_name
    d['prices']=prices
    d['request']=request
    arr.append(d)

for i in arr:
    if i['request'] =="max":
        #code
    else if i['request']=="min":
        #code
    else:
        prices=i['prices']
        sumi=0
        n_prices=len(prices)
        for j in prices:
            sumi+=j
        avg=sumi/n_prices
        i['avg']=avg 

for i in arr:
    print(i)