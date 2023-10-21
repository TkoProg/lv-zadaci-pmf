def sljedeci(d, m, g):
    godina = []
    if m % 2 == 0:
        if g <= 0:
            return "Godina nije ispravna"
        elif 1 > m > 12:
            return "Mjesec nije ispravan"
        elif 1 > d > 31:
            return "Dan nije ispravan"
    elif m % 2 != 0:
        if g <= 0:
            return "Godina nije ispravna"
        elif 1 > m > 12:
            return "Mjesec nije ispravan"
        elif 1 > d > 30:
            return "Dan nije ispravan"
    if (g % 4 == 0) and (g % 100 == 0) and (g % 400 == 0):
        if d == 29 & m == 2:
            pres = [1, 3, g]
            return pres
        else:
            d = d + 1
            pres = [d, m, g]
            return pres
    if m == 2:
        if 1 <= d <= 27:
            d = d + 1
            feb = [d, m, g]
            return feb
        elif d == 28:
            d = 1
            m = 3
            feb = [d, m, g]
            return feb
    if m % 2 == 0:
        if 1 <= d <= 30:
            d = d + 1
        elif d == 31:
            d = 1
            if 1 <= m <= 11:
                m = m + 1
            if m == 12:
                m = 1
                g = g + 1
    else:
        if 1 <= d <= 30:
            d = d + 1
        elif d == 30:
            d = 1
            if 1 <= m <= 11:
                m = m + 1
            if m == 12:
                m = 1
                g = g + 1
    godina.append(d)
    godina.append(m)
    godina.append(g)
    return godina


god = input("Unesite dan, mesec i godinu (ex: 11.4.2024): ").split(".")

god = [int(x) for x in god]

print(sljedeci(god[0], god[1], god[2]))

