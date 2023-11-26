import math


def jelProst(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def vratiProst(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n


n = int(input("Unesite paran prirodan broj: "))

brojac = 1
while True:
    if jelProst(n-brojac):
        prvi = vratiProst(brojac)
        drugi = n - prvi
        if jelProst(drugi):
            break
        else:
            brojac += 1
            continue
    brojac += 1

print(f"Dva prosta broja koji sacine broj {n} su: {prvi} i {drugi}")
