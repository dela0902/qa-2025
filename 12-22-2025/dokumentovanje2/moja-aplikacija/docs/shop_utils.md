# ShoopUtils - modul - dostupan za upotrebu u cijeloj aplikaciji

Ovaj modul sadrzi:

- Klasu ShopUtils, koja u sebi ima metode za:
    - konverziju **RSD -> EUR**
    - konverziju **EUR -> RSD**
    - racunanje **cijene sa porezom**

Primjeri upotrebe:

```python
print(ShooUtils.rsd_to_eur(1170)) # 10.00
```

## Pravila i formule
RSD->EUR
Formula:

- EUR = RSD / EUR_TO_RSD
    -Primjer: 1170 / 117 = 10.00

EUR -> RSD

Formula:


-RSD = EUR * EUR_TO_RSD
    -Primjer: 10* 117 = 1170.00

## Pravila upotrebe - API
ShopUtils.rsd_to_eur(rsd)

- Ulaz mora biti > 0
- Rezultat je zaokruzen na dve decimale

ShopUtils.eur_to_rsd(eur)

- Ulaz mora biti > 0
- Rezultat je zaokruzen na dvije decimale

Kurs je preuzet sa :
[NBS](https://www.nbs.rs/sr_RS/indeks/)

