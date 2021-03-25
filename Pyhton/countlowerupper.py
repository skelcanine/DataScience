def countUpperAndLowerCase(sentence):
    upper = 0
    lower = 0
    for i in sentence:
        if 'A' <= i <= 'Z':
            upper += 1
        elif 'a' <= i <= 'z':
            lower += 1
    print("Upper case: " + str(upper))
    print("Lower case: " + str(lower))


countUpperAndLowerCase(input("Please enter a string "))
