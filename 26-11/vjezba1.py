#definisanje telefona iz vjezbe
proizvodjac = "Samsung" #string tip
model = "S25" # string tip
cijena = 800
url_do_slike = "samsung_slika.jpg" 

#print("proizvodjac:",proizvodjac,"Model:",model,"Cijena",cijena)
print(f"Proizvodjac:\t{proizvodjac}\n Model: {model},\n Cijena: {cijena}")
#\t-tab
#\n-novi red
print(cijena + 50)
print(cijena)

cijena = cijena + 50
print(cijena)

cijena = cijena - 30
print(cijena)

popust = 0.2
umanjenje = cijena * 0.2
cijena = cijena - umanjenje
print(cijena)

cijena_bez_popusta = 800
print(int(cijena_bez_popusta / 2))

#dijeljenje bez ostatka //
print(25 // 2)

#stepenovanje **
print(8**3)
print(2**2)

# celobrojni ostatak pri djeljenju %
print(10 % 3) # 3* 3 = 9 +1 =10

#u ovom primjeru cemo da trazimo od korisnika brpj i provjeravamo da li je paran broj

unjeti_broj = int (input("Unesite  broj: "))
# print(unijeti_broj + 50)
# provjeravam da li je unijeti broj paran broj
print(unjeti_broj % 2) #ostatak pri djeljenju sa 2
# broj je paran ako je ostatak pri djeljenju sa 2 jednak 0
# == True / False
ostatak_pri_dijeljenju_sa_dva = unjeti_broj % 2
print(ostatak_pri_dijeljenju_sa_dva == 0 )
broj_je_paran = ostatak_pri_dijeljenju_sa_dva == 0 # true / False
print(broj_je_paran)

# teest plan
# test_broj 15
# ocekivano - nije paran - Rezultat: False
ocekivano = False
print("Test je prosao:",broj_je_paran == ocekivano)

#test slucaj za parne
# test_broj 16
#ocekivano - da je paran - rezultat: True
ocekivano_2 = True
print("test je prosao: ", broj_je_paran == ocekivano_2)

# Opis buga
# provjera da li je broj paran
# Reprodukcija buga:
# 1.unijeti broj 16
# 2.klik na enter
# Dobijeno: False - da broj nije paran
# Ocekivano: True - broj je paran