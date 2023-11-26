def parniBrojevi(n):
    n = str(n)
    novi = ""
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            novi += n[i]
    return novi


n = int(input("Unesite broj, program stvara parni broj od njega: "))
print(f"Parni broj stvoren od broja {n} je: {parniBrojevi(n)}")
