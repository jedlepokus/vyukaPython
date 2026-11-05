a = float(input("Zadej cislo a: "))
b = float(input("Zadej cislo b: "))
c = float(input("Zadej cislo c: "))

if (a + b > c) * (b + c > a) * (c + a > b):
    print("Trojuhelnik lze zkonstruovat.") 
else:
    print("ee.")

if (a + b <= c):
    print("nejde")
elif b+c<=a:
    print("nejde")
elif a+c<=b:
    print("nejde")
else:
    print("jojo")