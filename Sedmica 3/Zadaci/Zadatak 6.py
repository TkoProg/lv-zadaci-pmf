a = input("Unesite petocifren broj: ")

if 9999 < int(a) < 100000:
    a.split()
    a = [int(x) for x in a]
    a = sorted(a)
    print(f"Rjesenje je: {a[-2] - a[0]}")
