toplam=0
for i in range(1,101):
	toplam += i**2

top=0
for i in range(1,101):
	top += i

a=top**2

print(a-toplam)