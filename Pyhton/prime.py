number = int(input("Enter number to check whether it is prime: "))
for i in range(2,number):
    if not(number%i==0):
        print("Number is not prime")
        break
    else:
      print("Number is prime")
      break