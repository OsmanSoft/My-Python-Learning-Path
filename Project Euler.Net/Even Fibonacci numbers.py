fibonacci = list()

fibonacci.append(1)
fibonacci.append(2)

i = 2
toplam = 0

while fibonacci[i-1] + fibonacci[i-2] < 4000000 :
	fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
	i += 1

for i in fibonacci:
	if i%2==0:
		toplam += i

print(toplam)

