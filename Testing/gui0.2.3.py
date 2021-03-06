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


def add_stud():
    # Oppretter en cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    studentnr = studentnr_1.get()
    fornavn = fornavn_1.get()
    etternavn = etternavn_1.get()
    epost = epost_1.get()
    telefon = telefon_1.get()

    # Setter opp database strukturen for tabellen
    m_stud = ('INSERT INTO Student'
             '(Studentnr, Fornavn, Etternavn, Epost, Telefon)'
             'VALUES(%s, %s, %s, %s, %s)')
    d_stud = (studentnr, fornavn, etternavn, epost, telefon)

    # Legger strengene inn i databasen
    marker.execute(m_stud, d_stud)
    mydb.commit()

    # Lukker cursor
    marker.close()


def update_stud():
    # Oppretter en cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    studentnr = studentnr_1.get()
    fornavn = fornavn_1.get()
    etternavn = etternavn_1.get()
    epost = epost_1.get()
    telefon = telefon_1.get()

    # Setter opp database strukturen for tabellen
    m_stud = ('UPDATE Student '
              'SET Fornavn = %s, Etternavn = %s, Epost = %s, Telefon = %s '
              'WHERE Studentnr = %s')

    d_stud = (fornavn, etternavn, epost, telefon, studentnr)

    # Legger strengene inn i databasen
    marker.execute(m_stud, d_stud)
    mydb.commit()

    # Lukker cursor
    marker.close()


def delete_stud():
    # Oppretter en cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    studentnr = studentnr_2.get()


    # Setter opp database strukturen for tabellen
    m_stud = ('DELETE FROM Student '
              'WHERE Studentnr = %s')
    d_stud = studentnr

    # Legger strengene inn i databasen
    marker.execute(m_stud, d_stud)
    mydb.commit()

    # Lukker cursor
    marker.close()


# GUI for administrering av emne
def adm_emne_gui():

    # Oppretter en toplevel-frame
    adm_emne = Toplevel()
    adm_emne.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_emne, text="Administrering av Emne").grid(column=0, columnspan=8, row=0, pady=15, padx=15,
                                                            sticky=(W, E))
    ttk.Separator(adm_emne).grid(row=2, column=0, columnspan=8, pady=5, sticky=(W, E))

    # Lager en infoboks som skal gi informasjon til brukeren
    p = ttk.Panedwindow(adm_emne, orient=VERTICAL)
    p.grid(row=3, column=3, columnspan=3, rowspan=3, padx=20)
    l1 = ttk.Labelframe(p, text='Info', width=125, height=100)
    p.add(l1)
    l = Label(l1, text="Fyll inn alle feltene med \n"
                       "riktig informasjon om \n "
                       "emnet, og klikk \n"
                       "'Legg til emne'")
    l.grid(row=0, column=0)

    # Lables og Entries for administrasjon av emne
    ttk.Label(adm_emne, text='Emnekode:').grid(row=3, column=0, padx=5, pady=7, sticky=W)
    ttk.Entry(adm_emne, textvariable=emnekode_1, width=15).grid(row=3, column=1, padx=5, pady=7, sticky=W)

    ttk.Label(adm_emne, text='Emnenavn:').grid(row=4, column=0, padx=5, pady=7, sticky=W)
    ttk.Entry(adm_emne, textvariable=emnenavn_1, width=15).grid(row=4, column=1, padx=5, pady=7, sticky=W)

    ttk.Label(adm_emne, text='Studiepoeng:').grid(row=5, column=0, padx=5, pady=7, sticky=W)
    ttk.Entry(adm_emne, textvariable=studiepoeng_1, width=8).grid(row=5, column=1, padx=5, pady=7, sticky=W)

    ttk.Separator(adm_emne).grid(row=6, column=0, columnspan=8, pady=5, sticky=(W, E))

    # Lager button som legger inn strengene i databasen
    ttk.Button(adm_emne, text='Legg til emne', command=add_emne).grid(row=7, column=0, columnspan=2, padx=5, pady=5,
                                                                      sticky=W)
    ttk.Separator(adm_emne).grid(row=8, column=0, columnspan=8, pady=5, sticky=(W, E))

    # Lager button som gj??r at brukeren kan g?? tilbake til hovedmeny
    ttk.Button(adm_emne, text='G?? tilbake', command=adm_emne.destroy).grid(row=9, column=4, padx=5, pady=5, sticky=E)
    ttk.Separator(adm_emne).grid(row=10, column=0, columnspan=8, pady=5, sticky=(W, E))


