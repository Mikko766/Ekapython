#funktioesimerkki, ja def jotta tiedetään funktio määritelmä(montako kertaa)
def terve(tervehdys, kerrat):
    for k in range(kerrat):
        print(tervehdys)
    return
#range funktio tarvitsee numeron, teksti ei kelpaa. yllä kerrat suluissa on numeraalinen "kerrat alla"
def yhteenlasku(luku1, luku2, luku3):
    summa = luku1 + luku2 + luku3
    return summa
#Palauta summa eli return yllä

#Pääohjelma
print ("uusi päivä alkaa tervehdyksellä:")
terve("Moikka!", 3)
#Tuo kolmonen lähetetään ylös kohtaan deef terve(kerrat tänne)
print("jatketaan eteenpäin!")
terve("Hei hei", 2)
yhteenlasku(3,2, 3)
#jos kaksi parametriä, niin molemmat pitää täyttää ja print loppuun!
#ohjelma luetaan ylhäältä ala ja määritetyt funktiot luetaan
# kun funktio kutsutaan palaa ohjelma ylös ja suorittaa funktion (return)
#Jos halutaan toistaa, tulee lisätä uusi kutsu