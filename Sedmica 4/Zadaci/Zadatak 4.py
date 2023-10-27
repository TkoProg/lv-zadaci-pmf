import random

a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b koji je veci od a: "))

neki = random.randint(a, b)

while True:
    n = int(input("Pogodite generisani broj: "))
    if n == neki:
        print("Nasli ste ga!")
        break
    elif n < neki:
        print("Generisani broj je veci od unesenog!")
    elif n > neki:
        print("Generisani broj je manji od unesenog!")
