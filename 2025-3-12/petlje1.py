import time
for i in range(5):
    print("Hello", i)
    print("******")
pocetna_godina =2010
krajnja_godina = 2025

for godina in range(pocetna_godina,krajnja_godina):
    print("*******************Allowed years*******")
    print(godina)

print("**********")    

# opseg brojeva do unijetog broja (1, 2,3,4,5) pomnoziti sa 1,2,3
#broj = int(input("unesite broj:"))
#print("1/t2/t3")
#print(20*"*")
#for x in range(1, broj+1):
 #   print(f"{x*1}\t{x*2}\t{x*3}")
 #iscrtati kvadrat
###
###
###
for x in range(3):
    for y in range (3):
        print("#" , end="")
    print()    

sirina =10
visina = 5
#           (0,1,2,3,4)
for x in range(visina):
    for y in range(sirina):
        if x == 0 or x ==  4 or y== 0 or y== 9:
            print("#", end="")
        else:
            print("", end="\r")
    print()

cilj = 20 
trenutna_pozicija =0
trenutna_pozicija * " "

for x in range(cilj):
    print(trenutna_pozicija * " " + "#" , end="\r")
    trenutna_pozicija += 1
    time.sleep(1)





