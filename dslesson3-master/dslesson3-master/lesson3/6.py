cash=[1,2,3,4]
sumi=0
for i in cash:
    if i%2!=0:
        continue
    sumi=sumi+i

print(sumi)
