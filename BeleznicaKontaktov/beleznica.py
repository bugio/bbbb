print ("Beleznica kontaktov")

class kontakt:
    def __init__(self, ime, priimek, naslov, telefon, email):
        self.ime = ime
        self.priimek = priimek
        self.naslov = naslov
        self.telefon = telefon
        self.email = email

    def polno_ime(self):
        print("Ime in priimek: ", self.ime, self.priimek)

    def podatki(self):
        print("Naslov: ", self.naslov)
        print("Telefon: ", self.telefon)
        print("Email: ", self.email)


seznam_kontaktov= []

while True:
    dodam_kontakt = raw_input("Ali zelite dodati nov kontakt(Da/ Ne): ")
    if dodam_kontakt == "Da":
        nov_kontakt = kontakt(ime = raw_input("Ime: "),
                          priimek = raw_input("Priimek: "),
                          naslov = raw_input("Naslov: "),
                          telefon = raw_input("Telefon: "),
                          email = raw_input("Email: "))

        seznam_kontaktov.append(nov_kontakt)
    else:
        break



for kontakt in seznam_kontaktov:
    print kontakt.polno_ime(), kontakt.podatki()