#Laivan hyttiluokan tulostus
hytti = input("Anna hyttiluokkasi: LUX, A, B, C: " )

if hytti == "LUX":
    print("LUX luokan hytti on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
    print("A luokan hytti on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print("B luokan hytti on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("C luokan hytti on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")


