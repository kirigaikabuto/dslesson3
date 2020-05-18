salary=1000
percent=0.0
if salary>=1000:
    percent = 0.3
elif salary>500 and salary<=1000:
    percent = 0.2
elif salary>250 and salary<=500:
    percent = 0.15
total = salary +salary*percent
print(total)