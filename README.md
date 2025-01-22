# Mokyklos skambutis
# Tvarkaraštis
Įjungus programą pakraunami laikai iš nurodyto tekstinio dokumento laukelyje `Tvarkaraštis`. Tekstinis dokumentas pateikiamas tokiu pavidalu:
kiekvienoje eilutėje užrašoma, kelinto skambučio norima tuo metu, tarpas, dvitaškiu atskirta valanda ir minutė. Valandos ir minutės formatas rekomenduojamas toks `00:00`.
# Garsas
Pirmo, antro ir pabaigos skambučio garsas gali būti paleistas iš `.mp3`, `.wav` ir `.ogg`
# Nustatymai
Pakeitus dokumento pavadinimą, reikia spustelti mygtuką `Išsaugoti`, kad pakeitimai būtų įgyvendinti.
# Aktyvavymas
Paleidus programą, skambutis yra išjungtas. Norint jį įjungti, reikia spustelti mygtuką `Neaktyvuotas`, kad mygtuko tekstas pasikeistų į `Aktyvuotas`. Norint sustabdyti veikimą, reikia dar kartą tą patį mygtuką paspausti.
# Įrašymas
1. Privalomas [Python](https://www.python.org/downloads/) branduolys suinstaliuotas kompiuteryje.
2. Turi būti suinstaliuotos PIP pagalba bibliotekos `tkinter` ir `playsound`.
3. Nukopijuojama ši repozitorija ir paleidžiama programa su komanda
    ```python
    python3 skambutis.py
    ```