file = open("Zadatak 1.in", "r")

citavo = file.read()
recenice = citavo.split(".")

print(len(recenice)-1)

file.close()
