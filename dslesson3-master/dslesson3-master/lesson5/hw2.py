word = "Hellloo"
unique=[]
unique_count=[]
for i in word:
    if i not in unique:
        unique.append(i)
for i in unique:
    counter=0
    for j in word:
        if i==j:
            counter+=1
    unique_count.append(counter)
n = len(unique)
for i in range(n):
    print(unique[i],unique_count[i])