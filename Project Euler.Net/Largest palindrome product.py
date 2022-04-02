
l=[]
for i in range(100,1000):
	for x in range(100,1000):
		y=x*i
		if y == int(str(y)[::-1]):
			l.append(y)

print(max(l))