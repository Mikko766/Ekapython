def seven_brothers(lista):
    #Kirjoita funktion toiminta, järjestetään lista aakkosjärjestykseen
    lista.sort()
#lista.sort() yllä järjestää aakkosiin
    #Tulostetaan nimet
    print(lista)

    #Tulostetaan nimet yksitellen on toinen tapa, käytetään "for looppia" alla
    #Tallentaa aina yhden nimi Aapo ja tulosta, loop pyörähtää, poimii Eeron ja tulosta jne.
    for nimi in lista:
        print(nimi)
    return


#Pääohjelma
veljekset = ["Eero", "Aapo", "Lauri", "Juhani", "Simeoni", "Timo", "Tuomas"]
#kutsutaan meidän funtiota alla
seven_brothers(veljekset)

