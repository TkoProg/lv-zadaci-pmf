file = open("Zadatak 4.in", "r")

citavo = file.read()

file.close()

novo = ""

for i in range(len(citavo)):
    if i == 0 and citavo[i] == "i" and (not citavo[i + 1].isalpha()):
        novo += "I"
    elif citavo[i] == "i" and (not citavo[i - 1].isalpha()) and (not citavo[i + 1].isalpha()):
        novo += "I"
    elif i == len(citavo) - 1 and citavo[i] == "i" and (not citavo[i - 1].isalpha()):
        novo += "I"
    else:
        novo += citavo[i]

fajl = open("Zadatak 4.in", "w")

fajl.write(novo)

fajl.close()
