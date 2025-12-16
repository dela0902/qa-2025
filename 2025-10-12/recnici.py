poruke = ["zdravo", "Hello", "Hallo"]
print(poruke[0])

poruke1 = {"sr":"Zdravo", "en":"Hello", "de":"Hallo"}
print(poruke1["sr"])
poruke1["sr"] = "Dobar dan"
print(poruke1)

poruke2 = {}
# temperatura,grad,padavine da/ne
vremenska_prognoza = {"temperature": 10,"city":"beograd", "padavine":True}
#print(f"temperatura: {vremenska_prognoza["temperatura"]}")
#print(f"Grad: {vremenska_prognoza["grad"]}")
#print(f"padavine: {vremenska_prognoza['padavine']}")
for kljuc,vrijednost in vremenska_prognoza.items():
    print(kljuc,vrijednost)

dogovoreni_kljucevi = ["temperatura","grad","padavine"]
for kljuc in dogovoreni_kljucevi:
    if kljuc in vremenska_prognoza:
        print(f"kljuc {kljuc} je OK")
    else:
        print(f"kljuc {kljuc} nije pronadjen!!!")


proizvodi ={
    "naziv": "patike",
    "cijena":{
        "vrijednost":200,"valuta":"EUR"},
     "slike":["slika1.png","slika2.png"]}
print(proizvodi["naziv"])
informacije_o_cijeni = proizvodi["cijena"]
print(informacije_o_cijeni)
print(informacije_o_cijeni["vrijednost"])
print(informacije_o_cijeni["valuta"])
lista_slika = proizvodi["slike"]
print(lista_slika)
for slika in lista_slika:
    print(f"slika: {slika}")

proizvodi ={
    "naziv": "patike",
    "cijena":{
        "vrijednost":200,
        "valuta":"EUR"},
     "slike":["slika1.png","slika2.png"]}
{
    "naziv": "Majica",
    "cijena":{
        "vrijednost":20,
        "valuta":"EUR"},
     "slike":["slika1.png","slika2.png"]}

print(len(proizvodi))
for proizvod in proizvodi:
    cijena = proizvodi["cijena"]
    vrijednost_cijene = cijena["vrijednost"]
    valuta = cijena["valuta"]
    print(f"Naziv: {proizvodi["naziv"]}/nCijena: {vrijednost_cijene} {valuta}")
    print("___________")

kurs = {
    "naziv":"intro to Software Development",
    "trajanje":60,
    "lekcije":["Uvod u programiranje",
           "Jira",
           "Git"
           ]
    }   
#print(kurs["naziv"])
#print(kurs["trajanje"])
#lekcije = kurs["lekcije"]
#for lekcije in lekcije:
    #print(lekcije)

obavezni_kljucevi_za_kurs = ["naziv", "trajanje", "lekcije"]
for kljuc in obavezni_kljucevi_za_kurs:
    if not kljuc in kurs:
        print(f"Nedostaje obavezan kljuc: {kljuc}")

skup = {"Python", "QA", "Mobilno programiranje"}
skup.add("Web programiranje")
print(skup)
skup.remove("web programiranje")
for element in skup:
    print(element)

