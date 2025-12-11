import random
tajmer = 5

while tajmer > 0:
    print(tajmer)
    tajmer -= 1

broj_pokusaja = 3

while broj_pokusaja > 0:
    print("saljem zahtjev za podatke")
    podaci = "dobijeni podaci"
    if podaci != "":
        print("napustam petlju")
        break
    else:
         broj_pokusaja -= 1

#stampati samo parne brojeve - simulacija continue
for broj in range(1,10):
    if broj % 2 != 0:
        continue

    print(broj)

gorivo = 40
#potrosnja = 5

while gorivo > 0:
    print("voznja u toku")
    gorivo -= random.randint(6,15)

#unesi x za zavrsetak,pritisni enter "" unesi za prikaz rezultata
    suma = 0
    while True:
        vrijednost = input("unesite broj:")

        if vrijednost == "":
            print("Suma:", suma)
            suma = 0
        else:
            if vrijednost == "x":
                print("zavrsavam program")
                break
            else:
                if vrijednost.isnumeric():
                     suma += int(vrijednost)
                else:
                    print("molim unesite samo brojeve.")

