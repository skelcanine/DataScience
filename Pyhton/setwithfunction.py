def removeduplucates(mylist):
    temp = list()
    for x in mylist:
        if x not in temp:
            temp.append(x)
    return temp

dlist = list()
while True:
    number = input("Enter number or enter another char for exit= ")
    if number.isnumeric():
        dlist.append(number)
    else:
        break

print(list(removeduplucates(dlist)))