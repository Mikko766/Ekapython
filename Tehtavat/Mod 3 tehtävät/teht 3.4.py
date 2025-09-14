#ohjelma kysyy vuosiluvun ja kertoo, onko se karkausvuosi
vuosi = int(input("Ohjelma kertoo, onko vuosi karkausvuosi. Anna vuosiluku: "))

if vuosi % 4 == 0:
    print("Kyseessä on karkausvuosi.")

#Opettaja, en keksinyt mitä tarkoitetaan sillä, että 100:lla jaolliset tulee olla jaollisia myös 400:lla?
#Kaikki sataset ja tuhannetkin tasaluvut on jaollisia 4:llä eli karkausvuosi kyseessä.