# GUI for administrering av student
def adm_stud_gui():
    # Oppretter en toplevel-frame
    adm_stud = Toplevel()
    adm_stud.title('Eksamensadministrasjonsapplikasjon')


    ttk.Label(adm_stud, text="Administrering av Studenter").grid(column=0, row=0, pady=15, padx=15, sticky='WE')

    # Oppretter en Notebook-widget
    n = ttk.Notebook(adm_stud)
    n.grid(row=1, column=0, columnspan=4, rowspan=6, sticky='NESW')
    f1 = ttk.Frame(n)  # f??rste side
    f2 = ttk.Frame(n)  # andre side

    n.add(f1, text='Legg til/oppdater student')
    n.add(f2, text='Slett eksisterende student')

    # Oppretter Panedwindow for Notebook side 1 og legger inn veiledende tekst
    p1 = ttk.Panedwindow(f1, orient=VERTICAL)
    p1.grid(row=3, column=3, columnspan=3, rowspan=6, padx=20, pady=10)
    l1 = ttk.Labelframe(p1, text='Ny student', width=150, height=100)
    p1.add(l1)
    label = Label(l1, text="Fyll inn alle feltene med riktig      \n"
                           "informasjon om studenten,          \n"
                           "og klikk 'Legg til student'!           ")
    label.grid(row=0, column=0)

    l2 = ttk.Labelframe(p1, text='Oppdater student', width=150, height=100)
    p1.add(l2)
    label2 = Label(l2, text="Fyll ut studentnr p?? studenten som       \n"
                            "skal endres, og fyll ut resterende          \n"
                            "felter med oppdatert informasjon.         \n"
                            "Og klikk p?? 'Oppdater student'              ")
    label2.grid(row=0, column=0)

    # Lables og Entries for Notebook side 1
    ttk.Label(f1, text='Studentnr:').grid(row=3, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f1, textvariable=studentnr_1, width=6).grid(row=3, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f1, text='Fornavn:').grid(row=4, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f1, textvariable=fornavn_1).grid(row=4, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f1, text='Etternavn:').grid(row=5, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f1, textvariable=etternavn_1).grid(row=5, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f1, text='Epost:').grid(row=6, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f1, textvariable=epost_1).grid(row=6, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f1, text='Telefonnr:').grid(row=7, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f1, textvariable=telefon_1, width=8).grid(row=7, column=2, padx=5, pady=7, sticky=W)

    ttk.Separator(f1).grid(row=8, column=1, columnspan=6, sticky=(W, E))

    # Oppretter button som legger inn strengene i databasen
    ttk.Button(f1, text='Legg til student', command=add_stud).grid(row=9, column=1, columnspan=2, pady=15, padx=5,
                                                                   sticky=W)

    # Oppretter button som legger inn de oppdaterte strengene i databasen
    ttk.Button(f1, text='Oppdater student', command=update_stud).grid(row=9, column=1, columnspan=2, pady=15, padx=5,
                                                                      sticky=E)

    # Oppretter Panedwindow for Notebook side 2 og legger inn veiledende tekst
    p2 = ttk.Panedwindow(f2, orient=VERTICAL)
    p2.grid(row=3, column=3, columnspan=3, rowspan=6, padx=20, pady=10)
    l3 = ttk.Labelframe(p2, text='Slett student', width=125, height=100)
    p2.add(l3)
    label3 = Label(l3, text="NB! Studenter med eksamensresultater \n"
                            "g??r ikke ?? slette!                                    \n"
                            "Fyll inn studentnr og \n"
                            "trykk 'Slett student'.")
    label3.grid(row=0, column=0)

    # Lables og Entries for Notebook side 2
    ttk.Label(f2, text='Studentnr:').grid(row=3, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f2, textvariable=studentnr_2, width=6).grid(row=3, column=2, padx=5, pady=7, sticky=W)

    ttk.Separator(f2).grid(row=8, column=1, columnspan=6, sticky=(W, E))

    # Oppretter button som sletter student i databasen
    ttk.Button(f2, text='Slett student', command=delete_stud).grid(row=9, column=1, columnspan=2, pady=15, padx=5,
                                                                      sticky=E)

    # Button som avslutter programmet
    ttk.Button(adm_stud, text='Lukk vinduet', command=adm_stud.destroy).grid(row=11, column=3, pady=15, padx=5,
                                                                             sticky=E)

