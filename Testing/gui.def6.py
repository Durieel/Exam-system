from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


    
def oversikt_emneres(listbox):
    listbox.bind()
    listbox.delete(0, 'end')
    marker = mydb.cursor()
    emne = emne1.get()

    m_emneres = ('SELECT Studentnr, Dato, Karakter '
                 'FROM Eksamensresultat '
                 'WHERE Emnekode = %s'
                 'ORDER BY Studentnr ASC;' )
    listbox.insert('end', 'Studentnr: Dato: Karakter:')
    d_emneres = (emne)
    
    marker.execute(m_emneres, d_emneres)
    
    for row in marker:
        listbox.insert('end', row)

    marker.close()


def adm_emneres_gui():
    adm_emneres = Toplevel()
    adm_emneres.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_emneres, text="Eksamensresultat i et emne").grid(column=0, columnspan=1, row=0, pady=15, padx=15, sticky='WE')

    ttk.Separator(adm_emneres).grid(row=2, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(adm_emneres, text='Emnekode:').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_emneres, textvariable=emne1, width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Separator(adm_emneres).grid(row=6, column=0, columnspan=1, pady=5, sticky=(W, E))

    ttk.Button(adm_emneres, text='Tilbake', command=adm_emneres.destroy).grid(row=8, column=1, padx=5, pady=5, sticky=E)
    ttk.Separator(adm_emneres).grid(row=9, column=0, columnspan=2, pady=5, sticky=(W, E))

    #Listbox
    listbox = Listbox(adm_emneres, height=15)
    listbox.grid(row=6, column=0, columnspan=4, sticky=(W, E))

    s = ttk.Scrollbar(adm_emneres, orient=VERTICAL, command=listbox.yview)
    s.grid(row=6, column=5, sticky=(N, S, E, W))
    listbox['yscrollcommand'] = s.set
    ttk.Sizegrip().grid(row=6, column=6, sticky=(S, E))
    adm_emneres.grid_columnconfigure(1, weight=1)
    adm_emneres.grid_rowconfigure(1, weight=1)

    ttk.Button(adm_emneres, text='Utfør', command=lambda: oversikt_emneres(listbox)).grid(row=5, column=1, padx=5, pady=5, sticky=W)



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
ttk.Button(mainframe, text="Rom").grid(column=1, row=4, sticky=W)

ttk.Label(mainframe, text="Administrer Eksamener").grid(column=0, row=5, sticky=(E, W))
ttk.Button(mainframe, text="Eksamener").grid(column=1, row=5, sticky=W)

ttk.Label(mainframe, text="Administrer Karakterer").grid(column=0, row=6, sticky=(E, W))
ttk.Button(mainframe, text="Karakterer").grid(column=1, row=6, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=7, columnspan=2, sticky=(W, E))

ttk.Label(mainframe, text="Utskrifter av oversikter").grid(column=0, row=8, sticky=(E, W))
ttk.Button(mainframe, text="Oversikter", command=adm_emneres_gui).grid(column=1, row=8, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=9, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy).grid(column=1, row=10, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(pady=5)



emne1 = StringVar()





root.mainloop()
