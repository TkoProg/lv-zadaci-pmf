n = int(input("Unesite prirodan broj n: "))
brojac = 0

for i in range(n):
    if i == n - 1:
        break
    print(" " * (n - i - 1), end="")
    print("*", end="")
    if i > 0:
        print(" " * (i + brojac), end="")
        brojac += 1
        print("*", end="")
    print()

for j in range(n):
    for k in range(n - 1):
        if j == 0 or j == n - 1:
            print("* ", end="")
        else:
            if k == 0:
                print("* ", end="")
            else:
                print(" " * 2, end="")
    print("*", end="")
    print()
