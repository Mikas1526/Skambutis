from tkinter import *
from playsound import playsound

def setTimes(adress: str) -> list[dict]:
    """ insert txt document adress in order to load times """
    times = []
    time = {'h': 0, 'min': 0}
    doc = open(adress)
    for line in doc.readlines():
        line = line.strip().split(':')
        time['h'], time['min'] = int(line[0]), int(line[1])
        times.append(time.copy())
    doc.close()
    return times

def skambutis():
    playsound('drums.wav')

status = {'on': 'aktyvus', 'off': 'neaktyvus'}
timeSettings = 'skambuciuLaikai.txt'
times = []

m = Tk()
m.geometry("300x250")
m.title('Mokyklos skambutis')


Label(m, text='Nustatymai dokumente:').grid(row=0)

entrSetDoc = Entry(m)
entrSetDoc.insert(0, timeSettings)
entrSetDoc.grid(row=0, column=2)

Label(m, text='Įspėjimo skambutis:').grid(row=1)

firstBell = Entry(m)
firstBell.insert(0, timeSettings)
firstBell.grid(row=1, column=2)

Label(m, text='Pradžios skambutis:').grid(row=2)

secondBell = Entry(m)
secondBell.insert(0, timeSettings)
secondBell.grid(row=2, column=2)

Label(m, text='Pabaigos skambutis:').grid(row=3)

finalBell = Entry(m)
finalBell.insert(0, timeSettings)
finalBell.grid(row=3, column=2)

txtAntraste = Label(m, text="Sistemoje įvesti laikai")
txtAntraste.grid(row=4)

scrlTimeList = Scrollbar(m)
scrlTimeList.grid(row=4, column=1)
lstBoxTimes = Listbox(m, yscrollcommand=scrlTimeList.set)
times = setTimes(timeSettings)
for t in times:
    lstBoxTimes.insert("end", f'{t["h"]}.{t["min"]}')
lstBoxTimes.grid(row=4, column=0)
scrlTimeList.config(command=lstBoxTimes.yview)

Button(m, text="Testas", command=skambutis).grid(row=5)

m.mainloop()
