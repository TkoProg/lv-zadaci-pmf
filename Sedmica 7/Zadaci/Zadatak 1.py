def brojeviIzmedju(n,a,b):
    n = str(n)
    najv = max(a, b)
    najm = min(a, b)
    brojac = 0
    for i in range(len(n)):
        if najm < int(n[i]) < najv:
            brojac += 1
    return brojac


n = int(input())
a = int(input())
b = int(input())

print(f"Trazeni broj je: {brojeviIzmedju(n,a,b)}")
