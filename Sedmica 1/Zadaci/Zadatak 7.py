zenski = int(input("Unesite broj zenskih osoba u razredu: "))
muski = int(input("Unesite broj muskih osoba u razredu: "))

procenat_zenskih = round((zenski/(muski+zenski))*100, 2)
procenat_muskih = round((muski/(muski+zenski))*100, 2)

print(f"Procenat zenskih osoba u razredu je: {procenat_zenskih}")
print(f"Procenat muskih osoba u razredu je: {procenat_muskih}")
