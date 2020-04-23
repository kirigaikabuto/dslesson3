s = "12341234"
numbers=[int(i) for i in s]
n = len(numbers)
middle = n//2
left = numbers[:middle]
right = numbers[middle:]
left_sum=0
right_sum=0
for i in left:
    left_sum = left_sum+i
for i in right:
    right_sum = right_sum+i
if left_sum == right_sum:
    print("yes")
else:
    print("no")