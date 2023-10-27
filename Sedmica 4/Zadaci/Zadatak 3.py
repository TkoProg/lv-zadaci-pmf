def aritmeticka(poslano):
    zbir = 0
    for k in range(len(poslano)):
        zbir += poslano[k]
    return zbir / len(poslano)


def geometrijska(poslano):
    pro = 1
    for k in range(len(poslano)):
        pro *= poslano[k]
    return pro ** (1 / len(poslano))


def harmonijska(poslano):
    zbir = 0
    for k in range(len(poslano)):
        zbir += 1 / poslano[k]
    return len(poslano) / zbir


def kvadratna(poslano):
    zbir = 0
    for k in range(len(poslano)):
        zbir += poslano[k] ** 2
    return (zbir / len(poslano)) ** (1/2)


n = int(input("Unesite prirodan broj n: "))
brojevi = []

for i in range(n):
    m = int(input(f"Unesite {i + 1}. prirodan broj: "))
    brojevi.append(m)

print()

print(f"Aritmeticka sredina je:  {aritmeticka(brojevi)}")
print(f"Geometrijska sredina je: {geometrijska(brojevi)}")
print(f"Harmonijska sredina je:  {harmonijska(brojevi)}")
print(f"Kvadratna sredina je:    {kvadratna(brojevi)}")
