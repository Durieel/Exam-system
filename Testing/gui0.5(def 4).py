from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def add_eksres():

    marker = mydb.cursor()

    studentnr = studentnr1.get()
    emnekode = emne1.get()
    dato = dato1.get()
    karakter = karakter1.get()


    m_eksres = ('INSERT INTO Eksamensresultat'
             '(Studentnr, Emnekode, Dato, Karakter)'
             'VALUES(%s, %s, %s, %s)')
    d_eksres = (studentnr, emnekode, dato, karakter)

    marker.execute(m_eksres, d_eksres)
    mydb.commit()

    marker.close()




def adm_eksres_gui():
    adm_eksres = Toplevel()
    adm_eksres.title('Eksamensadministrasjonsapplikasjon')

    p = ttk.Panedwindow(adm_eksres, orient=VERTICAL)
    p.grid(row=1, column=0, columnspan=2, rowspan=2, padx=20, sticky=W)
    l1 = ttk.Labelframe(p, text='Info', width=50, height=100)
    p.add(l1)
    l = Label(l1, text="Fyll inn alle feltene med \n"
                       "riktig informasjon om    \n "
                       "eksamen, og klikk                \n"
                       "'Legg til eksamensresultat'               ")
    l.grid(row=0, column=0)

    ttk.Label(adm_eksres, text="Administrering av Eksamensresultat").grid(column=0, columnspan=1, row=0, pady=15, padx=15, sticky='WE')

    ttk.Label(adm_eksres, text='Emnekode:').grid(row=1, column=1, padx=10, pady=5, sticky=W)
    ttk.Entry(adm_eksres, textvariable=emne1, width=15).grid(row=1, column=2, padx=0, pady=5, sticky=W)

    ttk.Label(adm_eksres, text='Dato:').grid(row=2, column=1, padx=10, pady=5, sticky=W)
    ttk.Entry(adm_eksres, textvariable=dato1, width=15).grid(row=2, column=2, padx=0, pady=5, sticky=W)

    ttk.Separator(adm_eksres).grid(row=4, column=0, columnspan=5, pady=5, sticky=(W, E))

    ttk.Label(adm_eksres, text='Studentnr:').grid(row=5, column=0, padx=2, pady=5, sticky=W)
    ttk.Entry(adm_eksres, textvariable=studentnr1, width=10).grid(row=5, column=0, padx=0, pady=5)

    ttk.Label(adm_eksres, text='Karakter:').grid(row=6, column=0, padx=2, pady=5, sticky=W)
    ttk.Entry(adm_eksres, textvariable=karakter1, width=10).grid(row=6, column=0, padx=0, pady=5)

    ttk.Separator(adm_eksres).grid(row=7, column=0, columnspan=5, pady=5, sticky=(W, E))

    ttk.Button(adm_eksres, text='Legg til eksamensresultat', command=add_eksres).grid(row=8, column=0, padx=5, pady=5, sticky=W)
    ttk.Button(adm_eksres, text='Tilbake', command=adm_eksres.destroy).grid(row=8, column=2, padx=5, pady=5, sticky=E)
    ttk.Separator(adm_eksres).grid(row=9, column=0, columnspan=5, pady=5, sticky=(W, E))
    




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
ttk.Button(mainframe, text="Eksamener", command=adm_eksres_gui).grid(column=1, row=5, sticky=W)

ttk.Label(mainframe, text="Administrer Karakterer").grid(column=0, row=6, sticky=(E, W))
ttk.Button(mainframe, text="Karakterer").grid(column=1, row=6, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=7, columnspan=2, sticky=(W, E))

ttk.Label(mainframe, text="Utskrifter av oversikter").grid(column=0, row=8, sticky=(E, W))
ttk.Button(mainframe, text="Oversikter").grid(column=1, row=8, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=9, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy).grid(column=1, row=10, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(pady=5)



studentnr1 = StringVar()
emne1 = StringVar()
dato1 = StringVar()
karakter1 = StringVar()




root.mainloop()
