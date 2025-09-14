kuha = float(input("Onko kuhasi alamittainen? Anna kuhan pituus senttimetreinä: ", ))
pituus = kuha-37

if kuha >= 37:
    print("Mahtavan kokoinen vonkale, jonka voit pitää!")
elif kuha <37:
    print("Sinun kuhasi on alamittainen! Vähimmäispituus on 37cm. ")
    print("Kuhasi on", pituus,"cm liian lyhyt.", "Laske kuha heti takaisin järveen!")

