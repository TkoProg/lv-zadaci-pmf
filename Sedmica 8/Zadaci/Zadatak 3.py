from random import randint


def generisi_niz(a,b):
    lista = []
    if b-a+1 < 10:
        print(f"U segmentu [{a}, {b}] nema 10 brojeva.")
    else:
        while len(lista) < 10:
            random_broj = randint(a, b)
            if random_broj not in lista:
                lista.append(random_broj)
        print(lista)


generisi_niz()