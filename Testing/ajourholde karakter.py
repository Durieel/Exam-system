from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def upd_karakter():

    marker = mydb.cursor()

    karakter = karakter1.get()
    studentnr = studentnr1.get()
    emnekode = emne1.get()
    

    
    
    m_eks = ('UPDATE eksamensresultat '
             'SET Karakter=%s '
             'WHERE Studentnr=%s '
             'AND Emnekode=%s '
             'ORDER BY dato DESC '
             'LIMIT 1 '
             )

    d_eks = (karakter, studentnr, emnekode)

    marker.execute(m_eks, d_eks)
    mydb.commit()

    marker.close()



    


def adm_kar_gui():
    adm_kar = Toplevel()
    adm_kar.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_kar, text='Administrering av Karakter').grid(column=0, columnspan=1, row=0, pady=15, padx=15, sticky='WE')

    ttk.Separator(adm_kar).grid(row=2, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(adm_kar, text='Studentnr:').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_kar, textvariable=studentnr1, width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(adm_kar, text='Emnekode:').grid(row=4, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_kar, textvariable=emne1, width=15).grid(row=4, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(adm_kar, text='Karakter:').grid(row=5, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_kar, textvariable=karakter1, width=15).grid(row=5, column=1, padx=5, pady=5, sticky=W)

    
    ttk.Button(adm_kar, text='Oppdatere karakter', command=upd_karakter).grid(row=8, column=0, padx=5, pady=5, sticky=W)
    ttk.Button(adm_kar, text='Tilbake', command=adm_kar.destroy).grid(row=8, column=2, padx=5, pady=5, sticky=E)
    ttk.Separator(adm_kar).grid(row=9, column=0, columnspan=2, pady=5, sticky=(W, E))




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
ttk.Button(mainframe, text="Karakterer", command=adm_kar_gui).grid(column=1, row=6, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=7, columnspan=2, sticky=(W, E))

ttk.Label(mainframe, text="Utskrifter av oversikter").grid(column=0, row=8, sticky=(E, W))
ttk.Button(mainframe, text="Oversikter").grid(column=1, row=8, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=9, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy).grid(column=1, row=10, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(pady=5)

# Karakter
studentnr1 = StringVar()
emne1 = StringVar()
karakter1 = StringVar()





root.mainloop()
