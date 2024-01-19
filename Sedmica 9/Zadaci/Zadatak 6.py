def ukloni_slova(rijec):
    rijec = rijec.lower()
    while not samo_jedno_slovo(rijec) > 1:
        slovo = rijec[0]
        rijec = rijec.replace(slovo, "")


def samo_jedno_slovo(rijec):
    prvo_slovo = rijec[0]
    for slovo in rijec:
        if slovo != prvo_slovo:
            return False
    return True


rijec = input()
ukloni_slova(rijec)
