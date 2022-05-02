'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''

import random

rand_number = random.randint(1,100)
hak = int(input("Deneme sayısı giriniz: "))
can = hak
sayac=0

while hak>0:
    hak-=1
    sayac+=1
    tahmin = int(input("Bir sayı giriniz: "))
    if tahmin==rand_number:
        point=(100-((100/can)*(sayac-1)))
        print(f"Tebrikler sayıyı buldunuz. Puanınız: {point}")
        break
    elif tahmin>rand_number:
        print("Girdiğin değer random sayıdan yukarıda")
    elif tahmin<rand_number:
        print("Girdiğin değer random sayıdan aşağıda")
    if hak==0:
        print("Hakkınız bitmiştir.")

print(rand_number)
