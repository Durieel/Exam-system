from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def add_rom():

    marker = mydb.cursor()

    romnr = romnr1.get()
    antallplasser = antallplasser1.get()


    m_rom = ('INSERT INTO Rom'
             '(Romnr, Antallplasser)'
             'VALUES(%s, %s)')
    d_rom = (romnr, antallplasser)

    marker.execute(m_rom, d_rom)
    mydb.commit()

    marker.close()

    
def oversikt_rom(listbox):
    listbox.bind()
    listbox.delete(0, 'end')
    marker = mydb.cursor()

    marker.execute(
        'SELECT * '
        'FROM Rom ' )
    listbox.insert('end', 'Romnr: Antallplasser:')

    for row in marker:
        listbox.insert('end', row)

    marker.close()


def adm_rom_gui():
    adm_rom = Toplevel()
    adm_rom.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_rom, text="Administrering av Rom").grid(column=0, columnspan=1, row=0, pady=15, padx=15, sticky='WE')

    ttk.Separator(adm_rom).grid(row=2, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(adm_rom, text='RomNr:').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_rom, textvariable=romnr1, width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(adm_rom, text='AntallPlasser:').grid(row=4, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_rom, textvariable=antallplasser1, width=15).grid(row=4, column=1, padx=5, pady=5, sticky=W)

    ttk.Separator(adm_rom).grid(row=6, column=0, columnspan=1, pady=5, sticky=(W, E))

    ttk.Button(adm_rom, text='Legg til rom', command=add_rom).grid(row=8, column=0, padx=5, pady=5, sticky=W)
    ttk.Button(adm_rom, text='Tilbake', command=adm_rom.destroy).grid(row=8, column=1, padx=5, pady=5, sticky=E)
    ttk.Separator(adm_rom).grid(row=9, column=0, columnspan=2, pady=5, sticky=(W, E))

    listbox = Listbox(adm_rom, height=15)
    listbox.grid(row=6, column=0, columnspan=4, sticky=(W, E))

    s = ttk.Scrollbar(adm_rom, orient=VERTICAL, command=listbox.yview)
    s.grid(row=6, column=5, sticky=(N, S, E, W))
    listbox['yscrollcommand'] = s.set
    ttk.Sizegrip().grid(row=6, column=6, sticky=(S, E))
    adm_rom.grid_columnconfigure(1, weight=1)
    adm_rom.grid_rowconfigure(1, weight=1)

    ttk.Label(adm_rom, text="Oversikt av rom:").grid(row=5, column=0, padx=5, pady=5, sticky=W)
    ttk.Button(adm_rom, text='Klikk her', command=lambda: oversikt_rom(listbox)).grid(row=5, column=1, padx=5, pady=5, sticky=W)



mydb = pymysql.connect(host='localhost', port=3306, user='Eksamenssjef', passwd='eksamen2017', db='Eksamen')

root = Tk()
root.title("Eksamensapplikasjon")
mainframe = ttk.Frame(root, padding="6 6 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)



ttk.Label(mainframe, text="Administrering av eksamen ved HSN").grid(column=0, row=0, sticky=(W, E))
ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=1, columnspan=2, sticky=(W, E))

ttk.Label(mainframe, text="Administrer Studenter").grid(column=0, row=2, sticky=(E, W))
ttk.Button(mainframe, text="Studenter").grid(column=1, row=2, sticky=W)

ttk.Label(mainframe, text="Administrer Emner").grid(column=0, row=3, sticky=(E, W))
ttk.Button(mainframe, text="Emner").grid(column=1, row=3, sticky=W)

ttk.Label(mainframe, text="Administrer Rom").grid(column=0, row=4, sticky=(E, W))
ttk.Button(mainframe, text="Rom", command=adm_rom_gui).grid(column=1, row=4, sticky=W)

ttk.Label(mainframe, text="Administrer Eksamener").grid(column=0, row=5, sticky=(E, W))
ttk.Button(mainframe, text="Eksamener").grid(column=1, row=5, sticky=W)

ttk.Label(mainframe, text="Administrer Karakterer").grid(column=0, row=6, sticky=(E, W))
ttk.Button(mainframe, text="Karakterer").grid(column=1, row=6, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=7, columnspan=2, sticky=(W, E))

ttk.Label(mainframe, text="Utskrifter av oversikter").grid(column=0, row=8, sticky=(E, W))
ttk.Button(mainframe, text="Oversikter").grid(column=1, row=8, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=9, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy).grid(column=1, row=10, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(pady=5)



romnr1 = StringVar()
antallplasser1 = StringVar()




root.mainloop()
