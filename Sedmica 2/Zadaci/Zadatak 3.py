sek = int(input("Unesite ugao u sekundama: "))

step = sek / 60 / 60
minu = (step - int(step)) * 60
seku = round((minu - int(minu)) * 60)

step = round(step)
minu = round(minu)

print(f"Stepeni {step} | Minute: {minu} | Sekunde: {seku}")
