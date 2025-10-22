nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

names = []

nimi = input("Anna eka nimi tai lopeta Enterillä: ")

while nimi != "":
    names.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta Enterillä: ")
#Yllä viitataan listaan. append lisää arvon listaan, mutta ei muista jos ajat uudestaan
#eli alkaa alusta aina

print(names)