def brojUBinarni(n):
    n = str(bin(n))
    n = n[2:]
    return n


n = int(input("Unesite broj: "))
print(f"Broj {n} zapisano binarno je: {brojUBinarni(n)}")
