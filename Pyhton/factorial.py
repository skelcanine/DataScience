def factorial(number):
    factorial = 1
    for i in range(2,number+1):
        factorial = i * factorial
    return factorial


tocalc = int(input("Enter number to get factorial= "))
print(factorial(tocalc))