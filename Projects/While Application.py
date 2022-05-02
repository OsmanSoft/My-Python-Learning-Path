#sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
"""
i = 0
while i<len(sayilar):
    print(sayilar[i])
    i +=1


# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
# tek sayıları ekrana yazdırın.

baslangıc = int(input("Başlangıç: "))
bitis = int(input("Bitiş: "))

x = baslangıc  
while x < bitis:
    x += 1
    if x%2==1:
        print(x)

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

x = 100

while x > 1:
    x -= 1
    print(x)
"""

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
"""
lis = []
x = 1
while x<=5:
    sayi = int(input("Sayı gir: "))
    lis.append(sayi)
    x += 1

lis.sort()
print(lis)
"""
# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input("Kaç adet ürün var? "))

x = 0
while x<adet:
    name = input("name: ")
    price = input("price: ")
    urunler.append({"name": name, "price": price })
    x += 1

 