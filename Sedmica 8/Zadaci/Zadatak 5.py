def element_max_pojavljivanje(lista):
    max_broj_pojavljivanja = 0
    max_element = 0

    for element in lista:
        broj_pojavljivanja = lista.count(element)
        if broj_pojavljivanja > max_broj_pojavljivanja:
            max_broj_pojavljivanja = broj_pojavljivanja
            max_element = element

    print(f"Element sa maksimlanim brojem ponavljivanjima je {max_element} sa {max_broj_pojavljivanja} pojavljivanja.")


element_max_pojavljivanje([1, 2, 1, 1, 2, 2, 3, 2, 5, 1])
