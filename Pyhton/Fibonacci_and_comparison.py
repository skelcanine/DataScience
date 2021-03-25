fiblist = list()

fiblist.append(1)
fiblist.append(1)
for i in range(1,49):
    fiblist.append(fiblist[i-1]+fiblist[i])

print(fiblist)


enbisim = ""
enbyas = 0
for i in range(3):
    isim = input("Lutfen ismi giriniz: ")
    yas = input("Lutfen yasi giriniz ")
    if(i==0 or enbyas<yas):
        enbyas = yas
        enbisim = isim
print(enbisim, " En buyuktur")
