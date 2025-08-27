#Voit laittaa myös int sijasta Float
pituus = int(input("Anna pituutesi: "))
paino = float(input("Anna painosi: "))

#Muuttuja, jossa lasku suoritetaan
bmi = paino / (pituus / 100) ** 2
print("Pituus-paino-indeksisi on", bmi)
print(f"Pituus-paino-indeksisi on {bmi:.2f}")
print(f"Pituus-paino-indeksisi on {bmi:10.2f}")

#Käytä vastaus kentässä alla pistettä. ei pilkkua,


