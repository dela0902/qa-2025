# Bankomat modul

Omogucava korisniku interakciju sa bankovnim racunom

![bankomat_slika](https://img.freepik.com/premium-vector/set-realistic-atm-machine-isolated-atm-bank-cash-machine-with-interface-keypad-slot-card_320857-1122.jpg?w=360)

# Metod za podizanje novca
Ulazni parametri:
- Iznos

Povratna vrijednost:
- True / False - u zavisnosti od uspjesnosti
`     def podigni_novac(self, iznos):
        if iznos >= self.stanje:
            self.stanje -= iznos
            return True
        return False`

## Scenarij
### Podizanje novca - uspjesan slucaj
- Pocetno stanje: 10.000
- Zahtjev za podizanje: 2.000
- Ocekivani rezultat:
    - Transakcija uspjesna (True)
    - Novo stanje: 8.000

## Kodovi gresaka

| Kod | Opis |
|-----|------|
| E001| Nedovoljno sredstava |
| E002| Nevalidan iznos |
| E003| Nedovoljno novca u bankomatu|

    
