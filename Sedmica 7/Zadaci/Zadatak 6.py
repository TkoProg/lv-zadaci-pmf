import math


def jelProst(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def najmanjiZajednicki(m,n):
    najm = min(m, n)
    nzd = 0
    for i in range(1, najm+1):
        if jelProst(i):
            if m % i == 0 and n % i == 0:
                nzd = i
        else:
            continue
    return nzd


m = int(input("Unesite prvi prirodan broj: "))
n = int(input("Unesite drugi prirodan broj: "))

print(f"Najveci prosti broj koji djeli brojeve {m} i {n} je: {najmanjiZajednicki(m,n)}")