def utskrift_eks():

    utskrift_eksamen = Toplevel()
    utskrift_eksamen.title('Utskrift av eksamen')

    # innholdet i vinduet
    ramme = ttk.Frame(utskrift_eksamen, padding="6 6 15 15")
    ramme.grid(column=0, row=0, sticky=(N, W, E, S))
    ramme.columnconfigure(0, weight=1)
    ramme.rowconfigure(0, weight=1)

    ttk.Label(ramme, text="Utskrift eksamen") .grid(column=0, row=0, columnspan=4, sticky=(W, E))
    ttk.Separator(ramme, orient=HORIZONTAL).grid(column=0, row=1, columnspan=5, sticky=(W, E))

    p1 = ttk.Panedwindow(ramme, orient=VERTICAL, width=200, height=100)
    p1.grid(row=2, column=2, padx=5, pady=5, sticky=(W, E), columnspan=3)
    l1 = ttk.Labelframe(p1, text='Info', width=150, height=100)
    p1.add(l1)
    label = Label(l1, text="Ved eksamen i en periode\n"
                           "velg fra og til dato.\n"
                           "Hvis du vil ha en spesifikk dag\n "
                           "bruk kun fra dato")
    label.grid(row=4, column=4)


    # label fra og til
    l = Label(ramme, text="Fra")
    l.grid(column=1, row=3, sticky=S)
    l2 = Label(ramme, text="Formatet YYYY/MM/DD")
    l2.grid(column=2, row=2, sticky=S, columnspan=2)
    l3 = Label(ramme, text="Til")
    l3.grid(column=1, row=4, sticky=(N, W))

    # fra dato
    fra_aar = StringVar()
    fra_aar_entry = ttk.Entry(ramme, textvariable=fra_aar, width=7).grid(column=2, row=3, sticky=(N, W))

    fra_maaned = StringVar()
    fra_maaned_entry = ttk.Entry(ramme, textvariable=fra_maaned, width=6).grid(column=3, row=3, sticky=(N, W))

    fra_dag = StringVar()
    fra_dag_entry = ttk.Entry(ramme, textvariable=fra_dag, width=6).grid(column=4, row=3, sticky=(N, W))

    # til dato
    til_aar = StringVar()
    til_aar_entry = ttk.Entry(ramme, textvariable=til_aar, width=7).grid(column=2, row=4, sticky=(N, W))

    til_maaned = StringVar()
    til_maaned_entry = ttk.Entry(ramme, textvariable=til_maaned, width=6).grid(column=3, row=4, sticky=(N, W))

    til_dag = StringVar()
    til_dag_entry = ttk.Entry(ramme, textvariable=til_dag, width=6).grid(column=4, row=4, sticky=(N, W))

    # Lager Treeview-widget
    tree_ut = ttk.Treeview(ramme)

    tree_ut["columns"] = ("1", "2", "3", "4", "5", "6")
    tree_ut.column("#0", anchor="w", width=0)
    tree_ut.column("#1", width=100)
    tree_ut.column("#2", width=100)
    tree_ut.column("#3", width=100)
    tree_ut.column("#4", width=100)
    tree_ut.column("#5", width=100)
    # tree.column("#6", width=100)
    # tree.heading("#0", text='ID', anchor='w')
    tree_ut.heading("#1", text="Emnekode")
    tree_ut.heading("#2", text="Emnenavn")
    tree_ut.heading("#3", text="Romnr")
    tree_ut.heading("#4", text="Antall plasser")
    tree_ut.heading("#5", text="Dato")
    tree_ut.heading("#6", text="Antall oppmeldte")
    # tree.heading("#6", text="Studiepoeng Totalt")

    ysb = ttk.Scrollbar(ramme, orient=VERTICAL, command=tree_ut.yview)
    tree_ut['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree_ut.grid(row=2, column=0, sticky=NSEW)
    ysb.grid(row=2, column=1, sticky=(N, S, W))

    ttk.Button(ramme, text='Utf??r', command=lambda: info(fra_dag, fra_maaned, fra_aar, til_dag, til_maaned,
                                                         til_aar, tree_ut)).grid(column=4, row=6, sticky=W)

    for child in ramme.winfo_children():
        child.grid_configure(pady=2, padx=5)

def info(fra_dag, fra_maaned, fra_aar, til_dag, til_maaned, til_aar, tree_ut):

    tree_ut.bind()
    # Oppretter en cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    fra_dag1 = fra_dag.get()
    fra_maaned1 = fra_maaned.get()
    fra_aar1 = fra_aar.get()
    til_dag1 = til_dag.get()
    til_maaned1 = til_maaned.get()
    til_aar1 = til_aar.get()

    til_dato = til_aar1 + til_maaned1 + til_dag1
    fra_dato = fra_aar1 + fra_maaned1 + fra_dag1

    if til_dato == '':

        m_utskrift = ('SELECT eksamen.Emnekode, Emnenavn, eksamen.Romnr, Antallplasser, eksamen.dato '
                    'FROM Eksamen, rom, emne '
                    'WHERE Dato = %s AND eksamen.romnr = rom.Romnr '
                    'AND eksamen.Emnekode = emne.emnekode')

        d_utskrift = fra_dato
        marker.execute(m_utskrift, d_utskrift)
        mydb.commit()
        for row in marker:
            tree_ut.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))

        # Lukker cursor
        marker.close()


    else:
        if til_dato != '':
            m_utskrift = ('SELECT eksamen.Emnekode, Emnenavn, eksamen.Romnr, Antallplasser, eksamen.dato '
                          'FROM Eksamen, rom, emne '
                          'WHERE Dato >= %s AND Dato <= %s '
                          'AND eksamen.romnr = rom.Romnr '
                          'AND eksamen.Emnekode = emne.emnekode '
                          'GROUP BY Dato DESC')

            d_utskrift = fra_dato, til_dato
            marker.execute(m_utskrift, d_utskrift)
            mydb.commit()
            for row in marker:
                tree_ut.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))

            # Lukker cursor
            marker.close()










