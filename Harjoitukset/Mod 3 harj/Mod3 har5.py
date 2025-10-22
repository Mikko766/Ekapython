raha = float(input("Paljonko sinulla on rahaa: "))

#Jos ehto alla ei täyty eli rahaa alle 5, niin tulostaa vain kiitos hei, muutoin molemmat
if raha >= 5:
    print("Rahasi riittää, voit ostaa kahvin!")
#Huom. else kommentti

else:
    print("Rahasi eivät riitä kahviin.")

print("Kiitos ja Hei!")

#Huomaa print koodin taso : pisteen jälkeen, kun if pitää olla tab eli 4x väli