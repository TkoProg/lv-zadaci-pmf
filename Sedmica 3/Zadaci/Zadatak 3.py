def funckcija(v):
    if v <= 0:
        return v ** 2
    elif 0 < v <= 100:
        return (100 - v) / v ** 4
    elif 100 < v:
        return 200


x = float(input("Unesite broj: "))

print(f"f({x}) = {funckcija(x)}")
