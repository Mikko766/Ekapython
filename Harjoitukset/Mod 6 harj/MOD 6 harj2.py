#funktio esimerkki2
#Funktiomääritelmä (Alla on paikallinen eli lokaali muuttuja
def muuta():
    _city = "Vantaa"
    print("Funktion päätteeksi kaupungin nimi on: " + _city)
    return
#Parempi käyttää eri nimisiä tai ainakin _city kera
#Pääohjelma (Globaali muuttuja) eli näkyy kaikkialle
city = "Helsinki"
print("Pääohjelma alussa kaupungin nimi on: " + city)
muuta()
print("Pääohjelman lopussa kaupungin nimi on: " + city)