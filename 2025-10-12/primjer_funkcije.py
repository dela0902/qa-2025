# igrac,ukupan broj poena, ukupan broj utakmica
igraci =[{"prezime": "jokic", "poeni":100, "ukupan_broj_utakmica":10}]
[{"prezime": "gordon", "poeni":20, "ukupan_broj_utakmica":11}]
[{"prezime": "saric", "poeni":50, "ukupan_broj_utakmica":12}]

def izracunaj_prosjek_poena(broj_poena, ukupno_utakmica):
    rezultat=broj_poena / ukupno_utakmica
    return rezultat

for igrac in igraci:
    print(f"igrac: {igrac["prezime"]}")
    print(izracunaj_prosjek_poena(igrac["poeni"],igrac["ukupan_broj_utakmica"]))

#Testiranje funkcije sa izracunavanjem prosjeka
#test podaci
broj_poena_test = 50
ukupno_utakmica_test = 100
ocekivano = 5

dobijeno = izracunaj_prosjek_poena(broj_poena_test, ukupno_utakmica_test)
print(ocekivano== dobijeno)
def test_prosjeka_poena(broj_poena, ukupno_utakmica, ocekivano):
    dobijeno = izracunaj_prosjek_poena(broj_poena, ukupno_utakmica)
    print(ocekivano== dobijeno)

    test_prosao = ocekivano == dobijeno
    return test_prosao
