# Free License of Mikas Alisauskas
# mikas.alisauskas@gmail.com

from datetime import datetime
from tkinter import Button, Tk, Label, Entry, Scrollbar, Listbox, messagebox
import pygame
import json

def setTimes(adress: str) -> list[dict]:
    """Load times from a text file."""
    times = []
    with open(adress) as doc:
        for line in doc.readlines():
            line = line.strip().split()
            time_type = int(line[0])
            if not (0 < time_type < 4):
                messagebox.showwarning("Netinkamas skambučio tipas", f'Skambučio tipo reikšmė "{time_type}" negalima.\nGalimos reikšmės: 1, 2, 3')
                continue
            stamp = line[1]
            times.append({'stamp': stamp, 'type': time_type})
    return times

def skambutis(bellType: int | None = 1):
    """Play sound based on bell type."""
    global firstBellFile, secondBellFile, finalBellFiler
    match bellType:
        case 1: pygame.mixer.music.load(firstBellFile)
        case 2: pygame.mixer.music.load(secondBellFile)
        case 3: pygame.mixer.music.load(finalBellFile)
    pygame.mixer.music.play()

def updateTimeBox():
    """Update the listbox with time schedule."""
    try:
        global times
        times = setTimes(timeSettingsFile)
        lstBoxTimes.delete(0, 'end')
        for t in times:
            lstBoxTimes.insert("end", f'{t["type"]} {t["stamp"]}')
    except FileNotFoundError:
        messagebox.showerror('Error', f"File '{timeSettingsFile}' not found!")

def changeSettings():
    """Change bell settings."""
    global timeSettingsFile, firstBellFile, secondBellFile, finalBellFile, isBellActive
    # getting information from fields
    timeSettingsFile = entrSetDoc.get()
    firstBellFile = firstBell.get()
    secondBellFile = secondBell.get()
    finalBellFile = finalBell.get()

    updateTimeBox()

    # saving to settings file
    json.dump(
        {
            'isBellActive': isBellActive,
            'timeSettingsFile': timeSettingsFile,
            'firstBellFile': firstBellFile,
            'secondBellFile': secondBellFile,
            'finalBellFile': finalBellFile,
        },
        open('settings.json', 'w')
    )

played_alarms = set()  # Track already played alarms

def needSomeNoise(checkTime: str | None = datetime.now().strftime("%H:%M")) -> int | None:
    """Check if sound needs to play."""
    global times, played_alarms
    for t in times:
        if t['stamp'] == checkTime and t['stamp'] not in played_alarms:
            played_alarms.add(t['stamp'])  # Mark as played
            return t['type']
    return None

def periodic_check():
    """Check for alarms periodically."""
    global isBellActive
    if isBellActive:
        current_time = datetime.now().strftime("%H:%M")
        playSoundType = needSomeNoise(current_time)
        if playSoundType is not None:
            skambutis(playSoundType)
    m.after(1000, periodic_check)  # Check every second

def switchActivity():
    """Turns on/off bell activity"""
    global isBellActive, activationButton
    isBellActive = not(isBellActive)
    if isBellActive:
        activationButton.config(text="Aktyvuotas", fg="green")
    else:
        activationButton.config(text="Neaktyvuotas", fg="red")

def loadSettings():
    """ Loads settings of files """
    global isBellActive, timeSettingsFile, firstBellFile, secondBellFile, finalBellFile
    
    settingsFile = open('settings.json')
    settings = json.load(settingsFile)
    
    isBellActive = not(bool(settings['isBellActive']))
    timeSettingsFile = settings['timeSettingsFile']
    firstBellFile = settings['firstBellFile']
    secondBellFile = settings['secondBellFile']
    finalBellFile = settings['finalBellFile']

    settingsFile.close()

# Global variables
isBellActive = None
timeSettingsFile = None
firstBellFile = None
secondBellFile = None
finalBellFile = None
times = []

# loading settings
loadSettings()

# Bell initialization
pygame.mixer.init(buffer=4096)

# Start of GUI
m = Tk()
m.resizable(0, 0)

m.title('Mokyklos skambutis')
Label(m, text="Nustatymai", font=("Arial", 12, "bold")).grid(row=0, columnspan=3)

Label(m, text='Tvarkaraštis:').grid(row=1)
entrSetDoc = Entry(m)
entrSetDoc.insert(0, timeSettingsFile)
entrSetDoc.grid(row=1, column=2)

Label(m, text='Pirmasis skambutis:').grid(row=2)
firstBell = Entry(m)
firstBell.insert(0, firstBellFile)
firstBell.grid(row=2, column=2)

Label(m, text='Antrasis skambutis:').grid(row=3)
secondBell = Entry(m)
secondBell.insert(0, secondBellFile)
secondBell.grid(row=3, column=2)

Label(m, text='Pabaigos skambutis:').grid(row=4)
finalBell = Entry(m)
finalBell.insert(0, finalBellFile)
finalBell.grid(row=4, column=2)

Button(m, text="Išsaugoti", command=changeSettings).grid(row=5, column=2)
Label(m, text="Skambutis", font=("Arial", 12, "bold")).grid(row=6, columnspan=3)

scrlTimeList = Scrollbar(m)
scrlTimeList.grid(row=7, column=1)
lstBoxTimes = Listbox(m, yscrollcommand=scrlTimeList.set)
updateTimeBox()
lstBoxTimes.grid(row=7, column=0)
scrlTimeList.config(command=lstBoxTimes.yview)

Button(m, text="Testas", command=lambda: skambutis()).grid(row=8)
activationButton = Button(m, text="N/a", command=switchActivity)
switchActivity()
activationButton.grid(row=8, column=2)

Label(m, text="Free license\nMikas Ališauskas").grid(row=7, column=2)

# Start periodic check
periodic_check()

# Run the GUI loop
m.mainloop()
