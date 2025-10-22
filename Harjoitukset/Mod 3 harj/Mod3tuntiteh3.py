n = int(input("Anna kokonaisluku: "))

#Ensimmäiseksi pitää laittaa tapaus, jossa molemmat on totta eli onko molemmilla jaollinen
#"elif muista"
if n % 3 == 0 and n % 5 == 0:
    print("BoomBuzz")
elif n % 3 == 0:
    print("Boom")
elif n % 5 == 0:
    print("Buzz")



