import random

m = int(input())
n = int(input())

rijec = ""

lista = []

for i in range(m):
    rijec = ""
    for j in range(n):
        broj = random.randint(65, 122)
        slovo = chr(broj)
        if not slovo.isalpha():
            while not slovo.isalpha():
                broj = random.randint(65, 122)
                slovo = chr(broj)
        rijec += slovo
    lista.append(rijec)

file = open("Zadatak 3.in", "w")

for i in range(len(lista)):
    file.write(lista[i] + "\n")

file.close()
