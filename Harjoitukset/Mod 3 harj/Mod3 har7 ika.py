age = int(input("Anna ikäsi: "))

if age >= 65:
    print("Olet eläkeikässä.")
elif age >= 18:
    print("olet työikäinen.")
elif age >= 7:
    print("Olet koululainen.")
#Else lause ajetaan, jos mikään muu ei toteudu eli ei ole totta
else:
    print("Olet pikkulapsi.")

print("Suoritus jatkuu...")