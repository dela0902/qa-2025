moji_oglasi = []
oglas1 = {
    "naziv": "patike",
    "cijena": 150,
    "opis": "patike na prodaju"
}

moji_oglasi.append(oglas1)

oglas2 ={
    "naziv": "patike",
    "cijena": -50,
    "opis": "patike na prodaju"
}
moji_oglasi.append(oglas2)

print(moji_oglasi)

for oglas in moji_oglasi:
     print(f"naziv: {oglas["naziv"]}")
     print(f"cijena: {oglas["cijena"]}")
     print(f"opis: {oglas["opis"]}")

     cijena = oglas["cijena"]
     if cijena < 0:
          print(f"oglas sa nazivom {oglas["naziv"]} ima negativnu cijenu!!!")