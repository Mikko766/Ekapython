koira = input("Mikä koiran nimi on? ").lower()
kissa = input("Mikä kissan nimi on?").lower()

if koira == kissa:
    print("Oho, niillä on sama nimi!")

#Huom, jos vastaus ISOlla kirjaimella, niin ei tunnista
#.lower() perässä, niin ei huomioi isoja tai pieniä kirjaimia