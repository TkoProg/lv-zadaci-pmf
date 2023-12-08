def pomjeri_vrijednost(l):
    prvi_ele = l[0]
    for i in range(len(l)):
        if i != len(l) - 1:
            l[i] = l[i+1]
        else:
            l[i] = prvi_ele
    return l


print(pomjeri_vrijednost([1, 2, 3, 4, 5]))
