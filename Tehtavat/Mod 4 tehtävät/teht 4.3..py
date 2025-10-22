luku = input("Anna luku, tyhjä lopettaa: ")

pieni = luku
suuri = luku
#luku on aina pieni ja suuri, koska ei ole määritelty
#alla pelkät "" eli tyhjä
while luku != "":
    numero = int(luku)

    #Vertaillaan pientä ja suurta
    if pieni == luku or numero < pieni:
        pieni = numero

    #Jos uusi luku on pienempi kuin edellinen pieni se tallentaan uudeksi pieneksi
    if suuri == luku or numero > suuri:
        suuri = numero

    luku = input("Anna luku, tyhjä lopettaa: ")

print(f"Pienin luku on {pieni}")
print(f"Suuri luku on {suuri}")


