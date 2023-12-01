def rastuci_niz(lista):
    # sortirana_lista = sorted(lista)
    # return sortirana_lista == lista

    rastuca = True
    for i in range(1, len(lista)):
        if lista[i] < lista[i-1]:
            rastuca = False
    return rastuca


print(rastuci_niz([1, 2, 3, 3]))
