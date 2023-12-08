def zavrsava_sa(l, s):
    rezultat = 0
    n = len(s)
    for rijec in l:
        if rijec[-n:] == s:
            rezultat += 1
    return rezultat


print(zavrsava_sa(["abc", "gshbc", "dbe", "garbc"], "bc"))
