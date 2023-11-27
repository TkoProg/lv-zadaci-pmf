def najmanjiZjednicki(m,n):
    najm = min(m, n)
    nzd = 0
    for i in range(1, najm+1):
        if m % i == 0 and n % i == 0:
            nzd = i
    return nzd


m = int(input("Unesite prvi prirodan broj: "))
n = int(input("Unesite drugi prirodan broj: "))

print(f"NZD brojeva {m} i {n} je: {najmanjiZjednicki(m,n)}")
