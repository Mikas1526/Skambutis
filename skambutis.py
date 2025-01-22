from tkinter import *
from playsound import playsound

def setTimes(adress: str) -> list[dict]:
    """ insert txt document adress in order to load times """
    times = []
    time = {'h': 0, 'min': 0, 'type': 1}
    doc = open(adress)
    for line in doc.readlines():
        line = line.strip().split()
        time['type'] = int(line[0])
        line = line[1].split(':')
        time['h'], time['min'] = int(line[0]), int(line[1])
        times.append(time.copy())
    doc.close()
    return times

def skambutis(bellType: int | None = 1):
    """ play sound """
    match bellType:
        case 1:
            playsound(firstBellFile)
        case 2:
            playsound(secondBellFile)
        case 3:
            playsound(finalBellFile)
        case _:
            playsound(firstBellFile)
        
            

# Global variables
isBellActive = False
timeSettingsFile = 'skambuciuLaikai.txt'
firstBellFile = 'skambutis1.mp3'
secondBellFile = 'skambutis2.mp3'
finalBellFile = 'skambutis2.mp3'
times = []

# Start of GUI
m = Tk()
m.geometry("450x350")
m.title('Mokyklos skambutis')

txtNustatymai = Label(m, text="Nustatymai")
txtNustatymai.grid(row=0, columnspan=3)

Label(m, text='Nustatymai dokumente:').grid(row=1)

entrSetDoc = Entry(m)
entrSetDoc.insert(0, timeSettingsFile)
entrSetDoc.grid(row=1, column=2)

Label(m, text='Įspėjimo skambutis:').grid(row=2)

firstBell = Entry(m)
firstBell.insert(0, firstBellFile)
firstBell.grid(row=2, column=2)

Label(m, text='Pradžios skambutis:').grid(row=3)

secondBell = Entry(m)
secondBell.insert(0, secondBellFile)
secondBell.grid(row=3, column=2)

Label(m, text='Pabaigos skambutis:').grid(row=4)

finalBell = Entry(m)
finalBell.insert(0, finalBellFile)
finalBell.grid(row=4, column=2)

txtAntraste = Label(m, text="Skambutis")
txtAntraste.grid(row=5, columnspan=3)

scrlTimeList = Scrollbar(m)
scrlTimeList.grid(row=6, column=1)
lstBoxTimes = Listbox(m, yscrollcommand=scrlTimeList.set)
times = setTimes(timeSettingsFile)
for t in times:
    lstBoxTimes.insert("end", f'{t["type"]} {t["h"]:02d}.{t["min"]:02d}')
lstBoxTimes.grid(row=6, column=0)
scrlTimeList.config(command=lstBoxTimes.yview)

Button(m, text="Testas", command=lambda: skambutis(2)).grid(row=7)

m.mainloop()
