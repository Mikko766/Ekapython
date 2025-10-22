
import random

kuutiot = int(input("Kuinka monta arpakuutiota heitetään? "))



summa = 0
for i in range(kuutiot):
    silmaluku = random.randint(1, 6)
    summa += kuutiot

print(f"Arpakuutioiden summa on {summa}.")





