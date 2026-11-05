vstup1 = input("Zadej číslo: ")
vstup2 = input("Zadej číslo: ")


cislo1 = float(vstup1)
cislo2 = float(vstup2)

v = vstup1 + vstup2
vysledek = cislo1 + cislo2

print("Soucet cisel je: " + str(vysledek) + ".")

print(f"Soucet cisel je: {vysledek}.")

print("Soucet cisel je: {}.".format(vysledek))