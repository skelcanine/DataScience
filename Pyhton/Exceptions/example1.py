try:
    x = int(input("Bir sayı girin   : "))
    y = int(input("Bir sayı daha girin   : "))
    print(x/y)
except ValueError:
    print('Dosyada numerik olmayan veri var')
except Exception as e:
    print ("'{}' hatası oluştu ! ".format(e))


