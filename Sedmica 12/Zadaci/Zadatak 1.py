def najveciKljuc(r):
    najveca = 0

    for rijec in r:
        vrijednost = r[rijec]
        if vrijednost > najveca:
            najveca = vrijednost

    print(najveca)


rijecnik = {
    "a": 3,
    "b": 10,
    "c": 5
}

najveciKljuc(rijecnik)
