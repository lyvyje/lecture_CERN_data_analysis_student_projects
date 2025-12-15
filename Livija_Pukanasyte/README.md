2seku_viename_faile_entropija :

Kad veiktų failas, reikia į " with open("file.txt", "r") as file: " "file.txt" vietą parašyti savo failo pavadinimą. 
PASTABA: faile turi būti tik dvi fasta formato sekos, kadangi Needleman-Wunsch algoritmas geba sulygiuoti tik dvi sekas. :<

Pirma sutvarkome dokumentą: pašaliname simbolius, kurie nėra >,A,T,G,C, pakeičiame pasikartojančius ">" į viena ">" ir pašaliname tuščius tarpus. 

Tuomet ties ">" simbolius perkertame stringą į 2 substringus. Nuo čia pitonas turėtų atpažinti, kad čia yra jau dvi atskiros sekos.

Tada mūsų substringus sutalpiname į biblioteką ir suteikiame jiems kintamuosius. Kiekvieną kartą, kai mums reikia mūsų substringų, mes pirma pakviečiame kintamuosius, kad ištraukti iš bibliotekos ir juos panaudoti (šis procesas sulėtina kodą).

Tada prasideda Needleman-Wunsch sekų sulygiavimas. Tai reiškia, kad mes sekas norima sulyginti. Jei sekos yra nevienodo dydžio, atitinkamuose tarpuose yra įstatomi "-". "-" simboliai ignoruojami ir neprisideda prie entropijos.
Needleman-Wunsch skaičiavimai pasitelkia matricomis. Kiekvieną kartą kai bazės sutampa - +1 ir matrica pasikeičia. Jei nesutampa - -1.

<!-- if __name__ == "__main__": --> Ši vieta pradeda entropijos skaičiavimo dalį ir neleidžia kodui pačiam veikti jį vos atidarius ar įklijavus.

Galiausiai entropijos skaičiavimų dalyje yra suskaičuojama kiekviena bazė (A,T,G,C) ir jai apskaičiuojama entropija pagal Shannon entropijos formulę. 
Jei visų bazių yra vienodai daug, entropija bus didelė. Taip pat entropija didės didėjant genų sekoms.


Seku_atskiruose_failuose_entropija:

Padariau antrą programos variantą, kuriame viename skaičiavime naudojamos sekos iš skirtingų failų. 

Daug kas yra identiška, kaip ir pirmame variante, tačiau čia nereikia atskirti stringo į substringus, reikia tik pašalinti nereikalingus simbolius.
Taip pat kintamuosius (bibliotekos) priskiriame jau tiesiog patiems failams.




