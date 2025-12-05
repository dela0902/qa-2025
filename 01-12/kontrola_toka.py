age = 10
#prikazi igru ako ima vise od 13 godina
print(age > 13)
if age > 13: #false
    print("Prikazi sadrzaj")
    print("pokrenuta je igra")

print("prva sledeca linija")    

email_baza = "korisnik@gmail.com"
sifra_baza ="123"

unjeti_email = "korisnik@gmail.com"
unjeta_sifra = "123"

#ispisi uspjesno logovanje ako su ispravni email i sifra
if email_baza == unjeti_email and sifra_baza == unjeta_sifra:
    print("uspjesno logovanje!!!")

brzina_vozila = 80
ogranicenje = 50
urucena_kazna = True

if brzina_vozila > 50:
    if urucena_kazna == True:
        
        print("dodajte kaznene poene")

    print("posaljite kaznu")

#prikazati korisniku uspjesno ili neuspjesno zavisno od ispisanih podataka
if unjeti_email == email_baza and unjeta_sifra == sifra_baza:
    print("uspjesno logovanje")   
else:
    print("neispravni podaci")    

print("izvrsava se u svakom slucaju")


novac_na_racunu = 1200
cijene_proizvoda = 500

# Uspjesna / Neuspjesna
if novac_na_racunu >= cijene_proizvoda:
    print("uspjesna kupovina")
    novac_na_racunu -= cijene_proizvoda
    print(f"novo stanje na racunu: {novac_na_racunu}")
else:
    print("nemate dovoljno novca na racunu.")


#Kanban 
# prikazujemo razlicitu boju taskova i raspored u zavisnosti od dana u nedjelji
dan_u_nedjelji = "ponedjeljak"

if dan_u_nedjelji == "ponedjeljak":
    print("postavi boju na :crveno")
elif dan_u_nedjelji == "utorak":
    print("postavi boju na :zelenu")
elif dan_u_nedjelji == "srijeda":
    print("postavi boju na :zutu")
elif dan_u_nedjelji == "cetvrtak":
    print("postavi boju na:ljubicastu")
else:
    print("postavi boju na:bijelu")

print("izvrsava se u svakom slucaju")
broj = 10
#broj je veci od nule broj je manji od nulr i broj jr jednak nuli
if broj > 0:
    print("broj je veci od 0")
elif broj == 0:
    print("broj je jednak 0")
elif broj < 0:
    print("broj je manji od 0")

pozicija_automobila = 0
pozicija_parkinga = 30
brzina = 10

# a
pozicija_automobila += 10
print(pozicija_automobila)

if pozicija_automobila == pozicija_parkinga:
    print("stigli ste na parking")
else:
    pozicija_automobila += brzina
    if pozicija_automobila == pozicija_parkinga:
         print("stigli ste na parking!")
    else:
        pozicija_automobila += brzina
        if pozicija_automobila == pozicija_parkinga:
            print("stigli ste na parking")

print("izvrsava se u svakom slucaju")
 # dark / light tema
trenutna_tema_na_racunaru = "light" 
# na sajtu primjeni temu u skladu sa temom na racunaru korisnika

odabrana_tema_u_app = ""
#prva mogucnost
if trenutna_tema_na_racunaru == "light":
    odabrana_tema_u_app = "light"
else:
    odabrana_tema_u_app = "dark"
# druga mogucnost-ternarni operator
odabrana_tema_u_app = "light" if trenutna_tema_na_racunaru == "light" else "dark"

unjeti_broj =  int(input("unesite broj: "))

if unjeti_broj % 2 == 0:
    print("broj je paran")
else:
    print("broj je neparan")





