from tkinter import *
from tkinter import ttk
import pymysql


def utskrift_emneres(tree1):
    tree1.bind()
    for i in tree1.get_children():
        tree1.delete(str(i))
    marker = mydb.cursor()
    emne = emne1.get()

    m_emneres = ('SELECT Studentnr, Dato, Karakter '
                 'FROM Eksamensresultat '
                 'WHERE Emnekode = %s '
                 'ORDER BY Studentnr ASC;')

    d_emneres = emne

    marker.execute(m_emneres, d_emneres)

    teller = 0  # Teller som holder styr på første kolonne
    for row in marker:
        tree1.insert('', 'end', text=str(teller), values=(row[0], row[1], row[2]))
        teller += 1  # Øking for hver gjennomgang

    marker.close()


def utskrift_eks_student(tree2):
    tree2.bind()
    for i in tree2.get_children():
        tree2.delete(str(i))
    marker = mydb.cursor()
    studentnr = studentnr_2.get()

    m_eks_student = ('SELECT Dato, Karakter, Emnenavn, Studiepoeng '
                     'FROM eksamensresultat, emne '
                     'WHERE Studentnr=%s AND eksamensresultat.emnekode=emne.emnekode '
                     'ORDER BY dato desc;')

    d_eks_student = studentnr

    marker.execute(m_eks_student, d_eks_student)

    for row in marker:
        tree2.insert('', 'end', values=(row[0], row[1], row[2], row[3]))

    marker.close()


def utskrift_eksamen_pd(fra_dag, fra_maaned, fra_aar, til_dag, til_maaned, til_aar, tree3):
    tree3.bind()
    for i in tree3.get_children():
        tree3.delete(str(i))
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
            tree3.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))

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
                tree3.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))

            # Lukker cursor
            marker.close()


def utskrift_karstat(tree4):
    tree4.bind()
    for i in tree4.get_children():
        tree4.delete(str(i))
    marker = mydb.cursor()
    dato = dato1.get()
    emnekode = emne1.get()

    m_karstat = (
        'SELECT Emnenavn, Karakter, count(*) '
        'FROM eksamensresultat, Emne '
        'WHERE dato=%s '
        'AND eksamensresultat.emnekode=%s '
        'AND eksamensresultat.emnekode=emne.emnekode '
        'GROUP BY karakter; '
    )
    d_karstat = (dato, emnekode)

    marker.execute(m_karstat, d_karstat)

    for row in marker:
        tree4.insert('', 'end', values=(row[0], row[1], row[2]))

    marker.close()


def utskrift_stud_emne(tree5):
    tree5.bind()
    for i in tree5.get_children():
        tree5.delete(str(i))
    marker = mydb.cursor()

    emne2 = emne_2.get()

    m_stud_emne = ('SELECT Student.Studentnr, Fornavn, Etternavn, Emne.Emnekode, Emnenavn '
                   'FROM Student, eksamensresultat, emne '
                   'WHERE Emne.Emnekode = %s '
                   'AND Student.Studentnr=eksamensresultat.Studentnr '
                   'ORDER BY Etternavn asc;')
    d_stud_emne = emne2

    marker.execute(m_stud_emne, d_stud_emne)

    for row in marker:
        tree5.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))

    marker.close()


def utskrift_vit(tree6, fornavn_vit, etternavn_vit, total_vit):
    tree6.bind()
    fornavn_vit.bind()
    etternavn_vit.bind()
    total_vit.bind()
    studentnr = studentnr_1.get()

    # Sletter innholdet i Treeviewet
    for i in tree6.get_children():
        tree6.delete(str(i))

    #Oppretter cursor for vitnemål
    marker_vit = mydb.cursor()

    m_vit = ('SELECT eksamensresultat.emnekode, emnenavn, studiepoeng, MIN(karakter) '
                'FROM emne left outer join eksamensresultat on emne.emnekode = eksamensresultat.emnekode '
                'WHERE studentnr=%s '
                'GROUP BY eksamensresultat.emnekode, emnenavn')
    d_vit = studentnr

    marker_vit.execute(m_vit, d_vit)

    for row in marker_vit:
        tree6.insert('', 'end', values=(row[0], row[1], row[2], row[3]))

    marker_vit.close()

    # Oppretter cursor for Fornavn Entryen
    marker_fornavn = mydb.cursor()

    m_fornavn = ('SELECT Fornavn '
                'FROM Student '
                'WHERE Studentnr = %s')

    d_fornavn = studentnr

    marker_fornavn.execute(m_fornavn, d_fornavn)

    for row in marker_fornavn:

        fornavn = row
    fornavn_vit.insert('', fornavn)
    marker_fornavn.close()

    # Oppretter cursor for Etternavn Entryen
    marker_etternavn = mydb.cursor()
    m_etternavn = ('SELECT Etternavn '
                 'FROM Student '
                 'WHERE Studentnr = %s')

    d_etternavn = studentnr

    marker_etternavn.execute(m_etternavn, d_etternavn)

    etternavn_vit.insert(0, marker_etternavn)
    marker_etternavn.close()

    # Oppretter cursor for Totalt studiepoeng Entryen
    marker_total = mydb.cursor()
    m_total = ('SELECT SUM(Studiepoeng) '
                'FROM eksamensresultat, emne '
                'WHERE studentnr=%s '
                'AND emne.emnekode=eksamensresultat.emnekode '
                'AND "F" not in (SELECT Karakter FROM eksamensresultat) '
                'GROUP BY Karakter LIMIT 1')

    d_total = studentnr

    marker_total.execute(m_total, d_total)

    total_vit.insert(0, marker_total)
    marker_total.close()



