chx = input("Please Enter Your Own Character : ")
if not(chx.isalpha()):
    print("Please only enter alphabetical character")
    exit()
if len(chx) > 1:
    print("Your first character will be proccesed")
ch = chx[0]
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'
       or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("The Given Character ", ch, "is a Vowel")
else:
    print("The Given Character ", ch, "is a Consonant")