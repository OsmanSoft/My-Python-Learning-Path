'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan 
   sayılara denir. 
'''

Number = int(input("Lütfen bir sayı giriniz: "))

asal = True

for i in range(2,Number):
    if Number % i == 0:
        asal = False
        print("Sayı asal değildir.")
        break
if asal == True:
    print("Sayı asaldır.")
