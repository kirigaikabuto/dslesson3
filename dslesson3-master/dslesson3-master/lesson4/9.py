s = "12341234"
numbers=[int(i) for i in s]
n = len(numbers)
middle = n//2
left_sum=0
right_sum=0
for i in range(0,middle):
    left_sum = left_sum+numbers[i]
for i in range(middle,n):
    right_sum = right_sum+numbers[i]

if left_sum == right_sum:
    print("yes")
else:
    print("no")