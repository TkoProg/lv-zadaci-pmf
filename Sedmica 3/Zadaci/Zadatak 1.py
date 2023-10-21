def bodovi(vj, p11, p21, zv):
    return vj + p11 + p21 + zv


def prolaz(ukupan):
    if 95 <= ukupan <= 100:
        return "Ocjena 10"
    elif 85 <= ukupan <= 94:
        return "Ocjena 9"
    elif 75 <= ukupan <= 84:
        return "Ocjena 8"
    elif 65 <= ukupan <= 74:
        return "Ocjena 7"
    elif 55 <= ukupan <= 64:
        return "Ocjena 6"
    elif 0 <= ukupan <= 54:
        return "Ocjena 5"
    else:
        return "Broj bodova nije validan!"


v = int(input("Unesite broj bodova osvojenih na vjezbama: "))
p1 = int(input("Unesite broj bodova osvojenih na prvoj parcijali: "))
p2 = int(input("Unesite broj bodova osvojenih na drugoj parcijali: "))
z = int(input("Unesite broj bodova osvojenih na zavrsnom ispitu: "))

ukupno = bodovi(v, p1, p2, z)

print(prolaz(ukupno))
