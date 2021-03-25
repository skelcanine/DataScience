def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def gcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd





number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("Least common multiplier is", lcm(number1, number2))
print("Greatest common divisor is", gcd(number1, number2))