# GUI for utskrifter
def utskrifter():
    # Oppretter en toplevel-frame
    utskrift = Toplevel()
    utskrift.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(utskrift, text='Oversikt over utskrifter', font=16).grid(row=0, column=0, padx=5)

    # Oppretter en Notebook-widget
    n = ttk.Notebook(utskrift)
    n.grid(row=1, column=0, columnspan=4, rowspan=6, sticky='NESW')
    f1 = ttk.Frame(n)  # første side
    f2 = ttk.Frame(n)  # andre side
    f3 = ttk.Frame(n)  # tredje side
    f4 = ttk.Frame(n)  # fjerde side
    f5 = ttk.Frame(n)  # femte side
    f6 = ttk.Frame(n)  # sjette side

    n.add(f1, text='Eksamensresultater(Emne)')
    n.add(f2, text='Eksamensresultater(Student)')
    n.add(f3, text='Alle eksamener(Periode/Dag)')
    n.add(f4, text='Karakterstatistikk(Eksamen)')
    n.add(f5, text='Studenter(Emne)')
    n.add(f6, text='Vitnemål')

    # Side 1 i notebook er eksamensresultater i et emne
    ttk.Label(f1, text="Eksamensresultat i et emne").grid(column=0, columnspan=1, row=0, pady=15, padx=15,
                                                          sticky='WE')

    ttk.Separator(f1).grid(row=1, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(f1, text='Emnekode:').grid(row=2, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=emne1, width=15).grid(row=2, column=1, padx=5, pady=5, sticky=W)

    ttk.Separator(f1).grid(row=3, column=0, columnspan=1, pady=5, sticky=(W, E))

    # Oppretter treeview
    tree1 = ttk.Treeview(f1)

    tree1["columns"] = ("1", "2", "3")
    tree1.column("#0", anchor="w", width=0)
    tree1.column("#1", width=100)
    tree1.column("#2", width=100)
    tree1.column("#3", width=100)
    tree1.heading("#1", text="Studentnr")
    tree1.heading("#2", text="Dato")
    tree1.heading("#3", text="Karakter")

    ysb = ttk.Scrollbar(f1, orient=VERTICAL, command=tree1.yview)
    tree1['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree1.grid(row=4, column=0, sticky=NSEW)
    ysb.grid(row=4, column=1, sticky=NS)

    ttk.Button(f1, text='Utfør', command=lambda: utskrift_emneres(tree1)).grid(row=6, column=1, padx=5,
                                                                               pady=5, sticky=W)

    # Side 2 i notebook er eksamensresultater for en student
    ttk.Label(f2, text="Eksamensresultater for en student").grid(column=0, columnspan=1, row=0, pady=15, padx=15,
                                                                 sticky='WE')

    ttk.Separator(f2).grid(row=1, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(f2, text='Studentnr:').grid(row=2, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f2, textvariable=studentnr_2, width=15).grid(row=2, column=1, padx=5, pady=5, sticky=W)

    ttk.Separator(f2).grid(row=3, column=0, columnspan=1, pady=5, sticky=(W, E))

    # Oppretter treeview
    tree2 = ttk.Treeview(f2)

    tree2["columns"] = ("1", "2", "3", "4")
    tree2.column("#0", anchor="w", width=0)
    tree2.column("#1", width=100)
    tree2.column("#2", width=100)
    tree2.column("#3", width=100)
    tree2.column("#4", width=100)
    tree2.heading("#1", text="Dato")
    tree2.heading("#2", text="Karakter")
    tree2.heading("#3", text="Emnenavn")
    tree2.heading("#4", text="Studiepoeng")

    ysb = ttk.Scrollbar(f2, orient=VERTICAL, command=tree2.yview)
    tree2['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree2.grid(row=4, column=0, sticky=NSEW)
    ysb.grid(row=4, column=1, sticky=NS)

    ttk.Button(f2, text='Utfør', command=lambda: utskrift_eks_student(tree2)).grid(row=6, column=1, padx=5,
                                                                                   pady=5, sticky=W)

    # Side 3 i notebook er
    p1 = ttk.Panedwindow(f3, orient=VERTICAL, width=200, height=100)
    p1.grid(row=2, column=2, padx=5, pady=5, sticky=(W, E), columnspan=3)
    l1 = ttk.Labelframe(p1, text='Info', width=150, height=100)
    p1.add(l1)
    label = Label(l1, text="Ved eksamen i en periode\n"
                           "velg fra og til dato.\n"
                           "Hvis du vil ha en spesifikk dag\n "
                           "bruk kun fra dato")
    label.grid(row=4, column=4)

    # label fra og til
    l = Label(f3, text="Fra")
    l.grid(column=1, row=3, sticky=S)
    l2 = Label(f3, text="Formatet YYYY/MM/DD")
    l2.grid(column=2, row=2, sticky=S, columnspan=2)
    l3 = Label(f3, text="Til")
    l3.grid(column=1, row=4, sticky=(N, W))

    # fra dato
    fra_aar = StringVar()
    fra_aar_entry = ttk.Entry(f3, textvariable=fra_aar, width=7).grid(column=2, row=3, sticky=(N, W))

    fra_maaned = StringVar()
    fra_maaned_entry = ttk.Entry(f3, textvariable=fra_maaned, width=6).grid(column=3, row=3, sticky=(N, W))

    fra_dag = StringVar()
    fra_dag_entry = ttk.Entry(f3, textvariable=fra_dag, width=6).grid(column=4, row=3, sticky=(N, W))

    # til dato
    til_aar = StringVar()
    til_aar_entry = ttk.Entry(f3, textvariable=til_aar, width=7).grid(column=2, row=4, sticky=(N, W))

    til_maaned = StringVar()
    til_maaned_entry = ttk.Entry(f3, textvariable=til_maaned, width=6).grid(column=3, row=4, sticky=(N, W))

    til_dag = StringVar()
    til_dag_entry = ttk.Entry(f3, textvariable=til_dag, width=6).grid(column=4, row=4, sticky=(N, W))

    # Lager Treeview-widget
    tree3 = ttk.Treeview(f3)

    tree3["columns"] = ("1", "2", "3", "4", "5", "6")
    tree3.column("#0", anchor="w", width=0)
    tree3.column("#1", width=100)
    tree3.column("#2", width=100)
    tree3.column("#3", width=100)
    tree3.column("#4", width=100)
    tree3.column("#5", width=100)
    tree3.heading("#1", text="Emnekode")
    tree3.heading("#2", text="Emnenavn")
    tree3.heading("#3", text="Romnr")
    tree3.heading("#4", text="Antall plasser")
    tree3.heading("#5", text="Dato")
    tree3.heading("#6", text="Antall oppmeldte")

    ysb = ttk.Scrollbar(f3, orient=VERTICAL, command=tree3.yview)
    tree3['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree3.grid(row=2, column=0, sticky=NSEW)
    ysb.grid(row=2, column=1, sticky=(N, S, W))

    ttk.Button(f3, text='Utfør', command=lambda: utskrift_eksamen_pd(fra_dag, fra_maaned, fra_aar, til_dag, til_maaned,
                                                                  til_aar, tree3)).grid(column=4, row=6, sticky=W)

    # Side 4 i notebook er karakterstatistikk
    ttk.Label(f4, text='Karakterstatistikk eksamen').grid(column=0, columnspan=1, row=0, pady=15, padx=15,
                                                          sticky='WE')

    ttk.Separator(f4).grid(row=2, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(f4, text='Emnekode:').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f4, textvariable=emne1, width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f4, text='Dato:').grid(row=4, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f4, textvariable=dato1, width=15).grid(row=4, column=1, padx=5, pady=5, sticky=W)

    tree4 = ttk.Treeview(f4)

    tree4["columns"] = ("1", "2", "3")
    tree4.column("#0", anchor="w", width=0)
    tree4.column("#1", width=100)
    tree4.column("#2", width=100)
    tree4.column("#3", width=100)
    tree4.heading("#1", text="Emnenavn")
    tree4.heading("#2", text="Karakter")
    tree4.heading("#3", text="Antall")

    ysb = ttk.Scrollbar(f4, orient=VERTICAL, command=tree4.yview)

    tree4['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree4.grid(row=6, column=0, columnspan=3, pady=7, sticky=NSEW)
    ysb.grid(row=6, column=4, pady=7, sticky=NS)

    ttk.Button(f4, text='Karakterstatistikk', command=lambda: utskrift_karstat(tree4)).grid(row=8, column=0,
                                                                                            padx=5,
                                                                                            pady=5, sticky=W)

    # Side 5 i notebook er studenter i et emne
    ttk.Label(f5, text="En oversikt som viser studentene i et emne").grid(column=0, columnspan=1, row=0, pady=15,
                                                                          padx=15,
                                                                          sticky='WE')

    ttk.Separator(f5).grid(row=1, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(f5, text='Emnekode:').grid(row=2, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f5, textvariable=emne_2, width=15).grid(row=2, column=1, padx=5, pady=5, sticky=W)

    ttk.Separator(f5).grid(row=3, column=0, columnspan=1, pady=5, sticky=(W, E))

    # Oppretter treeview
    tree5 = ttk.Treeview(f5)

    tree5["columns"] = ("1", "2", "3", "4", "5")
    tree5.column("#0", anchor="w", width=0)
    tree5.column("#1", width=100)
    tree5.column("#2", width=100)
    tree5.column("#3", width=100)
    tree5.column("#4", width=100)
    tree5.column("#5", width=100)
    tree5.heading("#1", text="Studentnr")
    tree5.heading("#2", text="Fornavn")
    tree5.heading("#3", text="Etternavn")
    tree5.heading("#4", text="Emnekode")
    tree5.heading("#5", text="Emnenavn")

    ysb = ttk.Scrollbar(f1, orient=VERTICAL, command=tree1.yview)
    tree5['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree5.grid(row=4, column=0, sticky=NSEW)
    ysb.grid(row=4, column=1, sticky=NS)

    ttk.Button(f5, text='Utfør', command=lambda: utskrift_stud_emne(tree5)).grid(row=6, column=1, padx=5,
                                                                                 pady=5, sticky=W)

    # Side 6 i notebook'en er vitnemål
    ttk.Label(f6, text="Utskrift av vitnemål for en student").grid(column=0, columnspan=8, row=0, pady=15, padx=15,
                                                                   sticky=(W, E))
    ttk.Separator(f6).grid(row=1, column=0, columnspan=8, pady=5, sticky=(W, E))

    # Lables og Entries
    ttk.Label(f6, text='Studentnr:').grid(row=2, column=0, padx=5, pady=7, sticky=W)
    ttk.Entry(f6, textvariable=studentnr_1, width=6).grid(row=2, column=1, padx=5, pady=7, sticky=W)

    ttk.Label(f6, text='Fornavn:').grid(row=3, column=0, padx=5, pady=7, sticky=W)
    fornavn_vit = ttk.Entry(f6, width=6, state='readonly')
    fornavn_vit.grid(row=3, column=1, padx=5, pady=7, sticky=W)

    ttk.Label(f6, text='Etternavn:').grid(row=4, column=0, padx=5, pady=7, sticky=W)
    etternavn_vit = ttk.Entry(f6, width=6, state='readonly')
    etternavn_vit.grid(row=4, column=1, padx=5, pady=7, sticky=W)

    # Oppretter Panedwindow for å legge inn veiledende tekst
    p = ttk.Panedwindow(f6, orient=VERTICAL)
    p.grid(row=2, column=3, columnspan=2, rowspan=3, padx=20, pady=10)
    l = ttk.Labelframe(p, text='Ny student', width=300, height=100)
    p.add(l)
    label = Label(l, text="LOL INFO")
    label.grid(row=0, column=0)

    # Lager Treeview-widget
    tree6 = ttk.Treeview(f6)

    tree6["columns"] = ("1", "2", "3", "4")
    tree6.column("#0", anchor="w", width=0)
    tree6.column("#1", width=100)
    tree6.column("#2", width=100)
    tree6.column("#3", width=100)
    tree6.column("#4", width=100)
    tree6.heading("#1", text="Emnekode")
    tree6.heading("#2", text="Emnenavn")
    tree6.heading("#3", text="Studiepoeng")
    tree6.heading("#4", text="Karakter")

    ysb = ttk.Scrollbar(f6, orient=VERTICAL, command=tree6.yview)

    tree6['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree6.grid(row=5, column=0, sticky=NSEW)
    ysb.grid(row=5, column=1, sticky=NS)

    ttk.Label(f6, text='Totalt studiepoeng:').grid(row=6, column=0, padx=5, pady=7, sticky=W)
    total_vit = ttk.Entry(f6, width=5, state='readonly')
    total_vit.grid(row=6, column=1, padx=5, pady=7, sticky=W)

    # Oppretter button som kjører mysql-queries mot databasen
    ttk.Button(f6, text='Utfør', command=lambda: utskrift_vit(tree6, fornavn_vit, etternavn_vit, total_vit)).grid(row=7,
                                                                                                                  column=0,
                                                                                                                  columnspan=2,
                                                                                                                  pady=15,
                                                                                                                  padx=5,
                                                                                                                  sticky=W)

    # Lager button som gjør at brukeren kan gå tilbake til hovedmeny
    ttk.Button(utskrift, text='Lukk vinduet', command=utskrift.destroy).grid(row=9, column=3, padx=5, pady=15, sticky=E)


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

    ttk.Label(adm_kar, text='Administrering av Karakter').grid(column=0, columnspan=1, row=0, pady=15, padx=15,
                                                               sticky='WE')

    # Oppretter en Notebook-widget
    n = ttk.Notebook(adm_kar)
    n.grid(row=1, column=0, columnspan=4, rowspan=6, sticky='NESW')
    f1 = ttk.Frame(n)  # første side
    f2 = ttk.Frame(n)  # andre side

    n.add(f1, text='Ajourhold karakter på student')
    n.add(f2, text='Registrer karakterer for avholdt eksamen')

    #Side 1 i notebook
    ttk.Separator(f1).grid(row=2, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(f1, text='Studentnr:').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=studentnr1, width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f1, text='Emnekode:').grid(row=4, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=emne1, width=15).grid(row=4, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f1, text='Karakter:').grid(row=5, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=karakter1, width=15).grid(row=5, column=1, padx=5, pady=5, sticky=W)

    ttk.Button(f1, text='Oppdatere karakter', command=upd_karakter).grid(row=8, column=0, padx=5, pady=5, sticky=W)



    #Side 2 i notebook
    ttk.Label(f2, text='Emnekode:').grid(row=1, column=2, padx=10, pady=5, sticky=W)
    ttk.Entry(f2, textvariable=emne1, width=15).grid(row=1, column=3, padx=0, pady=5, sticky=W)

    ttk.Label(f2, text='Dato:').grid(row=2, column=2, padx=10, pady=5, sticky=W)
    ttk.Entry(f2, textvariable=dato1, width=15).grid(row=2, column=3, padx=0, pady=5, sticky=W)

    ttk.Separator(f2).grid(row=4, column=0, columnspan=5, pady=5, sticky=(W, E))

    ttk.Label(f2, text='Studentnr:').grid(row=5, column=0, padx=2, pady=5, sticky=W)
    stud = ttk.Entry(f2, textvariable=studentnr1, width=10)
    stud.grid(row=5, column=0, padx=40, pady=5, sticky=E)

    ttk.Label(f2, text='Karakter:').grid(row=6, column=0, padx=2, pady=5, sticky=W)
    kar = ttk.Entry(f2, textvariable=karakter1, width=10)
    kar.grid(row=6, column=0, padx=40, pady=5, sticky=E)

    ttk.Separator(f2).grid(row=7, column=0, columnspan=5, pady=5, sticky=(W, E))

    button = ttk.Button(f2, text='Legg til eksamensresultat', command=lambda: add_eksres(stud, kar))
    button.grid(row=8, column=0, padx=5, pady=5, sticky=W)

    p1 = ttk.Panedwindow(f2, orient=VERTICAL)
    p1.grid(row=1, column=0, columnspan=2, rowspan=2, padx=20, sticky=W)
    l3 = ttk.Labelframe(p1, text='Info', width=50, height=100)
    p1.add(l3)
    l4 = Label(l3, justify='left', text="Fyll inn alle feltene med \n"
                                        "riktig informasjon om \n "
                                        "eksamen, og klikk \n"
                                        "'Legg til eksamensresultat'")
    l4.grid(row=0, column=0)


    ttk.Button(adm_kar, text='Lukk vinduet', command=adm_kar.destroy).grid(row=8, column=2, padx=5, pady=5, sticky=E)


def utskrift_eksamen(tree):
    tree.bind()
    for i in tree.get_children():
        tree.delete(str(i))
    marker = mydb.cursor()

    marker.execute(
        'SELECT * '
        'FROM Eksamen '
        'ORDER BY Dato DESC ')

    teller = 0  # Teller som holder styr på første kolonne
    for row in marker:
        tree.insert('', 'end', text=str(teller), values=(row[0], row[1], row[2]))
        teller += 1  # Øking for hver gjennomgang

    marker.close()


def add_eksamen():
    marker = mydb.cursor()

    emnekode = emne1.get()
    dato = dato1.get()
    romnr = romnr1.get()

    m_eks = ('INSERT INTO eksamen (emnekode, dato, romnr) '
             'SELECT * FROM (SELECT %s, %s, %s) AS tmp '
             'WHERE NOT EXISTS ( '
             'SELECT dato, romnr FROM eksamen WHERE dato = %s and romnr=%s '
             ') LIMIT 1 '
             )

    d_eks = (emnekode, dato, romnr, dato, romnr)

    marker.execute(m_eks, d_eks)
    mydb.commit()

    marker.close()


def add_eksres(stud, kar):
    stud.bind()
    kar.bind()

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

    stud.delete(0, 'end')
    kar.delete(0, 'end')


def adm_eksamen_gui():
    adm_eks = Toplevel()
    adm_eks.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_eks, text='Administrering av Eksamen').grid(column=0, columnspan=1, row=0, pady=15, padx=15,
                                                              sticky='WE')

    # Oppretter en Notebook-widget
    n = ttk.Notebook(adm_eks)
    n.grid(row=1, column=0, columnspan=4, rowspan=6, sticky='NESW')
    f1 = ttk.Frame(n)  # første side
    f2 = ttk.Frame(n)  # andre side

    n.add(f1, text='Ajourhold fremtidige eksamner')
    n.add(f2, text='Endre oppsatt eksamen')

    # Side 1 i notebook
    ttk.Label(f1, text='Emnekode:').grid(row=0, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=emne1, width=15).grid(row=0, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f1, text='Dato:').grid(row=1, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=dato1, width=15).grid(row=1, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f1, text='RomNr:').grid(row=2, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=romnr1, width=15).grid(row=2, column=1, padx=5, pady=5, sticky=W)

    ttk.Button(f1, text='Legg til eksamen', command=add_eksamen).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f1, justify='left', text='Oversikt over alle \n oppsatte eksamner').grid(row=4, column=2, padx=25,
                                                                                       pady=10, sticky=(N, W))
    ttk.Button(f1, text='Klikk her!', command=lambda: utskrift_eksamen(tree)).grid(row=4, column=2, padx=25,
                                                                                           pady=50, sticky=(N, W))
    tree = ttk.Treeview(f1)

    tree["columns"] = ("1", "2", "3")
    tree.column("#0", anchor="w", width=0)
    tree.column("#1", width=70)
    tree.column("#2", width=75)
    tree.column("#3", width=75)
    tree.heading("#1", text="Emnekode")
    tree.heading("#2", text="Dato")
    tree.heading("#3", text="RomNr")

    ysb = ttk.Scrollbar(f1, orient=VERTICAL, command=tree.yview)

    tree['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree.grid(row=4, column=0, columnspan=2, pady=7, sticky=NSEW)
    ysb.grid(row=4, column=2, pady=7, sticky=(N, S, W))

    p = ttk.Panedwindow(f1, orient=VERTICAL)
    p.grid(row=1, column=2, columnspan=1, rowspan=2, padx=10, sticky=W)
    l = ttk.Labelframe(p, text='Info', width=50, height=100)
    p.add(l)
    l2 = Label(l, justify='left', text="Fyll inn alle feltene med \n"
                                       "riktig informasjon om \n "
                                       "eksamen, og klikk \n"
                                       "'Legg til eksamensresultat'")
    l2.grid(row=0, column=0)

    # Side 2 i notebook


    # Avslutt-knapp for toplevel
    ttk.Button(adm_eks, text='Lukk vinduet', command=adm_eks.destroy).grid(row=8, column=2, padx=5, pady=5, sticky=E)


def oversikt_rom(tree):
    tree.bind()
    for i in tree.get_children():
        tree.delete(str(i))
    marker = mydb.cursor()

    marker.execute(
        'SELECT * '
        'FROM Rom ')

    for row in marker:
        tree.insert('', 'end', values=(row[0], row[1]))

    marker.close()


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


def adm_rom_gui():
    adm_rom = Toplevel()
    adm_rom.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_rom, text="Administrering av Rom").grid(column=0, columnspan=2, row=0, pady=15, padx=15, sticky='WE')

    ttk.Separator(adm_rom).grid(row=2, column=0, columnspan=6, pady=5, sticky=(W, E))

    ttk.Label(adm_rom, text='RomNr:').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_rom, textvariable=romnr1, width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(adm_rom, text='AntallPlasser:').grid(row=4, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_rom, textvariable=antallplasser1, width=15).grid(row=4, column=1, padx=5, pady=5, sticky=W)

    ttk.Button(adm_rom, text='Legg til rom', command=add_rom).grid(row=5, column=1, padx=10, pady=7, sticky=W)

    ttk.Label(adm_rom, text="Oversikt over alle rom:").grid(row=6, column=3, padx=10, pady=10, sticky=(N, W))
    ttk.Button(adm_rom, text='Klikk her!', command=lambda: oversikt_rom(tree)).grid(row=6, column=3, padx=10, pady=30,
                                                                                    sticky=(N, W))
    # Lager en infoboks som skal gi informasjon til brukeren
    p = ttk.Panedwindow(adm_rom, orient=VERTICAL)
    p.grid(row=3, column=3, rowspan=3, padx=20)
    l1 = ttk.Labelframe(p, text='Info', width=125, height=100)
    p.add(l1)
    l = Label(l1, justify='left', text="Fyll inn alle feltene med \n"
                                       "riktig informasjon om \n "
                                       "rommet, og klikk \n"
                                       "'Legg til rom'")
    l.grid(row=0, column=0)

    # Lager Treeview-widget
    tree = ttk.Treeview(adm_rom)

    tree["columns"] = ("1", "2")
    tree.column("#0", anchor="w", width=1)
    tree.column("#1", width=20)
    tree.column("#2", width=40)
    tree.heading("#1", text="Romnr")
    tree.heading("#2", text="Antall plasser")

    ysb = ttk.Scrollbar(adm_rom, orient=VERTICAL, command=tree.yview)

    tree['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree.grid(row=6, column=0, columnspan=2, pady=7, sticky=NSEW)
    ysb.grid(row=6, column=2, pady=7, sticky=NS)

    ttk.Separator(adm_rom).grid(row=8, column=0, columnspan=6, sticky=(W, E))
    ttk.Button(adm_rom, text='Lukk vinduet', command=adm_rom.destroy).grid(row=9, column=3, padx=5, pady=10, sticky=E)


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


def oversikt_emne(tree_emne):
    tree_emne.bind()
    for i in tree_emne.get_children():
        tree_emne.delete(str(i))
    marker = mydb.cursor()

    m_emne = ('SELECT * '
              'FROM Emne '
              'ORDER BY Emnekode ASC;')

    marker.execute(m_emne)

    for row in marker:
        tree_emne.insert('', 'end', values=(row[0], row[1], row[2]))

    marker.close()


# GUI for administrering av emne
def adm_emne_gui():
    # Oppretter en toplevel-frame
    adm_emne = Toplevel()
    adm_emne.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_emne, text="Administrering av Emne").grid(column=0, columnspan=3, row=0, pady=15, padx=15,
                                                            sticky=(W, E))
    ttk.Separator(adm_emne).grid(row=2, column=0, columnspan=4, pady=5, sticky=(W, E))

    # Lager en infoboks som skal gi informasjon til brukeren
    p = ttk.Panedwindow(adm_emne, orient=VERTICAL)
    p.grid(row=3, column=2, columnspan=2, rowspan=4, padx=20)
    l1 = ttk.Labelframe(p, text='Info', width=125, height=100)
    p.add(l1)
    l = Label(l1, justify='left', text="Fyll inn alle feltene med \n"
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

    # Lager button som legger inn strengene i databasen
    ttk.Button(adm_emne, text='Legg til emne', command=add_emne).grid(row=7, column=1, columnspan=2, padx=5, pady=7,
                                                                      sticky=W)
    # Lager Treeview-widget
    tree_emne = ttk.Treeview(adm_emne)

    tree_emne["columns"] = ("1", "2", "3")
    tree_emne.column("#0", anchor="w", width=0)
    tree_emne.column("#1", width=65)
    tree_emne.column("#2", width=75)
    tree_emne.column("#3", width=95)
    tree_emne.heading("#1", text="Emnekode")
    tree_emne.heading("#2", text="Emnenavn")
    tree_emne.heading("#3", text="Studiepoeng")

    ysb = ttk.Scrollbar(adm_emne, orient=VERTICAL, command=tree_emne.yview)
    tree_emne['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree_emne.grid(row=9, column=0, columnspan=2, pady=10, sticky=NSEW)
    ysb.grid(row=9, column=2, pady=10, sticky=(N, S, W))

    ttk.Label(adm_emne, text='Oversikt over alle emner:').grid(row=9, column=2, padx=25, pady=10, sticky=(N, W))

    # Lager button som skriver ut oversikt over alle emner
    ttk.Button(adm_emne, text='Klikk her!', command=lambda: oversikt_emne(tree_emne)).grid(row=9, column=2, padx=25,
                                                                                           pady=30,
                                                                                           sticky=(N, W))

    ttk.Separator(adm_emne).grid(row=10, column=0, columnspan=3, sticky=(W, E))

    # Lager button som gjør at brukeren kan gå tilbake til hovedmeny
    ttk.Button(adm_emne, text='Lukk vinduet', command=adm_emne.destroy).grid(row=11, column=2, padx=5, pady=15,
                                                                             sticky=E)


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
              'WHERE Studentnr = %s AND %s NOT IN (SELECT Studentnr FROM Eksamensresultat)')
    d_stud = (studentnr, studentnr)

    # Legger strengene inn i databasen
    marker.execute(m_stud, d_stud)
    mydb.commit()

    # Lukker cursor
    marker.close()


# GUI for administrering av student
def adm_stud_gui():
    # Oppretter en toplevel-frame
    adm_stud = Toplevel()
    adm_stud.title('Eksamensadministrasjonsapplikasjon')

    ttk.Label(adm_stud, text="Administrering av Studenter").grid(column=0, row=0, pady=15, padx=15, sticky=(W, E))

    # Oppretter en Notebook-widget
    n = ttk.Notebook(adm_stud)
    n.grid(row=1, column=0, columnspan=4, rowspan=6, sticky='NESW')
    f1 = ttk.Frame(n)  # første side
    f2 = ttk.Frame(n)  # andre side

    n.add(f1, text='Legg til/oppdater student')
    n.add(f2, text='Slett eksisterende student')

    # Oppretter Panedwindow for Notebook side 1 og legger inn veiledende tekst
    p1 = ttk.Panedwindow(f1, orient=VERTICAL)
    p1.grid(row=3, column=3, columnspan=3, rowspan=6, padx=20, pady=10)
    l1 = ttk.Labelframe(p1, text='Ny student', width=150, height=100)
    p1.add(l1)
    label = Label(l1, justify='left', text="Fyll inn alle feltene med riktig \n"
                                           "informasjon om studenten, \n"
                                           "og klikk 'Legg til student'!")
    label.grid(row=0, column=0)

    l2 = ttk.Labelframe(p1, text='Oppdater student', width=150, height=100)
    p1.add(l2)
    label2 = Label(l2, justify='left', text="Fyll ut studentnr på studenten som \n"
                                            "skal endres, og fyll ut resterende \n"
                                            "felter med oppdatert informasjon. \n"
                                            "Og klikk på 'Oppdater student'")
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
    label3 = Label(l3, justify='left', text="NB! Studenter med eksamensresultater\n"
                                            "går ikke å slette! \n"
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
ttk.Button(mainframe, text="Rom", command=adm_rom_gui).grid(column=1, row=4, padx=20, sticky=W)

ttk.Label(mainframe, text="Administrer Eksamener").grid(column=0, row=5, sticky=(E, W))
ttk.Button(mainframe, text="Eksamener", command=adm_eksamen_gui).grid(column=1, row=5, padx=20, sticky=W)

ttk.Label(mainframe, text="Administrer Karakterer").grid(column=0, row=6, sticky=(E, W))
ttk.Button(mainframe, text="Karakterer", command=adm_kar_gui).grid(column=1, row=6, padx=20, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=7, columnspan=3, sticky=(W, E))

ttk.Label(mainframe, text="Utskrifter av oversikter").grid(column=0, row=8, sticky=(E, W))
ttk.Button(mainframe, text="Oversikter", command=utskrifter).grid(column=1, row=8, padx=20, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=9, columnspan=3, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy).grid(column=2, row=10, padx=20, sticky=E, )

tekst = Text(mainframe, width=26, height=10, wrap="word")
tekst.grid(column=2, row=2, rowspan=5)
tekst.insert('1.0', 'Fra denne siden kan du redigere alle aspekter av eksamensinformasjonen. På administrer studenter'
                    ' kan du legge til, endre eller slette studenter')

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

# Strenger for rom
romnr1 = StringVar()
antallplasser1 = StringVar()

# Strenger for emne
studentnr1 = StringVar()
emne1 = StringVar()
dato1 = StringVar()
karakter1 = StringVar()
emne_2 = StringVar()

# Strenger for eksamen
emne1 = StringVar()
dato1 = StringVar()
romnr1 = StringVar()

# Strenger for utskrift eksamen
fra_dag1 = StringVar()
fra_maaned1 = StringVar()
fra_aar1 = StringVar()
til_dag1 = StringVar()
til_maaned1 = StringVar()
til_aar1 = StringVar()

root.mainloop()
