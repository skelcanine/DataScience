try:
    liste = ['Merhaba', 42, 3.414, True, None]
    liste.sort()
    print(liste)
except Exception as e:
    print ("'{}' hatası oluştu ! ".format(e))