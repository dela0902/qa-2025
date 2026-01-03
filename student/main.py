class Student:
    def __init__(self, ime, prezime,broj_indexa):
        self.ime = ime
        self.prezime = prezime
        self.broj_indexa = broj_indexa

    def get_info(self):
            return f"Student: {self.ime} {self.prezime} {self.broj_indexa}"
        
class Predmet:
    def __init__(self, naziv):
        self.naziv = naziv

class Ispit(Predmet):
    def __init__(self, naziv, datum_odrzavanja):
        super().__init__(naziv)
        self.datum_odrzavanja = datum_odrzavanja

    def get_info(self):
            return f"Predmet:{self.naziv}, Datum ispita:{self.datum_odrzavanja}"

if __name__== "__main__":
    s = Student("Adel", "Maric","666/66")
    print(s.get_info())
    i = Ispit("Matematika","10.01.2026")
    print(i.get_info())