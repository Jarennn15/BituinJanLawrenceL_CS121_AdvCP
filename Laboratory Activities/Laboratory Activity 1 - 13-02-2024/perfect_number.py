num1 = int(input("Enter a number: "))
sum = 0

for j in range (1, num1):
    if num1 % j == 0:
        sum += j
if sum == num1:
    print (f"{num1} is a perfect number.")
else:
    print (f"{num1} is not a perfect number.")
