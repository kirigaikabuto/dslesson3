n = int(input())
persons=[]
for i in range(n):
    person = input().split()
    #["yerassyl","tleugazy","22"]
    d={}
    d['name']=person[0]
    d['surname']=person[1]
    d['age']=person[2]
    persons.append(d)
for i in persons:
    print(i)