n=int(input('product number--> '))
data=[]
for i in range(n):
    entry=input('id, name, values, type-> ').split(",")
    dic={}
    dic['id']=entry[0]
    dic['name']=entry[1]
    dic['type']=entry[3]
    prices=[int(i) for i in entry[2].split()]
    dic['prices']=prices
    data.append(dic)
# for i in data:
#     print(i)


maxi=data[0]['prices'][0]
mini=data[0]['prices'][0]

for i in data:
    tmp=i['prices']
    sumi=0
    avgi=0
  
    for j in tmp:
        sumi=sumi+j
    avgi=sumi/int(len(tmp))
    
    for j in tmp:
        if maxi < j:
            maxi = j
    
    for j in tmp:
        if mini > j:
            mini = j

    if i['type'] == "avg":
        print(i['name'],"selected for avg")
        i['settledPrice']=avgi

        
    if i['type'] == "max":
        print(i['name'],"selected for max")
        i['settledPrice']=maxi
    
    if i['type'] == "min":
        print(i['name'],"selected for min")
        i['settledPrice']=mini

for i in data:
    print(i)