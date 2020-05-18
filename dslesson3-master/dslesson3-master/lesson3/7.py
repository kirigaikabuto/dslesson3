money = 1000
cars=[100,200,300,400,500,600]
sumi=0
count=0
for i in cars:
    if sumi+i>money:
        break
    sumi = sumi +i
    count = count +1
print(count)