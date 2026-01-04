class korisnik:
    korisnicko_ime = ""
    sifra = ""
    smjer = ""
    godina_upisa = 0
    ustanova = "ITacademy"
    krediti = 0

    def __init__(self,korisnicko_ime,sifra , smjer,godina_upisa):
        self.korisnicko_ime = korisnicko_ime
        self.sifra = sifra
        self.smjer = smjer 
        self.godina_upisa =godina_upisa

    def promjeni_smjer(self,novi_smjer):
        print("korisnik jee promjenio smjer")
        self.smjer = novi_smjer

    def dodaj_kredite(self,vrijednost):
        self.krediti = vrijednost

    def prikazi_kredite(self):
        return self.krediti


korisnik1 = korisnik("jovana", "123", "QA",2025)
print(korisnik1.korisnicko_ime)
print(korisnik1.sifra)
print(korisnik1.smjer)
print(korisnik1)

print(korisnik1.__dict__)

rijecnik_korisnik = korisnik1.__dict__
for kljuc, vrijednost in rijecnik_korisnik.items():
    print(kljuc, vrijednost)

korisnik1.promjeni_smjer("Python")
print(korisnik1.smjer)

korisnik2 = korisnik("petar", "543", "qa",2025)
korisnik3 = korisnik("marija", "123", "qa",2024)

upisani_qa_korisnici = [korisnik1,korisnik2,korisnik3]

for korisnik in upisani_qa_korisnici:
    if korisnik.godina_upisa == 2025 and korisnik.smjer == "qa":
        print("ocekivano - 2025 qa")
    else:
        print(f"greska - korisnik je smjer : {korisnik.smjer} i godina upisa je: {korisnik.godina_upisa}")

print(korisnik.ustanova)

korisnik1.dodaj_kredite(50)
print(korisnik1.krediti)
print(korisnik2.krediti)
print(korisnik1.prikazi_kredite())