
seznam = []


odg = raw_input("Ali zelite dodati kak izdelek v seznam?: ")
while odg == "Da":
   odg1 = raw_input("Napisite izdelek, ki ga zelite dodati: ")
   seznam.append(odg1)
   odg2 = raw_input("Ali zelite dodati se kak izdelek v seznam?: ")
   if odg2 == "Da":
          odg1 = raw_input ("Napisite izdelek, ki ga zelite dodati: ")
          seznam.append(odg1)
          odg2 = raw_input ("Ali zelite dodati se kak izdelek v seznam?: ")
   else:
       print ("Vas nakup vsebuje: "), seznam
       print ("Hvala za vas nakup!")

else:
   print ("Vas nakup vsebuje: "), seznam
   print ("Hvala za vas nakup!")
