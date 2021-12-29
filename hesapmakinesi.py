sayi1 = int(input("1. sayiyi girin: "))
sayi2 = int(input("2. sayiyi girin: "))

secim = int(input("Seciminizi yapin\n1. Toplama\n2. Cikarma\n3. Carpma\n4. Bolme"))
if secim == 1:
    print("sonuc {}".format(sayi1+sayi2))
elif secim == 2:
    print("sonuc {}".format(sayi1-sayi2))   
elif secim == 3:
    print("sonuc {}".format(sayi1*sayi2)) 
elif secim == 4:
    print("sonuc {}".format(sayi1/sayi2))
else:
    print("Hatali giris yaptiniz")