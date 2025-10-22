#While (ehto): eli koodilohko joka toistetaan
#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000."
luku = 1

while luku <= 1000:
    #katsotaan seuraavaksi , onko luku jaollinen kolmella
    if luku % 3 == 0:
        print(luku)
    luku += 1

    #onko 1 jaollinen 3? ei eli lisätään yhdellä (ei print), lisätään yksi (no pprint)
    #onko 3 jaollinen 3? on, niin printataan luku jne.



