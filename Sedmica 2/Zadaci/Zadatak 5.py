a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))
a2 = float(input("a2: "))
b2 = float(input("b2: "))
c2 = float(input("c2: "))

kol_b = b1 / b2
x = (c2 * kol_b - c1) / (a1 - a2 * kol_b)

kol_a = a1 / a2
y = (c2 * kol_a - c1) / (b1 - b2 * kol_a)

print(f"Rjesenja su x={x} y={y}")
