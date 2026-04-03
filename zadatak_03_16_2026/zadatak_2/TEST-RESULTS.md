# TEST RESULTS

## Valid inputs

Input: 4+5  
Expected: 9  
Result: OK

Input: 10+5*4  
Expected: 30  
Result: OK

Input: 10+5*4+3  
Expected: 33  
Result: OK

---

## Edge cases

Input: 5/0  
Expected: Error (division by zero)  
Result: Program crashes / no validation

Input: +5  
Expected: Error  
Result: Program nevalidno ponašanje

Input: 5+  
Expected: Error  
Result: Program nevalidno ponašanje

Input: 5++5  
Expected: Error  
Result: Program prihvata nevalidan izraz

---

## Invalid inputs

Input: abc  
Expected: Error  
Result: Nema validacije inputa

Input: 5+a  
Expected: Error  
Result: Program ne obrađuje slova

---

## Observations

- Nema validacije korisničkog unosa
- Program može pasti na neispravnim izrazima
- Nije obrađena greška dijeljenja sa nulom
- Nema poruka o grešci korisniku