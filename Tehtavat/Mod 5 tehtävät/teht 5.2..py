
syote = int(input("Anna numero (tai lopeta painamalla enter eli tyhjä): "))

numerot = []

while True:
    syote = input("Anna numero (tai lopeta painamalla enter eli tyhjä): ")
    if syote == "":
        break
    numerot.append(int(syote))
numerot.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in numerot[:5]:
    print(luku)

