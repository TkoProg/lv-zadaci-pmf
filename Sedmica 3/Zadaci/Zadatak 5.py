a = float(input("Broj a: "))
op = input("Unesite +,-,/,* ili %: ")
b = float(input("Broj b: "))

if op != "+" and op != "-" and op != "/" and op != "*" and op != "%":
    print("Taj unos nije opcija!")
else:
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "/":
        print(a / b)
    elif op == "*":
        print(a * b)
    elif op == "%":
        print(a % b)
