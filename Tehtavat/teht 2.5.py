eka = float(input("Anna leiviskät: "))
toka = float(input("Anna naulat: "))
kolmas = float(input("Anna luodit: "))

luoti = 0.0133
naula = luoti * 32
leiviska = naula * 20

kilot = leiviska * eka + naula * toka + luoti * kolmas
print(f"Annettujen keskiaikaisten mittojen nykyaikainen paino on: {kilot:2.4f}","kilogrammaa")


