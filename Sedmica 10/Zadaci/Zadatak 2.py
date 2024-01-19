# naziv = input()

file = open("Zadatak 2.in", "r")

citavo = file.read()

sve = ''

for i in range(len(citavo)):
    if (not citavo[i].isalpha()) and citavo[i] != " ":
        continue
    else:
        sve += citavo[i]

print(sve)

file.close()

sve = sve.split()

print(len(sve))
