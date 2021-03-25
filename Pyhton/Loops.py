girdi = input("Bir kelime giriniz: ")

print(girdi[::-1])




sayi = int(input("Bir sayi giriniz: "))

for i in range(1,11):
    print(sayi, " x ", i, " = ", i*sayi)







liste = [x**3 if x % 2 == 0 else x**2 for x in range(1,21)]
print(liste)






liste = [x for x in range(1,201) if x%2==0]
print(liste)
liste = [x for x in range(1,201) if x%2==1]
print(liste)