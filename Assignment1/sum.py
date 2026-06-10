# 5. Create a list of integers from 1 to 10 and print it. Calculate the sum of all the numbers in the list and print the result.

num = [1,2,3,4,5,6,7,8,9,10]
print(num)
sum = 0

for i in num:
    sum+=i

print("Sum of numbers from 1 to 10 is "+str(sum))
