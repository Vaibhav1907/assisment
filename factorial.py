def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact
number = [2,5,7,8]

for num in number:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
