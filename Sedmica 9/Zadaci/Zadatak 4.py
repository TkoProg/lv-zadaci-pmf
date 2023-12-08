def matrica_savrsena(m):
    svi_redovi_palindromi = True
    for red in m:
        if not (red == list(reversed(red))):
            svi_redovi_palindromi = False
            break

    sve_kolone_palindromi = True
    broj_kolona = len(m[0])
    broj_redova = len(m)
    for j in range(broj_kolona):
        kolona = []
        for i in range(broj_redova):
            kolona.append(m[i][j])
        if not (kolona == list(reversed(kolona))):
            sve_kolone_palindromi = False
            break
    if svi_redovi_palindromi and sve_kolone_palindromi:
        print("savrsena")
    elif not svi_redovi_palindromi and sve_kolone_palindromi:
        print("nesavrsena")
    else:
        print("polusavrsena")


matrica_savrsena([[1,2,2,1], [1,2,2,1], [1,4,4,1]])
