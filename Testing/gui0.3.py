from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql



def add_emne():
    # Oppretter en cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    emnekode = emnekode_1.get()
    emnenavn = emnenavn_1.get()
    studiepoeng = studiepoeng_1.get()

    # Setter opp database strukturen for tabellen
    m_stud = ('INSERT INTO Emne'
              '(Emnekode, Emnenavn, Studiepoeng)'
              'VALUES(%s, %s, %s)')
    d_stud = (emnekode, emnenavn, studiepoeng)

    # Legger strengene inn i databasen
    marker.execute(m_stud, d_stud)
    mydb.commit()

    # Lukker cursor
    marker.close()

def adm_kara_gui():
    # Oppretter en toplevel-frame
    adm_kara = Toplevel()
    adm_kara.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_kara, text='Karakterstatistikk/utskrift').grid(column=0, columnspan=3, row=0, pady=15, padx=15, sticky='WE')

    global listbox
    listbox = Listbox(adm_kara, height=15)
    listbox.grid(row=2, column=0, columnspan=5, sticky=(W, E))

    s = ttk.Scrollbar(adm_kara, orient=VERTICAL, command=listbox.yview)
    s.grid(row=2, column=5, sticky=(N, S, E, W))
    listbox['yscrollcommand'] = s.set
    ttk.Sizegrip().grid(row=2, column=5, sticky=(S, E))
    adm_kara.grid_columnconfigure(1, weight=1)
    adm_kara.grid_rowconfigure(1, weight=1)

    # Lager button som legger inn strengene i databasen
    ttk.Button(adm_kara, text='Legg til emne', command=adm_kara).grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky=W)
    ttk.Separator(adm_kara).grid(row=8, column=0, columnspan=5, pady=5, sticky=(W, E))

    # Lager button som gjør at brukeren kan gå tilbake til hovedmeny
    ttk.Button(adm_kara, text='Gå tilbake', command=adm_kara.destroy).grid(row=9, column=4, padx=5, pady=5, sticky=E)
    ttk.Separator(adm_kara).grid(row=10, column=0, columnspan=8, pady=5, sticky=(W, E))

def adm_emne_gui():
    # Oppretter en toplevel-frame
    adm_emne = Toplevel()
    adm_emne.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_emne, text="Administrering av Emne").grid(column=0, columnspan=8, row=0, pady=15, padx=15, sticky='WE')
    ttk.Separator(adm_emne).grid(row=2, column=0, columnspan=8, pady=5, sticky=(W, E))

    #Lager en infoboks som skal gi informasjon til brukeren
    p = ttk.Panedwindow(adm_emne, orient=VERTICAL)
    p.grid(row=3, column=3, columnspan=3, rowspan=4, padx=20)
    l1 = ttk.Labelframe(p, text='Info', width=125, height=100)
    p.add(l1)
    l = Label(l1, text="Fyll inn alle feltene med \n"
                       "riktig informasjon om \n "
                       "emnet, og klikk \n"
                       "'Legg til emne'")
    l.grid(row=0, column=0)

    # Lables og Entries for administrasjon av emne
    ttk.Label(adm_emne, text='Emnekode:').grid(row=3, column=0, padx=5, pady=10, sticky=W)
    ttk.Entry(adm_emne, textvariable=emnekode_1, width=15).grid(row=3, column=1, padx=5, pady=10, sticky=W)

    ttk.Label(adm_emne, text='Emnenavn:').grid(row=4, column=0, padx=5, pady=10, sticky=W)
    ttk.Entry(adm_emne, textvariable=emnenavn_1, width=15).grid(row=4, column=1, padx=5, pady=10, sticky=W)

    ttk.Label(adm_emne, text='Studiepoeng:').grid(row=5, column=0, padx=5, pady=10, sticky=W)
    ttk.Entry(adm_emne, textvariable=studiepoeng_1, width=8).grid(row=5, column=1, padx=5, pady=10, sticky=W)

    ttk.Separator(adm_emne).grid(row=6, column=0, columnspan=8, pady=5, sticky=(W, E))

    #Lager button som legger inn strengene i databasen
    ttk.Button(adm_emne, text='Legg til emne', command=add_emne).grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky=W)
    ttk.Separator(adm_emne).grid(row=8, column=0, columnspan=8, pady=5, sticky=(W, E))

    #Lager button som gjør at brukeren kan gå tilbake til hovedmeny
    ttk.Button(adm_emne, text='Gå tilbake', command=adm_emne.destroy).grid(row=9, column=4, padx=5, pady=5, sticky=E)
    ttk.Separator(adm_emne).grid(row=10, column=0, columnspan=8, pady=5, sticky=(W, E))



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
ttk.Button(mainframe, text="Emner", command=adm_emne_gui).grid(column=1, row=3, sticky=W)

ttk.Label(mainframe, text="Administrer Rom").grid(column=0, row=4, sticky=(E, W))
ttk.Button(mainframe, text="Rom").grid(column=1, row=4, sticky=W)

ttk.Label(mainframe, text="Administrer Eksamener").grid(column=0, row=5, sticky=(E, W))
ttk.Button(mainframe, text="Eksamener").grid(column=1, row=5, sticky=W)

ttk.Label(mainframe, text="Administrer Karakterer").grid(column=0, row=6, sticky=(E, W))
ttk.Button(mainframe, text="Karakterer", command=adm_kara_gui).grid(column=1, row=6, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=7, columnspan=2, sticky=(W, E))

ttk.Label(mainframe, text="Utskrifter av oversikter").grid(column=0, row=8, sticky=(E, W))
ttk.Button(mainframe, text="Oversikter").grid(column=1, row=8, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=9, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy).grid(column=1, row=10, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(pady=5)


emnekode_1 = StringVar()
emnenavn_1 = StringVar()
studiepoeng_1 = StringVar()




root.mainloop()
