a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

racun = (abs(a+b-c) + abs(a-b+c) + abs(-a+b+c)) / 3
decimale = int((racun - int(racun)) * 100) * (1/100)

print(f"Racun sa najvise dvije decimale je: {int(racun)+decimale}")
print(f"Racun sa tacno dvije decimale je: {racun:.2f}")
