#Vihje: tutustu random.randint()-funktion käyttöön

import random

#eka = (f"Rolled: {random.randint(0, 9)}")
eka = (f" {random.randint(0, 9)}")
toka = (f" {random.randint(0, 9)}")
kolmas = (f" {random.randint(0, 9)}")

uno = (f" {random.randint(1, 6)}")
dos = (f" {random.randint(1, 6)}")
tres = (f" {random.randint(1, 6)}")
quatro = (f" {random.randint(1, 6)}")

print("arvottu kolminumeroinen koodi 0 - 9 välillä on: ", eka, toka, kolmas)
print("Arvottu neljänumeroinen koodi 1 - 6 välillä on: ", uno, dos, tres, quatro)