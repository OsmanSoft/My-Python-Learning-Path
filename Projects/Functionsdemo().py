
# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 

def func(word, times):
    return word * times

print(func("Osman\n",5))

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

lis = []
def func(*params):

    for i in params:
        lis.append(i)
    print(lis)

func(10,20,30,40,5,6,7,89)


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def func(num1, num2):
    for num in range(num1, num2+1):
        if num > 1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)

func(10,20)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.
lis = []
def func(num):
    for i in range(1,num+1):
        if num%i == 0:
            lis.append(i)

    print(lis)

func(24)








