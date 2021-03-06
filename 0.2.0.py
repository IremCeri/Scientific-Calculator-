import math

def toplama(x, y):
    return x + y

def çıkartma(x, y):
    return x - y

def üshesapla(x,y):
    return x ** y

def çarpma(x,y):
    return x * y

def bölme(x,y):
    return x / y

def mod(x,y):
    return x % y

def piçarpma(x,y):
    return x * y

def pibölme(x,y):
    return x / y

def pitoplama(x,y):
    return x + y

def piçıkartma(x,y):
    return x - y

def karekök(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def log10(x):
    return math.log(x, 10)

def log2(x):
    return math.log2(x, 2)

def faktöriyel(x):
    return math.factorial(x)

def mutlakdeğer(x):
    return math.fabs()

def radyanderece(x):
    return math.degrees(x)

def dereceradyan(x):
    return math.radians(x)

def sayınınkaresi(x):
    return x ** 2

def sayınınküpü(x):
     return x ** 3

print("""
Lütfen Bir İşlem Seçiniz:
1-Toplama '+'
2-Çıkartma '-'
3-Çarpma '*'
4-Bölme '/'
5-Üs Alma 'xʸ'
6-PI ile Çarpma-Bölme-Toplama-Çıkartma 
7-Karekök Hesaplama '√x'
8-Sin
9-Cos
10-Tan
11-LOG 10 
12-LOG 2
13-Faktöriyel 'x!'
14-Mutlak Değer '|x|'
15-Radyanı Dereceye Çevirme 'xπ'
16-Dereceyi Radyana Çevirme 'x°'
17-Mod Alma 'x%'
18-Sayının Karesi 'x²'
19-Sayının Küpü 'x³'
        """)

selection= input("Seçtiğiniz İşlemi Yazınız (1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19): ")
if selection == '1':
    number1 = float(input("Bir sayı girin: "))
    number2 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "+", number2, "=", toplama(number1, number2))

elif selection == '2':
    number1 = float(input("Bir sayı girin: "))
    number2 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "-", number2, "=", çıkartma(number1, number2))

elif selection == '3':
    number1 = float(input("Bir sayı girin: "))
    number2 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "*", number2, "=", çarpma(number1, number2))

elif selection == '4':
    number1 = float(input("Bir sayı girin: "))
    number2 = int(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "/", number2, "=", bölme(number1, number2))

elif selection == '5':
    number1 = float(input("Bir sayı girin: "))
    number2 = int(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "**", number2, "=", üshesapla(number1, number2))

elif selection == '6':
    number1 = float(input("Bir sayı girin: "))
    number2 = float(3.14)
    operation= input("Hangi işlemi yapmak istersin? (Çarp-Böl-Topla-Çıkar)")
    if operation == 'çarp' or operation == 'Çarp':
        print("ÇÖZÜM: ", number1, "*", number2, "=", piçarpma(number1, number2))
    elif operation == 'böl' or operation == 'Böl':
        print("ÇÖZÜM: ", number1, "/", number2, "=", pibölme(number1, number2))
    elif operation == 'topla' or operation == 'Topla':
        print("ÇÖZÜM: ", number1, "+", number2, "=", pitoplama(number1, number2))
    elif operation == 'çıkar' or operation == 'Çıkar':
        print("ÇÖZÜM: ", number1, "-", number2, "=", piçıkartma(number1, number2))

elif selection == '7':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "=", karekök(number1))

elif selection == '8':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "sin", "=", sin(number1))

elif selection == '9':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "cos", "=", cos(number1))

elif selection == '10':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "tan", "=", tan(number1))

elif selection == '11':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "log10", "=", log10(number1))

elif selection == '12':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "log2", "=", log2(number1))

elif selection == '13':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "!", "=", faktöriyel(number1))

elif selection == '14':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ",'|',number1,'|', "=", mutlakdeğer(number1))

elif selection == '15':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ",number1,"π", "=", radyanderece(number1))

elif selection == '16':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "°", "=", dereceradyan(number1))

elif selection == '17':
    number1 = float(input("Bir sayı girin: "))
    number2 = int(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1, "%", number2, "=", mod(number1, number2))

elif selection == '18':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1,"²", "=", sayınınkaresi(number1))

elif selection == '19':
    number1 = float(input("Bir sayı girin: "))
    print("ÇÖZÜM: ", number1,"³", "=", sayınınküpü(number1))