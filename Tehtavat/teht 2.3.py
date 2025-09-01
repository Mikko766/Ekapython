#Voit laittaa myös int sijasta Float
kanta = float(input("Anna suorakulmion kannan pituus: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

#Muuttuja, jossa lasku suoritetaan
piiri = kanta + kanta + korkeus + korkeus
pinta = kanta * korkeus

print("Suorakulmion piirin pituus on", piiri)
print("Suorakulmion pinta-ala on", pinta)
