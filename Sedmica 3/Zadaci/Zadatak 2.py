def trocifren(br):
    if 100 <= br <= 999:
        br = str(br)
        return f"Proizvod: {int(br[0])*int(br[1])*int(br[2])}"
    else:
        return "Nije trocifren!"


broj = int(input("Unesite trocifren broj, program ispisuje proizvod cifara unesenog broja: "))

print(trocifren(broj))
