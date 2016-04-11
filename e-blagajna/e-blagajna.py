cenik_izdelkov = {"banane" : 1.45, "kruh": 1.50 , "mleko": 0.50, "kava": 3.80}

for izdelek in cenik_izdelkov:
    print izdelek, cenik_izdelkov[izdelek]

while True:
    izberi_izdelek = str(raw_input("Izberi izdelek: "))

    if izberi_izdelek in cenik_izdelkov.keys():
        cena = cenik_izdelkov[izberi_izdelek]
        print "Cena izdelka je %s" % (cena)
    else:
        print "Tega izdelka ni."
        break
