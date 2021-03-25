

girdi = input("Lutfen sicaklik giriniz: ")
girdix = girdi

if 'F' in girdi:
    girdix = girdix.replace('F', '')
    print(girdix)
    C = (5 / 9) * (int(girdix) - 32)
    print(girdi, " --> ", C, "C")
else:
    girdix = girdix.replace('C', '')
    print(girdix)
    F = int(girdix) * 1.8 + 32
    print(girdi, " --> ", F, "F")


