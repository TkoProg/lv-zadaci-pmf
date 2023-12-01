def pojavljivanje_max(lista):
    maks_el = max(lista)
    broj_pojavljivanja = 0
    for element in lista:
        if element == maks_el:
            broj_pojavljivanja += 1
    print(f"Maksimalni element {maks_el} se pojavljuje {broj_pojavljivanja} puta.")
    # ovo je isto dobro: lista.count(maks_el)

pojavljivanje_max([1, 2, 3, 3, 2, 0])
