def jelPalindorm(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[len(n)-i-1]:
            return f"Broj {n} nije palindrom! (Znas li sta je definicija palindroma lmao?)"
    return f"Broj {n} je palindrom!"


n = int(input("Unesite broj, program provjerava da li je palindrom: "))

print(jelPalindorm(n))
