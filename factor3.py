def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

inputs = []
for i in range(4):
            
    num = int(input("Enter a number: "))
    inputs.append(num)

factorials = []
for num in inputs:
    factorials.append(factorial(num))
print("Factorials:")
for i in range(len(inputs)):
   print(f"The factorial of {inputs[i]} is {factorials[i]}")
        