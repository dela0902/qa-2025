
def ispisi_poruku(korisnicko_ime="gost"): #funkcija sa opcionim parametrom
    print(f"Zdravo {korisnicko_ime}!!!!")

#print(korisnicko_ime) ne postoji izvan tijela funkcije
ispisi_poruku("Admin")
ispisi_poruku()
#def saberi(prvi_sabirak=0, drugi_sabirak=0):
   # print(prvi_sabirak+drugi_sabirak)


#saberi(prvi_sabirak=10,drugi_sabirak= 20)


def dodaj_oglas(naziv, cijena, dodatne_informacije=""):
    print(f"Naziv: {naziv}")
    print(f"cijena: {cijena}")
    if dodatne_informacije != "":
        print(f"dodate info: {dodatne_informacije}")


dodaj_oglas("patike", 200)
dodaj_oglas("Automobil",5000,"u odlicnom stanju")
dodaj_oglas(cijena=500,naziv="slusalice", dodatne_informacije="informacije....")

brojevi =[5,3,4]
broj_clanova=len(brojevi)
print(broj_clanova)

def pomnozi(broj1, broj2):
    rezultat =broj1*broj2
    return rezultat
    #print("pozdrav iz funkcije za mnozenje") ovo se nikada nece izvrsiti
rezultat_mnozenja = pomnozi(5,3)
print(rezultat_mnozenja)
