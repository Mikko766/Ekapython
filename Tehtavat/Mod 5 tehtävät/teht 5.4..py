#kaupungit lista rakenteella 5.4.
kaupungit = []

for i in range(5):
    nimi = input(f"Anna {i+1}. kaupungin nimi: ")
    kaupungit.append(nimi)

print("Tässä kaupungit, jotka kerroit:")
for kaupunki in kaupungit:
    print(kaupunki)
