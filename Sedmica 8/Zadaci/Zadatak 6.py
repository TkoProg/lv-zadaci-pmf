lista_str = input().split(" ")

lista = []

for element in lista_str:
    lista.append(float(element))

n = int(input())
lista.sort(reverse=True)

maks_element = lista[0]
n_ti_najveci = lista[n-1]

print(f"Razlika izmedju {najveceg} i {n-n_ti_najveci} je {maks_element - n_ti_najveci}")
