st = "Hello World"
counter_upper=0
counter_lower=0
#islower()
#isupper()
for i in st:
    if i.isupper():
        counter_upper=counter_upper+1
    else:
        counter_lower=counter_lower+1

print(f"Upper case character count is {counter_upper}")
print(f"Lower case character count is {counter_lower}")
    