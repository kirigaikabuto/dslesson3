#break закрывает цикл 
cash=[1000,1600,1100,550]
sumi=0
for i in cash:
    sumi = sumi + i
    if sumi > 2500:
        break
print(sumi)