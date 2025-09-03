print("Valitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku"
"\n C: Kertolasku \n D: Desimaalijakolasku")

valinta = input("Valintasi (A - D): ").upper()
a = float(input("Anna ensimmäinen luku: "))
b = float(input("Anna toinen luku: "))
#.upper() muuttaa pienen kirjaimen a- A. voisit laittaa myös jokaiseen kohtaan .lower() pien..
#if valinta == "A" or valinta == "a":
if valinta == "A":
    print("Yhteenlasku:", a + b)
elif valinta == "B":
    print("Vähennyslasku:", a - b)
elif valinta == "C":
    print("Kertolasku:", a * b)
elif valinta == "D":
    print("Desimaalijakolasku:", a / b)
else:
    print("Valintasi oli virheellinen.")

#030925 laskinta paranneltu, \n vaihtaa riviä ekassa