# Mokyklos skambutis
# Tvarkaraštis
Įjungus programą pakraunami laikai iš nurodyto tekstinio dokumento laukelyje `Tvarkaraštis`. Tekstinis dokumentas pateikiamas tokiu pavidalu:
kiekvienoje eilutėje užrašoma, kelinto skambučio norima tuo metu, tarpas, dvitaškiu atskirta valanda ir minutė. Valandos ir minutės formatas toks `00:00`.
# Garsas
Pirmo, antro ir pabaigos skambučio garsas gali būti paleistas iš `.mp3`, `.wav` ir `.ogg`
# Nustatymai
Pakeitus dokumento (-ų) pavadinimą (-us) arba norint atnaujinti laikus, reikia spustelti mygtuką `Išsaugoti`, kad pakeitimai būtų įrašyti ir jais programa remtųsi.
# Aktyvavimas
Paleidus programą, skambutis bus arba įjungtas arba ne, priklausomai nuo paskutinio išsaugojimo. Norint jį įjungti, reikia spustelti mygtuką `Neaktyvuotas`, kad mygtuko tekstas pasikeistų į `Aktyvuotas`. Norint sustabdyti veikimą, reikia dar kartą tą patį mygtuką paspausti.
# Diegimas
1. Privalomas [Python](https://www.python.org/downloads/) branduolys suinstaliuotas kompiuteryje.
2. Turi būti suinstaliuotos PIP pagalba bibliotekos `tkinter` ir `playsound`.
3. Nukopijuojama ši repozitorija ir paleidžiama programa su komanda
    ```python
    python3 skambutis.py
    ```