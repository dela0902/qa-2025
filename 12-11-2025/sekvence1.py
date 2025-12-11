brojevi = range(1,5) # 1, 2, 3, 4
for broj in range(1,5):
    print(broj)
    #   01234
poruka = "Hello"
broj_karaktera = len(poruka)
print(broj_karaktera)
for x in range(0,5):
    print(poruka[x])

for slovo in poruka:
    print(slovo)

#poruka = "Zdravo kako ste"
#print=len(poruka)


#for slovo in poruka:
    #print(slovo)

poruka = "Hello World"
print(poruka.upper())
print(poruka.lower())
print(poruka.capitalize())

brojevi = [3,10,12,7]
for broj in brojevi:
    print(broj)
for x in range(0, len(brojevi)):
    print(x)
korisnicka_imena = ["gost123" ,"petar123", "jovana123"]
for x in range(len(korisnicka_imena)):
    print(korisnicka_imena[x])

#korisnicka_imena[3] = "marko"
korisnicka_imena.append("marko")
print(korisnicka_imena)
korisnicka_imena[1] = "marija"
print(korisnicka_imena)

korisnicka_imena.remove("marija")
print(korisnicka_imena)
korisnicka_imena.pop(0)
print(korisnicka_imena)
del korisnicka_imena[0]
print(korisnicka_imena)

korisnici = ["petar","ana","jovana","adel","nejla"]
for i in range(len(korisnici)):
    print(f"index: {i}, vrijednost: {korisnici[i]}")

for index,vrijednost in enumerate(korisnici):
    print(f"index: {index}, vrijednost: {vrijednost}")
izdvojeni_korisnici = korisnici[1:5]
print(izdvojeni_korisnici)