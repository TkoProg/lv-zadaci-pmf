suma = 0
print("Program ispisuje sumu posljednjih cifara cijelih brojeva")
while True:
    n = input("Unesite cijeli broj: ")
    if n == "-1":
        break
    else:
        suma += int(n[-1])

print(f"Suma posljednjih brojeva je: {suma}")
