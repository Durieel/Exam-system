from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


def utskrift_karstat(tree):

    tree.bind()
    for i in tree.get_children():
        tree.delete(str(i))
    marker = mydb.cursor()
    dato = dato1.get()
    emnekode = emne1.get()

    m_karstat =   (
                   'SELECT Emnenavn, Karakter, count(*) '
                   'FROM eksamensresultat, Emne '
                   'WHERE dato=%s '
                   'AND eksamensresultat.emnekode=%s '
                   'AND eksamensresultat.emnekode=emne.emnekode '
                   'GROUP BY karakter; '
                   )
    d_karstat = (dato, emnekode)


    marker.execute(m_karstat, d_karstat)
    
    teller = 0  # Teller som holder styr på første kolonne
    for row in marker:
        tree.insert('', 'end', text=str(teller), values=(row[0], row[1], row[2]))
        teller += 1  # Øking for hver gjennomgang

    marker.close()

    


def adm_karstat_gui():
    adm_karstat = Toplevel()
    adm_karstat.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_karstat, text='Karakterstatistikk eksamen').grid(column=0, columnspan=1, row=0, pady=15, padx=15, sticky='WE')

    ttk.Separator(adm_karstat).grid(row=2, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(adm_karstat, text='Emnekode:').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_karstat, textvariable=emne1, width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(adm_karstat, text='Dato:').grid(row=4, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_karstat, textvariable=dato1, width=15).grid(row=4, column=1, padx=5, pady=5, sticky=W)


    tree = ttk.Treeview(adm_karstat)

    tree["columns"] = ("1", "2", "3")
    tree.column("#0", anchor="w", width=0)
    tree.column("#1", width=100)
    tree.column("#2", width=100)
    tree.column("#3", width=100)
    tree.heading("#1", text="Emnenavn")
    tree.heading("#2", text="Karakter")
    tree.heading("#3", text="Antall")
    

    ysb = ttk.Scrollbar(adm_karstat, orient=VERTICAL, command=tree.yview)

    tree['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree.grid(row=6, column=0, columnspan=3, pady=7, sticky=NSEW)
    ysb.grid(row=6, column=4, pady=7, sticky=NS)

    
    ttk.Button(adm_karstat, text='Karakterstatistikk', command=lambda: utskrift_karstat(tree)).grid(row=8, column=0, padx=5,
                                                                                          pady=5, sticky=W)
    ttk.Button(adm_karstat, text='Tilbake', command=adm_karstat.destroy).grid(row=8, column=2, padx=5, pady=5, sticky=E)
    ttk.Separator(adm_karstat).grid(row=9, column=0, columnspan=2, pady=5, sticky=(W, E))




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
ttk.Button(mainframe, text="Oversikter", command=adm_karstat_gui).grid(column=1, row=8, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=9, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy).grid(column=1, row=10, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(pady=5)


emne1 = StringVar()
dato1 = StringVar()






root.mainloop()
