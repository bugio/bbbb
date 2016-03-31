dna_text = open("dna.txt").read()

#lasje
lasje_crni = "CCAGCAATCGC"
lasje_rjavi = "GCCAGTGCCG"
lasje_korencek = "TTAGCTATCGC"

#oblika obraza
obraz_kvadraten = "GCCACGG"
obraz_okrogel = "ACCACAA"
obraz_ovalen = "AGGCCTCA"

#barva oci
oci_modre = "TTGTGGTGGC"
oci_zelene = "GGGAGGTGGC"
oci_rjave = "AAGTAGTGAC"

#spol
spol_moski = "TGCAGGAACTTC"
spol_zenski = "TGAAGGACCTTC"

#rasa
belec = "AAAACCTCA"
crnec = "CGACTACAG"
azijec = "CGCGGGCCG"

if dna_text.find(lasje_korencek) > -1 and dna_text.find(obraz_okrogel) > -1 and dna_text.find(oci_rjave) > -1 and dna_text.find(spol_moski) > -1:
    print "Zlocin je storil Ziga!"

if dna_text.find(lasje_crni) > -1 and dna_text.find(obraz_ovalen) > -1 and dna_text.find(oci_modre) > -1 and dna_text.find(spol_moski) > -1:
    print "Zlocin je storil Matej!"

if dna_text.find(lasje_rjavi) > -1 and dna_text.find(obraz_kvadraten) > -1 and dna_text.find(oci_zelene)> -1 and dna_text.find(spol_moski) > -1:
    print "Zlocin je storil Miha!"