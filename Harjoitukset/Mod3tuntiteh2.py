#.lower() komennolla ei ole merkitystä onko iso vai pieni
nimi = input("Kerro nimesi: ").lower()
#keitto = int(input("Montako keittoannosta?"))
# != eri suuri kuin matti, huomaa "heittomerkit tekstiin""
if nimi != "matti":
    keitto = int(input("Montako keittoannosta? "))
    print("Kokonaishinta: ", keitto * 5.90)
    print ("Seuraava kiitos!")

else:
    print("Seuraava kiitos!")

