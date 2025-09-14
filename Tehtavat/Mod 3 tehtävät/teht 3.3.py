#henoglobiini arvot
bio = input("Anna biologinen sukupuolesi eli nainen tai mies: "). lower()
hem = int(input("Anna hemoglobiini arvosi: "))


if bio != "nainen":
    print("")
elif hem <= 116:
    print("Hemoglobiini arvosi on matala!")
elif hem >= 176:
    print("Hemoglobiini arvosi on korkea!")
else:
    print("hemoglobiiniarvosi on normaali")

if bio != "mies":
    print("")
elif hem <= 133:
    print("Hemoglobiini arvosi on matala!")
elif hem >= 196:
    print("Hemoglobiiniarvosi on korkea!")
else:
    print("Hemoglobiiniarvosi on normaali")


