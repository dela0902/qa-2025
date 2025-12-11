#    0,1,2
a = [1,2,3]
b = [4,5,6]

zbir =[]
#print(a+b)nadovezuje liste
for i in range(len(a)):
    zbir.append(a[i]+b[i]) # dodaje clan u listi

print(zbir)
zbir.clear() #uklanja sve clanove liste
print(zbir)

registrovani_korisnici = ["jovana","a n a","x","marijana123"]
ispravna_imena = []

for korisnik in registrovani_korisnici:
    formatirano_ime = korisnik.replace(" ", "")#strip() sa kraja i pocetka uklanja
    if len(formatirano_ime) >=5:
        ispravna_imena.append(formatirano_ime)
    else:
        print(f"neispravno: {korisnik}")
        
print(ispravna_imena)
ispravna_imena.sort()
print(ispravna_imena)

#[5,1,2,7,4]
#[1,2,4,5,7]
#ime korisnika                             poeni
# korisnik,                         test 1, test 2, test 3
#ana                                  85       90      60
#jovana                               75       60      90
korisnik1 = ["ana",85,90,60,55] 
korisnik2 = ["jovana",75,60,90]
#                  0                         1
polaznici = [["ana",85,90,60,55], ["jovana", 75, 60,90]]
#ana= polaznici[0]
#jovana= polaznici[1]
for polaznik in polaznici:
    #print(polaznik)
    for informacija in polaznik:
        print(informacija)
    print("###########")


#print(ana[2])
#print(jovana[1])
#prikazi 85
#polaznici[0][1]
#prikazi 75
#polaznici[1][2]

korpa = [["patike adidas", 15000,1], ["patike nike" , 13000,2]]

print(f"ukupno proizvoda u korpi: {len(korpa)}")
#ispisi detalje clanova korpe
for proizvod in korpa:
    for informacija in proizvod:
        print(informacija)
    print("*************")
