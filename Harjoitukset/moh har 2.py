summa = 0

while True:
    num = int(input("Anna luku, tai -1 lopettaaksesi: "))
    if num == -1:
        break
    if num >= 10:
        continue
    summa += num

print(f"Summa on {summa}.")