# connecter til databasen
mydb = pymysql.connect(host='localhost', port=3306, user='Eksamenssjef', passwd='eksamen2017', db='Eksamen')

# oppretter hovedvinduet
root = Tk()
root.title("Eksamensapplikasjon")

# innholdet i vinduet
mainframe = ttk.Frame(root, padding="6 6 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Tekst som Label, knapper som Button, med separators og plassering i grid
ttk.Label(mainframe, text="Administrering av eksamen ved HSN").grid(column=0, row=0, columnspan=2, sticky=(W, E))
ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=1, columnspan=3, sticky=(W, E))

ttk.Label(mainframe, text="Administrer Studenter").grid(column=0, row=2, sticky=(E, W))
ttk.Button(mainframe, text="Studenter", command=adm_stud_gui).grid(column=1, row=2, padx=20, sticky=W)

ttk.Label(mainframe, text="Administrer Emner").grid(column=0, row=3, sticky=(E, W))
ttk.Button(mainframe, text="Emner", command=adm_emne_gui).grid(column=1, row=3, padx=20, sticky=W)

ttk.Label(mainframe, text="Administrer Rom").grid(column=0, row=4, sticky=(E, W))
ttk.Button(mainframe, text="Rom").grid(column=1, row=4, padx=20, sticky=W)

ttk.Label(mainframe, text="Administrer Eksamener").grid(column=0, row=5, sticky=(E, W))
ttk.Button(mainframe, text="Eksamener").grid(column=1, row=5, padx=20, sticky=W)

ttk.Label(mainframe, text="Administrer Karakterer").grid(column=0, row=6, sticky=(E, W))
ttk.Button(mainframe, text="Karakterer").grid(column=1, row=6, padx=20, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=7, columnspan=3, sticky=(W, E))

ttk.Label(mainframe, text="Utskrifter av oversikter").grid(column=0, row=8, sticky=(E, W))
ttk.Button(mainframe, text="Utskrift eksamen", command=utskrift_eks).grid(column=1, row=8, padx=20, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=9, columnspan=3, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy).grid(column=2, row=10, padx=20, sticky=E,)

tekst = Text(mainframe, width=26, height=10, wrap="word")
tekst.grid(column=2, row=2, rowspan=5)
tekst.insert('1.0', 'Fra denne siden kan du redigere alle aspekter av eksamensinformasjonen. P?? administrer studenter'
                    ' kan du legge til, endre eller slette studenter')


# lager padding for alle child-elementene
for child in mainframe.winfo_children():
    child.grid_configure(pady=5)

# Strenger for student
studentnr_1 = StringVar()
fornavn_1 = StringVar()
etternavn_1 = StringVar()
epost_1 = StringVar()
telefon_1 = StringVar()
studentnr_2 = StringVar()

# Strenger for emne
emnekode_1 = StringVar()
emnenavn_1 = StringVar()
studiepoeng_1 = StringVar()

# Strenger for utskrift eksamen
fra_dag1 = StringVar()
fra_maaned1 = StringVar()
fra_aar1 = StringVar()
til_dag1 = StringVar()
til_maaned1 = StringVar()
til_aar1 = StringVar()
root.mainloop()
