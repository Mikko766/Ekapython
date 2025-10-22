#funktioesimerkki, ja def jotta tiedetään funktio määritelmä(montako kertaa)
def terve(tervehdys, kerrat):
    for k in range(kerrat):
        print(tervehdys)
    return
#range funktio tarvitsee numeron, teksti ei kelpaa. yllä kerrat suluissa on numeraalinen "kerrat alla"
def yhteenlasku(_luku1, _luku2, _luku3):
    _summa = _luku1 + _luku2 + _luku3
    return _summa
#Palauta summa eli return yllä

#Pääohjelma
luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))
luku3 = int(input("Anna kolmas luku: "))

summa = yhteenlasku(luku1, luku2, luku3)
print("lukujen summa on ", summa)
