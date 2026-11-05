zadany_vek = input("Zadej svůj věk: ")

vek = int(zadany_vek)

if vek >= 18:
    print("Tak to jsi dospely.")
    print(f"Je ti {vek}.")
else:
    print("Tak to jsi jeste dite")
    chybi = 18 - vek
    if chybi == 1:
        print(f"Do dospelosti ti chybi {chybi} rok.")
    if 1 < chybi <= 4:    
        print(f"Do dospelosti ti chybi {chybi} roky.")
    if chybi > 4:
        print(f"Do dospelosti ti chybi {chybi} let.")


