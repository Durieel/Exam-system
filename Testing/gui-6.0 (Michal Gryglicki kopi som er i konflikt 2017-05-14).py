from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


# Fikse dato felter fra singel til trippel
# Legge til oversikt på Student over alle studenter på skolen
# Finpusse GUI

# Utskrift for Notebook side 1
def utskrift_emneres(tree1):
    # Binder Treeview
    tree1.bind()

    # Sletter innholdet i Treeviewet før ny gjennomgang
    for i in tree1.get_children():
        tree1.delete(str(i))

    # Opretter cursor
    marker = mydb.cursor()

    # Henter String
    emne = emnekode_utskriftside1.get()

    # Lager variabel for MySQL-kode
    m_emneres = ('SELECT Studentnr, Dato, Karakter '
                 'FROM Eksamensresultat '
                 'WHERE Emnekode = %s '
                 'ORDER BY Studentnr ASC')

    # Lager variabel for input til MySQL
    d_emneres = emne

    # Utfører handlingen i databasen
    marker.execute(m_emneres, d_emneres)

    # Henter informasjon fra databsen inn i Treeviewet
    for row in marker:
        tree1.insert('', 'end', values=(row[0], row[1], row[2]))

    # Lukker cursor
    marker.close()


# Utskrift for Notebook side 2
def utskrift_eks_student(tree2):
    # Binder Treeview
    tree2.bind()

    # Sletter innholdet i Treeviewet før ny gjennomgang
    for i in tree2.get_children():
        tree2.delete(str(i))

    # Opretter cursor
    marker = mydb.cursor()

    # Henter String
    studentnr = studentnr_utskriftside2.get()

    # Lager variabel for MySQL-kode
    m_eks_student = ('SELECT Dato, Karakter, Emnenavn, Studiepoeng '
                     'FROM Eksamensresultat, Emne '
                     'WHERE Studentnr=%s AND Eksamensresultat.Emnekode=Emne.Emnekode '
                     'ORDER BY Dato DESC')

    # Lager variabel for input til MySQL
    d_eks_student = studentnr

    # Utfører handlingen i databasen
    marker.execute(m_eks_student, d_eks_student)

    # Henter informasjon fra databsen inn i Treeviewet
    for row in marker:
        tree2.insert('', 'end', values=(row[0], row[1], row[2], row[3]))

    # Lukker cursor
    marker.close()


# Utskrift for Notebook side 3
def utskrift_eksamen_pd(tree3, fra_aar_utskriftside3, fra_m_utskriftside3, fra_d_utskriftside3, til_aar_utskriftside3,
                        til_m_utskriftside3, til_d_utskriftside3):
    # Binder Treeviewet
    tree3.bind()

    # Sletter innholdet i Treeviewet før ny gjennomgang
    for i in tree3.get_children():
        tree3.delete(str(i))

    # Oppretter cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    fra_aar1 = fra_aar_utskriftside3.get()
    fra_maaned1 = fra_m_utskriftside3.get()
    fra_dag1 = fra_d_utskriftside3.get()
    til_aar1 = til_aar_utskriftside3.get()
    til_maaned1 = til_m_utskriftside3.get()
    til_dag1 = til_d_utskriftside3.get()

    til_dato = til_aar1 + til_maaned1 + til_dag1
    fra_dato = fra_aar1 + fra_maaned1 + fra_dag1

    if til_dato == '':

        # Lager variabel for MySQL-kode
        m_utskrift = (
            'SELECT Eksamen.Emnekode, Emnenavn, Eksamen.Romnr, Antallplasser, Eksamen.dato, COUNT(Oppmeldte.Studentnr) '
            'FROM Eksamen, Rom, Emne, Oppmeldte '
            'WHERE Eksamen.Dato = %s AND Eksamen.Romnr = Rom.Romnr '
            'AND Eksamen.Emnekode = Emne.Emnekode '
            'AND Eksamen.Emnekode = Oppmeldte.Emnekode '
            'AND Oppmeldte.Dato = Eksamen.Dato '
            'GROUP BY Eksamen.Dato DESC')

        # Lager variabel for input til MySQL
        d_utskrift = fra_dato

        # Utfører handlingen i databasen
        marker.execute(m_utskrift, d_utskrift)
        mydb.commit()

        # Henter informasjon fra databsen inn i Treeviewet
        for row in marker:
            tree3.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        # Lager en messagebox som gir informasjon om at antall oppmeldte er over antall plasser på rommet
        if row[5] > row[3]:
            messagebox.showinfo(message='Antall oppmeldte overskrider plasser på rommet')
        # Lukker cursor
        marker.close()

    else:
        if til_dato != '':

            # Lager variabel for MySQL-kode
            m_utskrift = (
                'SELECT Eksamen.Emnekode, Emnenavn, Eksamen.Romnr, Antallplasser, Eksamen.Dato, COUNT(Oppmeldte.Studentnr) '
                'FROM Eksamen, Rom, Emne, Oppmeldte '
                'WHERE Eksamen.Dato >= %s AND Eksamen.Dato <= %s '
                'AND Eksamen.Romnr = Rom.Romnr '
                'AND Eksamen.Emnekode = Emne.Emnekode '
                'AND Eksamen.Emnekode = Oppmeldte.Emnekode '
                'AND Oppmeldte.Dato = Eksamen.Dato '
                'GROUP BY Dato DESC')

            # Lager variabel for input til MySQL
            d_utskrift = fra_dato, til_dato

            # Utfører handlingen i databasen
            marker.execute(m_utskrift, d_utskrift)
            mydb.commit()

            # Henter informasjon fra databsen inn i Treeviewet
            for row in marker:
                tree3.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5]))

            # Lukker cursor
            marker.close()


# Utskrift for Notebook side 4
def utskrift_karstat(emnekode_utskriftside4, dato_aar_utskriftside4, dato_m_utskriftside4, dato_d_utskriftside4, tree4):
    # Binder Treeviewet
    tree4.bind()

    # Sletter innholdet i Treeviewet før ny gjennomgang
    for i in tree4.get_children():
        tree4.delete(str(i))

    # Oppretter cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    emnekode = emnekode_utskriftside4.get()
    dato1 = dato_aar_utskriftside4.get()
    dato2 = dato_m_utskriftside4.get()
    dato3 = dato_d_utskriftside4.get()

    dato_tot = dato1 + dato2 + dato3

    # Lager variabel for MySQL-kode
    m_karstat = (
        'SELECT Emnenavn, Karakter, COUNT(*) '
        'FROM Eksamensresultat, Emne '
        'WHERE Dato=%s '
        'AND Eksamensresultat.Emnekode = %s '
        'AND Eksamensresultat.Emnekode = Emne.Emnekode '
        'GROUP BY Karakter'
    )

    # Lager variabel for input til MySQL
    d_karstat = (dato_tot, emnekode)

    # Utfører handlingen i databasen
    marker.execute(m_karstat, d_karstat)

    # Henter informasjon fra databsen inn i Treeviewet
    for row in marker:
        tree4.insert('', 'end', values=(row[0], row[1], row[2]))

    # Lukker cursor
    marker.close()


# Utskrift for Notebook side 5
def utskrift_stud_emne(tree5):
    # Binder Treeviewet
    tree5.bind()

    # Sletter innholdet i Treeviewet før ny gjennomgang
    for i in tree5.get_children():
        tree5.delete(str(i))

    # Oppretter cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    emne2 = emnekode_utskriftside5.get()

    # Lager variabel for MySQL-kode
    m_stud_emne = ('SELECT Student.Studentnr, Fornavn, Etternavn, Eksamensresultat.Emnekode, Emnenavn '
                'FROM Student, Eksamensresultat, Emne '
                'WHERE Eksamensresultat.Emnekode = %s '
                'AND Student.Studentnr = Eksamensresultat.Studentnr '
                'AND Eksamensresultat.Emnekode = Emne.Emnekode '
                'ORDER BY Etternavn asc')

    # Lager variabel for input til MySQL
    d_stud_emne = (emne2, emne2)

    # Utfører handlingen i databasen
    marker.execute(m_stud_emne, d_stud_emne)

    # Henter informasjon fra databsen inn i Treeviewet
    for row in marker:
        tree5.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))

    # Lukker cursor
    marker.close()


# Utskrift for Notebook side 6
def utskrift_vit(tree6, fornavn_vit, etternavn_vit, total_vit):
    # Binder Treeviewet
    tree6.bind()
    fornavn_vit.bind()
    etternavn_vit.bind()
    total_vit.bind()
    studentnr = studentnr_utskriftside6.get()

    # Sletter textboxene før neste gjennomgang
    fornavn_vit.delete('1.0', 'end')
    etternavn_vit.delete('1.0', 'end')
    total_vit.delete('1.0', 'end')

    # Sletter innholdet i Treeviewet
    for i in tree6.get_children():
        tree6.delete(str(i))

    # Oppretter cursor for vitnemål
    marker_vit = mydb.cursor()

    # Lager variabel for MySQL-kode
    m_vit = ('SELECT Eksamensresultat.Emnekode, Emnenavn, Studiepoeng, MIN(Karakter) '
             'FROM Emne LEFT OUTER JOIN Eksamensresultat ON Emne.Emnekode = Eksamensresultat.Emnekode '
             'WHERE Studentnr = %s '
             'GROUP BY Eksamensresultat.Emnekode, Emnenavn')

    # Lager variabel for input til MySQL
    d_vit = studentnr

    # Utfører handlingen i databasen
    marker_vit.execute(m_vit, d_vit)

    # Henter informasjon fra databsen inn i Treeviewet
    for row in marker_vit:
        tree6.insert('', 'end', values=(row[0], row[1], row[2], row[3]))

    # Lukker cursor
    marker_vit.close()

    # Oppretter cursor for Fornavn Entryen
    marker_fornavn = mydb.cursor()

    m_fornavn = ('SELECT Fornavn '
                 'FROM Student '
                 'WHERE Studentnr = %s')

    d_fornavn = studentnr

    marker_fornavn.execute(m_fornavn, d_fornavn)

    for row in marker_fornavn:
        fornavn_vit.insert('1.0', row)
    marker_fornavn.close()

    # Oppretter cursor for Etternavn Entryen
    marker_etternavn = mydb.cursor()

    m_etternavn = ('SELECT Etternavn '
                   'FROM Student '
                   'WHERE Studentnr = %s')

    d_etternavn = studentnr

    marker_etternavn.execute(m_etternavn, d_etternavn)

    for row in marker_etternavn:
        etternavn_vit.insert('1.0', row)
    marker_etternavn.close()

    # Oppretter cursor for Totalt studiepoeng Entryen
    marker_total = mydb.cursor()
    m_total = ("SELECT SUM(Studiepoeng) "
               "FROM Emne "
               "WHERE EXISTS (SELECT Studentnr FROM Eksamensresultat WHERE Studentnr = %s "
               "AND Eksamensresultat.Emnekode = Emne.Emnekode "
               "AND Karakter != 'F')")

    d_total = studentnr

    marker_total.execute(m_total, d_total)

    for row in marker_total:
        total_vit.insert('1.0', row)
    marker_total.close()


# GUI for utskrifter
def utskrifter():
    # Oppretter en toplevel-frame
    utskrift = Toplevel()
    utskrift.title('Oversikter')

    ttk.Label(utskrift, text='Oversikt over utskrifter', font=('Calibri', '16')).grid(row=0, column=0, columnspan=2,
                                                                                      pady=10)

    # Oppretter en Notebook-widget
    n = ttk.Notebook(utskrift)
    n.grid(row=1, column=0, columnspan=2, rowspan=6, sticky='NESW')
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
    # Labels og entries for side 1
    # Lager et panewindow som skal gi informasjon til brukeren
    ttk.Label(f1, text="Alle eksamensresultater i et emne", font=('Calibri', '14')).grid(column=0, columnspan=3, row=0,
                                                                                         pady=15, padx=15)

    ttk.Separator(f1).grid(row=1, column=0, columnspan=3, pady=5, sticky=(W, E))

    p1 = ttk.Panedwindow(f1, orient=VERTICAL, width=220, height=45)
    p1.grid(row=2, column=0, padx=40, pady=5, rowspan=2, columnspan=2, sticky=W)
    l1 = ttk.Labelframe(p1, text='Info', width=340, height=55)
    p1.add(l1)
    label = Label(l1, justify='left', text="Skriv inn emnekode og klikk 'Utfør'")
    label.grid(row=0, column=0)

    ttk.Label(f1, text='Emnekode:').grid(row=2, column=0, columnspan=2, padx=90, pady=5, sticky=E)
    ttk.Entry(f1, textvariable=emnekode_utskriftside1, width=9).grid(row=2, column=1, pady=5, sticky=E)

    ttk.Button(f1, text='Utfør', command=lambda: utskrift_emneres(tree1)).grid(row=3, column=1, columnspan=2, padx=10,
                                                                               pady=10, sticky=E)

    # Oppretter treeview
    tree1 = ttk.Treeview(f1)

    tree1["columns"] = ("1", "2", "3")
    tree1.column("#0", anchor="w", width=0)
    tree1.column("#1", width=150)
    tree1.column("#2", width=150)
    tree1.column("#3", width=150)
    tree1.heading("#1", text="Studentnr")
    tree1.heading("#2", text="Dato")
    tree1.heading("#3", text="Karakter")

    # Lager scrollbar til viewet
    ysb = ttk.Scrollbar(f1, orient=VERTICAL, command=tree1.yview)
    tree1['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree1.grid(row=5, column=0, columnspan=2, sticky=NSEW)
    ysb.grid(row=5, column=2, sticky=(N, S))

    ###############################################################################################################

    # Side 2 i notebook er eksamensresultater for en student
    # Labels og entries for side 2
    # Lager et panewindow som skal gi informasjon til brukeren
    ttk.Label(f2, text="Eksamensresultater for en student", font=('Calibri', '14')).grid(column=0, columnspan=3, row=0,
                                                                                         pady=15, padx=15)

    ttk.Separator(f2).grid(row=1, column=0, columnspan=4, pady=5, sticky=(W, E))

    p1 = ttk.Panedwindow(f2, orient=VERTICAL, width=260, height=45)
    p1.grid(row=2, column=0, padx=100, pady=5, rowspan=2, columnspan=2, sticky=E)
    l1 = ttk.Labelframe(p1, text='Info', width=340, height=55)
    p1.add(l1)
    label = Label(l1, justify='left', text="Skriv inn studentnummer og klikk 'Utfør'")
    label.grid(row=0, column=0)

    ttk.Label(f2, text='Studentnr:').grid(row=2, column=2, padx=95, pady=5, sticky=E)
    ttk.Entry(f2, textvariable=studentnr_utskriftside2, width=9).grid(row=2, column=2, padx=10, pady=5, sticky=E)

    ttk.Button(f2, text='Utfør', command=lambda: utskrift_eks_student(tree2)).grid(row=3, column=2, padx=7,
                                                                                   pady=15, sticky=E)

    # Oppretter treeview
    tree2 = ttk.Treeview(f2)

    tree2["columns"] = ("1", "2", "3", "4")
    tree2.column("#0", anchor="w", width=0)
    tree2.column("#1", width=150)
    tree2.column("#2", width=150)
    tree2.column("#3", width=175)
    tree2.column("#4", width=150)
    tree2.heading("#1", text="Dato")
    tree2.heading("#2", text="Karakter")
    tree2.heading("#3", text="Emnenavn")
    tree2.heading("#4", text="Studiepoeng")

    # Lager scrollbar til viewet
    ysb = ttk.Scrollbar(f2, orient=VERTICAL, command=tree2.yview)
    tree2['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree2.grid(row=4, column=0, columnspan=3, sticky=NSEW)
    ysb.grid(row=4, column=3, sticky=NS)

    ###############################################################################################################

    # Side 3 i notebook er eksamner i perioder eller dag
    # Labels og entries for side 3
    # Lager et panewindow som skal gi informasjon til brukeren
    ttk.Label(f3, text="Utskrift av eksamner i en periode/dag", font=('Calibri', '14')).grid(column=0, columnspan=4,
                                                                                             row=0, pady=15, padx=15)
    ttk.Separator(f3).grid(row=1, column=0, columnspan=6, pady=5, sticky=(W, E))

    p1 = ttk.Panedwindow(f3, orient=VERTICAL, width=340, height=55)
    p1.grid(row=2, column=0, padx=10, pady=5, sticky=E, rowspan=4, columnspan=3)
    l1 = ttk.Labelframe(p1, text='Info', width=340, height=55)
    p1.add(l1)
    label = Label(l1, justify='left', text="Ved eksamen i en periode skriv inn fra og til dato.\n"
                                           "Hvis du vil ha en spesifikk dag skriv inn kun fra dato")
    label.grid(row=0, column=0)

    # label fra og til
    l = Label(f3, text="Fra")
    l.grid(column=2, row=3, columnspan=4, padx=150, sticky=E)
    l2 = Label(f3, text="Formatet YYYY/MM/DD")
    l2.grid(column=2, row=2, sticky=E, columnspan=4, padx=30)
    l3 = Label(f3, text="Til")
    l3.grid(column=2, row=4, columnspan=4, padx=150, sticky=E)

    # fra dato
    fra_aar_utskriftside3 = StringVar()
    ttk.Entry(f3, textvariable=fra_aar_utskriftside3, width=5)\
        .grid(column=2, row=3, columnspan=4, padx=80, pady=5, sticky=(N, E))

    fra_m_utskriftside3 = StringVar()
    ttk.Entry(f3, textvariable=fra_m_utskriftside3, width=3)\
        .grid(column=2, row=3, columnspan=4, padx=45, pady=5, sticky=(N, E))

    fra_d_utskriftside3 = StringVar()
    ttk.Entry(f3, textvariable=fra_d_utskriftside3, width=3)\
        .grid(column=2, row=3, columnspan=4, padx=10, pady=5, sticky=(N, E))

    # til dato
    til_aar_utskriftside3 = StringVar()
    ttk.Entry(f3, textvariable=til_aar_utskriftside3, width=5)\
        .grid(column=2, row=4, columnspan=4, padx=80, pady=5, sticky=(N, E))

    til_m_utskriftside3 = StringVar()
    ttk.Entry(f3, textvariable=til_m_utskriftside3, width=3)\
        .grid(column=2, row=4, columnspan=4, padx=45, pady=5, sticky=(N, E))

    til_d_utskriftside3 = StringVar()
    ttk.Entry(f3, textvariable=til_d_utskriftside3, width=3)\
        .grid(column=2, row=4, columnspan=4, padx=10, pady=5, sticky=(N, E))

    # Lager Treeview-widget
    tree3 = ttk.Treeview(f3)

    tree3["columns"] = ("1", "2", "3", "4", "5", "6")
    tree3.column("#0", anchor="w", width=0)
    tree3.column("#1", width=100)
    tree3.column("#2", width=200)
    tree3.column("#3", width=100)
    tree3.column("#4", width=100)
    tree3.column("#5", width=125)
    tree3.column("#6", width=125)
    tree3.heading("#1", text="Emnekode")
    tree3.heading("#2", text="Emnenavn")
    tree3.heading("#3", text="Romnr")
    tree3.heading("#4", text="Antall plasser")
    tree3.heading("#5", text="Dato")
    tree3.heading("#6", text="Antall oppmeldte")

    # Lager scrollbar til viewet
    ysb = ttk.Scrollbar(f3, orient=VERTICAL, command=tree3.yview)
    tree3['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree3.grid(row=6, column=0, columnspan=5, sticky=NSEW)
    ysb.grid(row=6, column=5, sticky=(N, S, W))

    ttk.Button(f3, text='Utfør',
               command=lambda: utskrift_eksamen_pd(tree3, fra_aar_utskriftside3, fra_m_utskriftside3, fra_d_utskriftside3,
                                                   til_aar_utskriftside3, til_m_utskriftside3,
                                                   til_d_utskriftside3))\
        .grid(column=3, row=5, columnspan=2, padx=25, pady=10, sticky=E)

    ###############################################################################################################

    # Side 4 i notebook er karakterstatistikk
    # Labels og entries for side 4
    # Lager et panewindow som skal gi informasjon til brukeren
    ttk.Label(f4, text='Karakterstatistikk for en eksamen', font=('Calibri', '14')).grid(column=0, columnspan=4, row=0,
                                                                                         pady=15, padx=15)

    ttk.Separator(f4).grid(row=1, column=0, columnspan=4, pady=5, sticky=(W, E))

    p1 = ttk.Panedwindow(f4, orient=VERTICAL, width=390, height=55)
    p1.grid(row=2, column=0, padx=10, pady=5, sticky=E, columnspan=3)
    l1 = ttk.Labelframe(p1, text='Info', width=390, height=55)
    p1.add(l1)
    label = Label(l1, justify='left', text="Skriv inn emnekode og dato, deretter klikk på knappen 'Utfør'.\n"
                                           "Dato skrives i format YYYY/MM/DD ")
    label.grid(row=0, column=0)

    ttk.Label(f4, text='Emnekode:').grid(row=3, column=2, columnspan=2, padx=140, pady=5, sticky=E)
    emnekode_utskriftside4 = StringVar()
    ttk.Entry(f4, textvariable=emnekode_utskriftside4, width=14)\
        .grid(row=3, column=2, columnspan=2, padx=10, pady=5, sticky=E)
    ttk.Label(f4, text='Dato:').grid(row=4, column=2, columnspan=2, padx=140, pady=5, sticky=E)
    dato_aar_utskriftside4 = StringVar()
    ttk.Entry(f4, textvariable=dato_aar_utskriftside4, width=5)\
        .grid(column=2, row=4, columnspan=2, padx=80, pady=5, sticky=(N, E))
    dato_m_utskriftside4 = StringVar()
    ttk.Entry(f4, textvariable=dato_m_utskriftside4, width=3)\
        .grid(column=2, row=4, columnspan=2, padx=45, pady=5, sticky=(N, E))
    dato_d_utskriftside4 = StringVar()
    ttk.Entry(f4, textvariable=dato_d_utskriftside4, width=3)\
        .grid(column=2, row=4, columnspan=2, padx=10, pady=5, sticky=(N, E))

    # Lager Treeview-widget
    tree4 = ttk.Treeview(f4)

    tree4["columns"] = ("1", "2", "3")
    tree4.column("#0", anchor="w", width=0)
    tree4.column("#1", width=175)
    tree4.column("#2", width=125)
    tree4.column("#3", width=125)
    tree4.heading("#1", text="Emnenavn")
    tree4.heading("#2", text="Karakter")
    tree4.heading("#3", text="Antall")

    # Lager scrollbar til viewet
    ysb = ttk.Scrollbar(f4, orient=VERTICAL, command=tree4.yview)

    tree4['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree4.grid(row=6, column=0, columnspan=3, pady=7, sticky=NSEW)
    ysb.grid(row=6, column=3, pady=7, sticky=(W, N, S))

    ttk.Button(f4, text='Utfør',
               command=lambda: utskrift_karstat(emnekode_utskriftside4, dato_aar_utskriftside4, dato_m_utskriftside4,
                                                dato_d_utskriftside4, tree4))\
        .grid(row=5, column=2, columnspan=2, padx=25, pady=5, sticky=E)

    ###############################################################################################################

    # Side 5 i notebook er studenter i et emne
    # Labels og entries for side 4
    # Lager et panewindow som skal gi informasjon til brukeren
    ttk.Label(f5, text="En oversikt som viser studenter som har utført et emne", font=('Calibri', '14'))\
        .grid(column=0, columnspan=3, row=0, pady=15, padx=15)

    ttk.Separator(f5).grid(row=1, column=0, columnspan=4, pady=5, sticky=(W, E))

    ttk.Label(f5, text='Emnekode:').grid(row=2, column=2, padx=100, pady=5, sticky=E)
    ttk.Entry(f5, textvariable=emnekode_utskriftside5, width=9).grid(row=2, column=2, padx=10, pady=5, sticky=E)

    ttk.Button(f5, text='Utfør', command=lambda: utskrift_stud_emne(tree5))\
        .grid(row=3, column=2, padx=7, pady=15, sticky=E)

    p1 = ttk.Panedwindow(f5, orient=VERTICAL, width=260, height=45)
    p1.grid(row=2, column=0, padx=100, pady=5, rowspan=2, columnspan=2, sticky=E)
    l1 = ttk.Labelframe(p1, text='Info', width=340, height=55)
    p1.add(l1)
    label = Label(l1, justify='left', text="Skriv inn emnekode og klikk 'Utfør'")
    label.grid(row=0, column=0)

    # Oppretter treeview
    tree5 = ttk.Treeview(f5)

    tree5["columns"] = ("1", "2", "3", "4", "5")
    tree5.column("#0", anchor="w", width=0)
    tree5.column("#1", width=100)
    tree5.column("#2", width=175)
    tree5.column("#3", width=175)
    tree5.column("#4", width=100)
    tree5.column("#5", width=200)
    tree5.heading("#1", text="Studentnr")
    tree5.heading("#2", text="Fornavn")
    tree5.heading("#3", text="Etternavn")
    tree5.heading("#4", text="Emnekode")
    tree5.heading("#5", text="Emnenavn")

    ysb = ttk.Scrollbar(f5, orient=VERTICAL, command=tree1.yview)
    tree5['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree5.grid(row=4, column=0, columnspan=3, sticky=NSEW)
    ysb.grid(row=4, column=4, sticky=NS)

    ###############################################################################################################

    # Side 6 i notebook'en er vitnemål
    # Lager et panewindow som skal gi informasjon til brukeren
    ttk.Label(f6, text="Utskrift av vitnemål for en student", font=('Calibri', '14'))\
        .grid(column=0, columnspan=4, row=0, pady=15, padx=15)
    ttk.Separator(f6).grid(row=1, column=0, columnspan=8, pady=5, sticky=(W, E))

    # Lables og Entries
    ttk.Label(f6, text='Studentnr:').grid(row=2, column=2, padx=5, pady=7, sticky=W)
    ttk.Entry(f6, textvariable=studentnr_utskriftside6, width=6).grid(row=2, column=3, padx=5, pady=7, sticky=W)

    # Oppretter button som kjører mysql-queries mot databasen
    but = ttk.Button(f6, text='Utfør', command=lambda: utskrift_vit(tree6, fornavn_vit, etternavn_vit, total_vit))
    but.grid(row=3, column=2, columnspan=2, pady=15, padx=5)

    ttk.Separator(f6).grid(row=4, column=0, columnspan=8, pady=5, sticky=(W, E))

    ttk.Label(f6, text='Fornavn:').grid(row=5, column=0, padx=5, pady=7, sticky=W)
    fornavn_vit = Text(f6, width=10, height=1, wrap="word", state='normal', background='lightgrey')
    fornavn_vit.grid(row=5, column=0, columnspan=2, padx=80, pady=7, sticky=W)

    ttk.Label(f6, text='Etternavn:').grid(row=6, column=0, padx=5, pady=7, sticky=W)
    etternavn_vit = Text(f6, width=10, height=1, wrap="word", state='normal', background='lightgrey')
    etternavn_vit.grid(row=6, column=0, columnspan=2, padx=80, pady=7, sticky=W)

    # Oppretter Panedwindow for å legge inn veiledende tekst
    p = ttk.Panedwindow(f6, orient=VERTICAL)
    p.grid(row=2, column=0, columnspan=2, rowspan=2, padx=20, pady=10, sticky=W)
    l = ttk.Labelframe(p, text='Vitnemål', width=300, height=100)
    p.add(l)
    label = Label(l, text="Skriv inn studentnummer og klikk 'Utfør'")
    label.grid(row=0, column=0)

    # Lager Treeview-widget
    tree6 = ttk.Treeview(f6)

    tree6["columns"] = ("1", "2", "3", "4")
    tree6.column("#0", anchor="w", width=0)
    tree6.column("#1", width=100)
    tree6.column("#2", width=200)
    tree6.column("#3", width=100)
    tree6.column("#4", width=100)
    tree6.heading("#1", text="Emnekode")
    tree6.heading("#2", text="Emnenavn")
    tree6.heading("#3", text="Studiepoeng")
    tree6.heading("#4", text="Karakter")

    # Lager scrollbar til viewet
    ysb = ttk.Scrollbar(f6, orient=VERTICAL, command=tree6.yview)

    tree6['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree6.grid(row=7, column=0, columnspan=4, sticky=NSEW)
    ysb.grid(row=7, column=4, sticky=(N, S, E))

    # Lager en label som viser brukeren totalt studiepoeng
    ttk.Label(f6, text='Totalt studiepoeng:').grid(row=8, column=0, padx=5, pady=7, sticky=W)
    total_vit = Text(f6, width=10, height=1, wrap="word", state='normal', background='lightgrey')
    total_vit.grid(row=8, column=0, columnspan=2, padx=135, pady=7, sticky=W)

    # Lager button som gjør at brukeren kan gå tilbake til hovedmeny
    ttk.Button(utskrift, text='Lukk vinduet', command=utskrift.destroy).grid(row=9, column=1, padx=5, pady=15, sticky=E)


# MySQL-kode som endrer karakter på student i databasen
def upd_karakter():
    # Lager cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    karakter = karakter_karakterendre.get()
    studentnr = studentnr_karakterendre.get()
    emnekode = emnekode_karakterendre.get()

    # Lager variabel for MySQL-kode
    m_eks = ('UPDATE Eksamensresultat '
             'SET Karakter = %s '
             'WHERE Studentnr = %s '
             'AND Emnekode = %s '
             'ORDER BY Dato DESC '
             'LIMIT 1'
             )

    # Lager variabel for input til MySQL
    d_eks = (karakter, studentnr, emnekode)

    # Utfører handlingen i databasen
    marker.execute(m_eks, d_eks)
    mydb.commit()

    # Lukker cursor
    marker.close()


# MySQL-kode som legger til eksamensresultater for en avholdt eksamen i databasen
def add_eksres(stud, kar):
    stud.bind()
    kar.bind()

    # Oppretter cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    studentnr = studentnr_karakteradd.get()
    emnekode = emnekode_karakteradd.get()
    dato_aar = dato_aar_karakteradd.get()
    dato_m = dato_m_karakteradd.get()
    dato_d = dato_d_karakteradd.get()
    karakter = karakter_karakteradd.get()

    dato = dato_aar + dato_m + dato_d

    # Setter opp database strukturen for tabellen
    m_eksres = ('INSERT INTO Eksamensresultat'
                '(Studentnr, Emnekode, Dato, Karakter)'
                'VALUES(%s, %s, %s, %s)')

    # Lager variabel for input til MySQL
    d_eksres = (studentnr, emnekode, dato, karakter)

    # Utfører handlingen i databasen
    marker.execute(m_eksres, d_eksres)
    mydb.commit()

    # Avslutter cursor
    marker.close()

    stud.delete(0, 'end')
    kar.delete(0, 'end')


# GUI for administrasjon av karakterer
def adm_kar_gui():
    adm_kar = Toplevel()
    adm_kar.title('Administrasjon av Karakterer')

    ttk.Label(adm_kar, text='Administrering av Karakter', font=('Calibri', '16')).grid(column=0, columnspan=1, row=0,
                                                                                       pady=15, padx=15,
                                                                                       sticky='WE')

    # Oppretter en Notebook-widget
    n = ttk.Notebook(adm_kar)
    n.grid(row=1, column=0, columnspan=4, rowspan=6, sticky='NESW')
    f1 = ttk.Frame(n)  # første side
    f2 = ttk.Frame(n)  # andre side

    n.add(f1, text='Ajourhold karakter på student')
    n.add(f2, text='Registrer karakterer for avholdt eksamen')

    # Side 1 i notebook
    ttk.Separator(f1).grid(row=2, column=0, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(f1, text='Studentnr:').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=studentnr_karakterendre, width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f1, text='Emnekode:').grid(row=4, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=emnekode_karakterendre, width=15).grid(row=4, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f1, text='Karakter:').grid(row=5, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=karakter_karakterendre, width=15).grid(row=5, column=1, padx=5, pady=5, sticky=W)

    ttk.Button(f1, text='Oppdatere karakter', command=upd_karakter).grid(row=8, column=0, padx=5, pady=5, sticky=W)

    # Oppretter Panedwindow for Notebook side 1 og legger inn veiledende tekst
    p1 = ttk.Panedwindow(f1, orient=VERTICAL)
    p1.grid(row=2, column=3, columnspan=3, rowspan=6, padx=20, pady=10)
    l1 = ttk.Labelframe(p1, text='Info', width=150, height=100)
    p1.add(l1)
    label = Label(l1, justify='left', text="Fyll inn studentnr og emnekode \n"
                                           "for den studenten og det emne du \n"
                                           "vil endre karakter på ,  \n"
                                           "og klikk 'Oppdatere karakter'!")
    label.grid(row=0, column=0)

    # Side 2 i notebook
    ttk.Label(f2, text='Emnekode:').grid(row=1, column=2, padx=10, pady=5, sticky=W)
    ttk.Entry(f2, textvariable=emnekode_karakteradd, width=15).grid(row=1, column=3, padx=0, pady=5, sticky=W)

    ttk.Label(f2, text='Dato:').grid(row=2, column=2, padx=5, pady=5, sticky=W)
    ttk.Entry(f2, textvariable=dato_aar_eksamenadd, width=5).grid(column=3, row=2, padx=5, pady=5, sticky=(N, W))
    ttk.Entry(f2, textvariable=dato_m_eksamenadd, width=3).grid(column=3, row=2, padx=47, pady=5, sticky=(N, W))
    ttk.Entry(f2, textvariable=dato_d_eksamenadd, width=3).grid(column=3, row=2, padx=76, pady=5, sticky=(N, W))

    ttk.Separator(f2).grid(row=4, column=0, columnspan=5, pady=5, sticky=(W, E))

    ttk.Label(f2, text='Studentnr:').grid(row=5, column=0, padx=2, pady=5, sticky=W)
    stud = ttk.Entry(f2, textvariable=studentnr_karakteradd, width=10)
    stud.grid(row=5, column=0, padx=40, pady=5, sticky=E)

    ttk.Label(f2, text='Karakter:').grid(row=6, column=0, padx=2, pady=5, sticky=W)
    kar = ttk.Entry(f2, textvariable=karakter_karakteradd, width=10)
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

    # Lager en knapp der brukeren kan lukke vinduet
    ttk.Button(adm_kar, text='Lukk vinduet', command=adm_kar.destroy).grid(row=8, column=3, padx=5, pady=15, sticky=E)


# MySQL-kode som legger til eksamen i databasen
def add_eksamen():
    # Oppretter cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    emnekode = emnekode_eksamenadd.get()

    dato_aar = dato_aar_eksamenadd.get()
    dato_m = dato_m_eksamenadd.get()
    dato_d = dato_d_eksamenadd.get()
    romnr = romnr_eksamenadd.get()

    dato = dato_aar + dato_m + dato_d

    # Setter opp database strukturen for tabellen
    m_eks = ('INSERT INTO Eksamen (Emnekode, Dato, Romnr) '
             'SELECT * FROM (SELECT %s, %s, %s) AS tmp '
             'WHERE NOT EXISTS ('
             'SELECT Dato, Romnr FROM Eksamen WHERE Dato = %s AND Romnr = %s '
             ') LIMIT 1'
             )

    # Lager variabel for input til MySQL
    d_eks = (emnekode, dato, romnr, dato, romnr)

    # Utfører handlingen i databasen
    marker.execute(m_eks, d_eks)
    mydb.commit()

    # Avslutter cursor
    marker.close()


# MySQL-kode for utskrift av alle oppsatte eksamner
def utskrift_eksamen(tree):
    # Binder Treeviewet
    tree.bind()

    # Sletter innholdet i Treeviewet
    for i in tree.get_children():
        tree.delete(str(i))

    # Lager cursor
    marker = mydb.cursor()

    # Lager strukturen for databasen
    marker.execute(
        'SELECT * '
        'FROM Eksamen '
        'ORDER BY Dato DESC')

    # Henter informasjon fra databsen inn i Treeviewet

    for row in marker:
        tree.insert('', 'end', values=(row[0], row[1], row[2]))

    # Avslutter cursor
    marker.close()


# MySQL-kode som endrer oppsatt eksamen i databasen
def eksamen_endre(emnekode_eksamenendre, til_dato_aar_eksamenendre, til_dato_m_eksamenendre,
                                             til_dato_d_eksamenendre, fra_dato_aar_eksamenendre,
                                             fra_dato_m_eksamenendre, fra_dato_d_eksamenendre,
                                             fra_rom_eksamenendre, til_rom_eksamenendre):
    # Lager cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    emnekode = emnekode_eksamenendre.get()
    rom_til = til_rom_eksamenendre.get()
    rom_fra = fra_rom_eksamenendre.get()
    til_dato_ar = til_dato_aar_eksamenendre.get()
    til_dato_m = til_dato_m_eksamenendre.get()
    til_dato_d = til_dato_d_eksamenendre.get()
    fra_dato_ar = fra_dato_aar_eksamenendre.get()
    fra_dato_m = fra_dato_m_eksamenendre.get()
    fra_dato_d = fra_dato_d_eksamenendre.get()

    dato_til = til_dato_ar + til_dato_m + til_dato_d
    dato_fra = fra_dato_ar + fra_dato_m + fra_dato_d

    # Setter opp database strukturen for tabellen
    m_update = ('UPDATE Eksamen '
                'SET Emnekode = %s, Dato = %s, Romnr = %s '
                'WHERE Emnekode = %s AND Dato = %s AND Romnr = %s')

    # Lager variabel for input til MySQL
    d_update = (emnekode, dato_til, rom_til, emnekode, dato_fra, rom_fra)

    # Utfører handlingen i databasen
    marker.execute(m_update, d_update)
    mydb.commit()

    # Lukker cursor
    marker.close()


# MySQL-kode som lager tabellen 'oppmeldte' i databasen Eksamen og legger til oppmeldte kandidater i tabellen
def oppmelding_eksamen(emnekode_eksamenoppmelding, dato_aar_eksamenoppmelding, dato_m_eksamenoppmelding, dato_d_eksamenoppmelding,
                                                  studentnr_eksamenoppmelding):
    # Oppretter cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    emnekode = emnekode_eksamenoppmelding.get()
    dato_aar = dato_aar_eksamenoppmelding.get()
    dato_m = dato_m_eksamenoppmelding.get()
    dato_d = dato_d_eksamenoppmelding.get()
    studentnr = studentnr_eksamenoppmelding.get()

    dato = dato_aar + dato_m + dato_d

    # Utfører handlingen i databasen
    marker.execute(
        'CREATE TABLE IF NOT EXISTS `Oppmeldte` '
        '( '
        ' `Studentnr` CHAR(6) NOT NULL, '
        '`Dato` DATE NOT NULL, '
        '`Emnekode` CHAR(8) NOT NULL, '
        'PRIMARY KEY (`Studentnr`, `Emnekode`, `Dato`), '
        'FOREIGN KEY (`Studentnr`) REFERENCES Student(`Studentnr`), '
        'FOREIGN KEY (`Emnekode`, `Dato`) REFERENCES Eksamen(`Emnekode`, `Dato`) '
        ') DEFAULT CHARSET=utf8;'
    )

    # Setter opp database strukturen for tabellen
    m_eks = (
        'INSERT INTO Oppmeldte (Emnekode, Dato, Studentnr) '
        'SELECT * FROM (SELECT %s, %s, %s) AS tmp '
        'WHERE EXISTS ( '
        'SELECT Dato, Emnekode, Studentnr '
        'FROM Eksamen, Student '
        'WHERE Dato = %s '
        'AND Emnekode = %s '
        'AND Studentnr = %s)'
    )

    # Lager variabel for input til MySQL
    d_eks = (emnekode, dato, studentnr, dato, emnekode, studentnr)

    # Utfører handlingen i databasen
    marker.execute(m_eks, d_eks)
    mydb.commit()

    # Avslutter cursor
    marker.close()


# MySQL-kode for diverse utskrifter fra tabellen 'oppmeldte'
def utskrift_opp(tree_opp, emnekode_eksamenoppmelding, dato_aar_eksamenoppmelding, dato_m_eksamenoppmelding, dato_d_eksamenoppmelding,
                                                  studentnr_eksamenoppmelding):
    # Binder Treeviewet
    tree_opp.bind()

    # Sletter innholdet i Treeviewet
    for i in tree_opp.get_children():
        tree_opp.delete(str(i))

    # Oppretter cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    emnekode_oppmelding = emnekode_eksamenoppmelding.get()
    dato_aar = dato_aar_eksamenoppmelding.get()
    dato_m = dato_m_eksamenoppmelding.get()
    dato_d = dato_d_eksamenoppmelding.get()
    studentnr_oppmelding = studentnr_eksamenoppmelding.get()

    dato_oppmelding = dato_aar + dato_m + dato_d

    if emnekode_oppmelding == '' and dato_oppmelding == '' and studentnr_oppmelding == '':

        # Utfører handlingen i databasen
        marker.execute(
            'SELECT * '
            'FROM Oppmeldte ')

        for row in marker:
            tree_opp.insert('', 'end', values=(row[0], row[1], row[2]))

        marker.close()

    else:
        if emnekode_oppmelding != '' and dato_oppmelding != '' and studentnr_oppmelding == '':
            # Setter opp database strukturen for tabellen
            m_stud_emne = (
                'SELECT * '
                'FROM Oppmeldte '
                'WHERE Emnekode = %s '
                'AND Dato = %s')

            # Lager variabel for input til MySQL
            d_stud_emne = (emnekode_oppmelding, dato_oppmelding)

            # Utfører handlingen i databasen
            marker.execute(m_stud_emne, d_stud_emne)

            # Henter informasjon fra databsen inn i Treeviewet
            for row in marker:
                tree_opp.insert('', 'end', values=(row[0], row[1], row[2]))

            # Avslutter cursor
            marker.close()

        else:
            if emnekode_oppmelding == '' and dato_oppmelding == '' and studentnr_oppmelding != '':
                # Setter opp database strukturen for tabellen
                m_stud_emne = (
                    'SELECT * '
                    'FROM Oppmeldte '
                    'WHERE Studentnr =%s'
                )

                # Lager variabel for input til MySQL
                d_stud_emne = studentnr_oppmelding

                # Utfører handlingen i databasen
                marker.execute(m_stud_emne, d_stud_emne)

                # Henter informasjon fra databsen inn i Treeviewet
                for row in marker:
                    tree_opp.insert('', 'end', values=(row[0], row[1], row[2]))

                # Avslutter cursor
                marker.close()

            else:
                if emnekode_oppmelding != '' and dato_oppmelding != '' and studentnr_oppmelding != '':
                    # Setter opp database strukturen for tabellen
                    m_stud_emne = (
                        'SELECT * '
                        'FROM Oppmeldte '
                        'WHERE Emnekode = %s '
                        'AND Dato = %s '
                        'AND Studentnr = %s')

                    # Lager variabel for input til MySQL
                    d_stud_emne = (emnekode_oppmelding, dato_oppmelding, studentnr_oppmelding)

                    # Utfører handlingen i databasen
                    marker.execute(m_stud_emne, d_stud_emne)

                    # Henter informasjon fra databsen inn i Treeviewet
                    for row in marker:
                        tree_opp.insert('', 'end', values=(row[0], row[1], row[2]))

                    # Avslutter cursor
                    marker.close()


# GUI for administrasjon av eksamner
def adm_eksamen_gui():
    adm_eks = Toplevel()
    adm_eks.title('Administrasjon av Eksamner')

    ttk.Label(adm_eks, text='Administrering av Eksamen', font=('Calibri', '16')) \
        .grid(column=0, columnspan=1, row=0, pady=15, padx=15, sticky='WE')

    # Oppretter en Notebook-widget
    n = ttk.Notebook(adm_eks)
    n.grid(row=1, column=0, columnspan=4, rowspan=6, sticky='NESW')
    f1 = ttk.Frame(n)  # første side
    f2 = ttk.Frame(n)  # andre side
    f3 = ttk.Frame(n)

    n.add(f1, text='Ajourhold fremtidige eksamner')
    n.add(f2, text='Endre oppsatt eksamen')
    n.add(f3, text='Oppmelding til eksamen')

    # Side 1 i notebook er oppsetting av eksamner
    # Lager labels og entries
    ttk.Label(f1, text='Emnekode:').grid(row=0, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=emnekode_eksamenadd, width=15).grid(row=0, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f1, text='Dato:').grid(row=1, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=dato_aar_eksamenadd, width=5).grid(column=1, row=1, padx=5, pady=5, sticky=(N, W))
    ttk.Entry(f1, textvariable=dato_m_eksamenadd, width=3).grid(column=1, row=1, padx=47, pady=5, sticky=(N, W))
    ttk.Entry(f1, textvariable=dato_d_eksamenadd, width=3).grid(column=1, row=1, padx=76, pady=5, sticky=(N, W))

    ttk.Label(f1, text='RomNr:').grid(row=2, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(f1, textvariable=romnr_eksamenadd, width=15).grid(row=2, column=1, padx=5, pady=5, sticky=W)

    ttk.Button(f1, text='Legg til eksamen', command=add_eksamen).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(f1, justify='left', text='Oversikt over alle \n oppsatte eksamner') \
        .grid(row=4, column=2, padx=25, pady=10, sticky=(N, W))
    ttk.Button(f1, text='Klikk her!', command=lambda: utskrift_eksamen(tree)) \
        .grid(row=4, column=2, padx=25, pady=50, sticky=(N, W))

    # Lager treeviewet
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

    # Lager en infoboks til brukeren
    p = ttk.Panedwindow(f1, orient=VERTICAL)
    p.grid(row=1, column=2, columnspan=1, rowspan=2, padx=10, sticky=W)
    l = ttk.Labelframe(p, text='Info', width=50, height=100)
    p.add(l)
    l2 = Label(l, justify='left', text="Fyll inn alle feltene med \n"
                                       "riktig informasjon om \n "
                                       "eksamen, og klikk \n"
                                       "'Legg til eksamen'")
    l2.grid(row=0, column=0)

    # Side 2 i notebook er endring av oppsatt eksamen
    p1 = ttk.Panedwindow(f2, orient=VERTICAL, width=340, height=55)
    p1.grid(row=0, column=0, padx=10, pady=5, sticky=E, rowspan=4, columnspan=3)
    l1 = ttk.Labelframe(p1, text='Info', width=340, height=55)
    p1.add(l1)
    label = Label(l1, justify='left', text="Skriv inn emnekode og dato, deretter trykk på knappen \n"
                                           "'endre eksamen'. Dato skrives i format YYYY/MM/DD ")
    label.grid(row=0, column=0)

    # Lager labels og entries
    ttk.Label(f2, text='Emnekode:').grid(row=4, column=0, padx=5, pady=5, sticky=W)
    emnekode_eksamenendre = StringVar()
    ttk.Entry(f2, textvariable=emnekode_eksamenendre, width=15).grid(row=4, column=0, padx=5, pady=5, sticky=E)

    ttk.Label(f2, text='Nåværende dato:').grid(row=5, column=0, padx=5, pady=5, sticky=W)
    til_dato_aar_eksamenendre = StringVar()
    ttk.Entry(f2, textvariable=til_dato_aar_eksamenendre, width=5).grid(column=0, row=5, padx=80, pady=5, sticky=(N, E))
    til_dato_m_eksamenendre = StringVar()
    ttk.Entry(f2, textvariable=til_dato_m_eksamenendre, width=3).grid(column=0, row=5, padx=45, pady=5, sticky=(N, E))
    til_dato_d_eksamenendre = StringVar()
    ttk.Entry(f2, textvariable=til_dato_d_eksamenendre, width=3).grid(column=0, row=5, padx=10, pady=5, sticky=(N, E))

    ttk.Label(f2, text='Nåværende romnr:').grid(row=5, column=1, padx=5, pady=5, sticky=E)
    fra_rom_eksamenendre = StringVar()
    ttk.Entry(f2, textvariable=fra_rom_eksamenendre, width=7).grid(row=5, column=2, padx=5, pady=5, sticky=W)

    ttk.Label(f2, text='Ønsket dato:').grid(row=6, column=0, padx=5, pady=5, sticky=W)
    fra_dato_aar_eksamenendre = StringVar()
    ttk.Entry(f2, textvariable=fra_dato_aar_eksamenendre, width=5).grid(column=0, row=6, padx=80, pady=5, sticky=(N, E))
    fra_dato_m_eksamenendre = StringVar()
    ttk.Entry(f2, textvariable=fra_dato_m_eksamenendre, width=3).grid(column=0, row=6, padx=45, pady=5, sticky=(N, E))
    fra_dato_d_eksamenendre = StringVar()
    ttk.Entry(f2, textvariable=fra_dato_d_eksamenendre, width=3).grid(column=0, row=6, padx=10, pady=5, sticky=(N, E))

    ttk.Label(f2, text='Ønsket romnr:').grid(row=6, column=1, padx=5, pady=5, sticky=E)
    til_rom_eksamenendre = StringVar()
    ttk.Entry(f2, textvariable=til_rom_eksamenendre, width=7).grid(row=6, column=2, padx=5, pady=5, sticky=W)

    # Lager knapp som sender til databsen
    ttk.Button(f2, text='Endre eksamen',
               command=lambda: eksamen_endre(emnekode_eksamenendre, til_dato_aar_eksamenendre, til_dato_m_eksamenendre,
                                             til_dato_d_eksamenendre, fra_dato_aar_eksamenendre,
                                             fra_dato_m_eksamenendre, fra_dato_d_eksamenendre,
                                             fra_rom_eksamenendre, til_rom_eksamenendre))\
        .grid(row=7, column=2, padx=5, pady=5, sticky=W)

    # Side 3 i notebook er oppmelding til eksamen
    ttk.Label(f3, text='Emnekode:').grid(row=1, column=0, rowspan=3, padx=5, pady=5, sticky=N)
    emnekode_eksamenoppmelding = StringVar()
    ttk.Entry(f3, textvariable=emnekode_eksamenoppmelding, width=15)\
        .grid(row=1, column=1, rowspan=3, padx=5, pady=5, sticky=(N, W))

    ttk.Label(f3, text='Dato:').grid(row=1, column=0, rowspan=3, padx=5, pady=35, sticky=(N, W))
    dato_aar_eksamenoppmelding = StringVar()
    ttk.Entry(f3, textvariable=dato_aar_eksamenoppmelding, width=5).grid(column=1, row=1, rowspan=3, padx=5, pady=35,
                                                                         sticky=(N, W))
    dato_m_eksamenoppmelding = StringVar()
    ttk.Entry(f3, textvariable=dato_m_eksamenoppmelding, width=3).grid(column=1, row=1, rowspan=3, padx=47, pady=35,
                                                                       sticky=(N, W))
    dato_d_eksamenoppmelding = StringVar()
    ttk.Entry(f3, textvariable=dato_d_eksamenoppmelding, width=3).grid(column=1, row=1, rowspan=3, padx=76, pady=35,
                                                                       sticky=(N, W))

    ttk.Label(f3, text='Studentnr:').grid(row=1, column=0, rowspan=3, padx=5, pady=65, sticky=N)
    studentnr_eksamenoppmelding = StringVar()
    ttk.Entry(f3, textvariable=studentnr_eksamenoppmelding, width=15)\
        .grid(row=1, column=1, rowspan=3, padx=5, pady=65, sticky=(N, W))

    ttk.Button(f3, text='Meld opp til eksamen',
               command=lambda: oppmelding_eksamen(emnekode_eksamenoppmelding, dato_aar_eksamenoppmelding, dato_m_eksamenoppmelding, dato_d_eksamenoppmelding,
                                                  studentnr_eksamenoppmelding)) \
        .grid(row=1, column=1, rowspan=3, padx=5, pady=95, sticky=(N, W))

    ttk.Label(f3, justify='left', text='Oversikt over alle \n oppmeldte elever')\
        .grid(row=1, column=3, padx=25, pady=10, sticky=(N, W))

    ttk.Button(f3, text='Klikk her!',
               command=lambda: utskrift_opp(tree_opp, emnekode_eksamenoppmelding, dato_aar_eksamenoppmelding, dato_m_eksamenoppmelding, dato_d_eksamenoppmelding,
                                                  studentnr_eksamenoppmelding))\
        .grid(row=1, column=3, padx=40, pady=50, sticky=(N, W))

    # Oppretter Panedwindow for Notebook side 1 og legger inn veiledende tekst
    p1 = ttk.Panedwindow(f3, orient=VERTICAL)
    p1.grid(row=0, column=0, columnspan=5, padx=20, pady=10)
    l1 = ttk.Labelframe(p1, text='Info', width=150, height=100)
    p1.add(l1)
    label = Label(l1, justify='left', text="For å melde opp student til eksamen, \n"
                                           "fyll inn alle feltene og trykk 'Meld opp til eksamen'\n"
                                           "* For å sjekke en spesifikk eksamen, fyll inn DATO og EMNEKODE og trykk "
                                           "'klikk her'\n "
                                           "* For å sjekke en spesifikk student, fyll inn STUDENTNR og trykk 'klikk "
                                           "her'\n "
                                           "* For å sjekke en spesifikk student opp mot en spesifikk eksamen, "
                                           "fyll inn ALLE felter og trykk 'klikk her'\n "
                                           "* For å sjekke alle studenter som er oppmeldt til eksamen, la alle "
                                           "feltene stå blankt og trykk 'klikk her'")
    label.grid(row=0, column=0)

    tree_opp = ttk.Treeview(f3)
    tree_opp["columns"] = ("1", "2", "3")
    tree_opp.column("#0", anchor="w", width=0)
    tree_opp.column("#1", width=70)
    tree_opp.column("#2", width=75)
    tree_opp.column("#3", width=85)
    tree_opp.heading("#1", text="Studentnr")
    tree_opp.heading("#2", text="Dato")
    tree_opp.heading("#3", text="Emnekode")

    ysb = ttk.Scrollbar(f3, orient=VERTICAL, command=tree_opp.yview)

    tree['yscroll'] = ysb.set

    # add tree and scrollbars to frame
    tree_opp.grid(row=1, column=2, rowspan=4, pady=7, sticky=NSEW)
    ysb.grid(row=1, column=3, rowspan=4, pady=7, sticky=(N, S, W))

    # Avslutt-knapp for toplevel
    ttk.Button(adm_eks, text='Lukk vinduet', command=adm_eks.destroy).grid(row=7, column=3, padx=5, pady=15, sticky=E)


# MySQL-kode for utskrift av alle rom i databasen
def oversikt_rom(tree):
    # Binder viewet
    tree.bind()

    # Sletter innholdet i Treeviewet
    for i in tree.get_children():
        tree.delete(str(i))

    # Oppretter cursor
    marker = mydb.cursor()

    # Utfører handlingen i databsen
    marker.execute(
        'SELECT * '
        'FROM Rom')

    # Henter informasjon fra databsen inn i Treeviewet
    for row in marker:
        tree.insert('', 'end', values=(row[0], row[1]))

    # Avslutter cursor
    marker.close()


# MySQL-kode som legger til rom i databasen
def add_rom():
    # Oppretter cursor
    marker = mydb.cursor()

    # Henter alle strengene og lager variabler
    romnr = romnr_add.get()
    antallplasser = antallplasser_add.get()

    # Setter opp database strukturen for tabellen
    m_rom = ('INSERT INTO Rom'
             '(Romnr, Antallplasser)'
             'VALUES(%s, %s)')

    # Lager variabel for input til MySQL
    d_rom = (romnr, antallplasser)

    # Utfører handlingen i databasen
    marker.execute(m_rom, d_rom)
    mydb.commit()

    # Avslutter cursor
    marker.close()


# GUI for administrasjon av rom
def adm_rom_gui():
    # Oppretter en toplevel-frame
    adm_rom = Toplevel()
    adm_rom.title('Administrasjon av Rom')

    # Lager labels og entries
    ttk.Label(adm_rom, text="Administrering av Rom", font=('Calibri', '16')).grid(column=0, columnspan=2, row=0,
                                                                                  pady=15, padx=15, sticky='WE')

    ttk.Separator(adm_rom).grid(row=2, column=0, columnspan=6, pady=5, sticky=(W, E))

    ttk.Label(adm_rom, text='RomNr:').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_rom, textvariable=romnr_add, width=15).grid(row=3, column=1, padx=5, pady=5, sticky=W)

    ttk.Label(adm_rom, text='AntallPlasser:').grid(row=4, column=0, padx=5, pady=5, sticky=W)
    ttk.Entry(adm_rom, textvariable=antallplasser_add, width=15).grid(row=4, column=1, padx=5, pady=5, sticky=W)

    # Knapp for å legge til rom
    ttk.Button(adm_rom, text='Legg til rom', command=add_rom).grid(row=5, column=1, padx=10, pady=7, sticky=W)

    # Knapp for å få oversikt over rommene
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
    ttk.Button(adm_rom, text='Lukk vinduet', command=adm_rom.destroy).grid(row=9, column=3, padx=5, pady=15, sticky=E)


# MySQL-kode som legger til emne i databasen
def add_emne():
    # Oppretter en cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    emnekode = emnekode_add.get()
    emnenavn = emnenavn_add.get()
    studiepoeng = studiepoeng_add.get()

    # Setter opp database strukturen for tabellen
    m_stud = ('INSERT INTO Emne'
              '(Emnekode, Emnenavn, Studiepoeng)'
              'VALUES(%s, %s, %s)')

    # Legger strengene inn i databasen
    d_stud = (emnekode, emnenavn, studiepoeng)

    # Utfører handlingen i databasen
    marker.execute(m_stud, d_stud)
    mydb.commit()

    # Lukker cursor
    marker.close()


# MySQL-kode for utskrift av alle emner i databasen
def oversikt_emne(tree_emne):
    # Binder treeviewet
    tree_emne.bind()

    # Sletter innholdet i treeviewet
    for i in tree_emne.get_children():
        tree_emne.delete(str(i))

    # Oppretter en cursor
    marker = mydb.cursor()

    # Setter opp database strukturen for tabellen
    m_emne = ('SELECT * '
              'FROM Emne '
              'ORDER BY Emnekode ASC')

    # Utfører handlingen i databasen
    marker.execute(m_emne)

    # Henter informasjon fra databsen inn i Treeviewet
    for row in marker:
        tree_emne.insert('', 'end', values=(row[0], row[1], row[2]))

    # Lukker cursor
    marker.close()


# GUI for administrering av emne
def adm_emne_gui():
    # Oppretter en toplevel-frame
    adm_emne = Toplevel()
    adm_emne.title('Administrasjon av Emner')

    ttk.Label(adm_emne, text="Administrering av Emne", font=('Calibri', '16')).grid(column=0, columnspan=3, row=0,
                                                                                    pady=15, padx=15,
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
    ttk.Entry(adm_emne, textvariable=emnekode_add, width=15).grid(row=3, column=1, padx=5, pady=7, sticky=W)

    ttk.Label(adm_emne, text='Emnenavn:').grid(row=4, column=0, padx=5, pady=7, sticky=W)
    ttk.Entry(adm_emne, textvariable=emnenavn_add, width=15).grid(row=4, column=1, padx=5, pady=7, sticky=W)

    ttk.Label(adm_emne, text='Studiepoeng:').grid(row=5, column=0, padx=5, pady=7, sticky=W)
    ttk.Entry(adm_emne, textvariable=studiepoeng_add, width=8).grid(row=5, column=1, padx=5, pady=7, sticky=W)

    # Lager button som legger inn strengene i databasen
    ttk.Button(adm_emne, text='Legg til emne', command=add_emne).grid(row=7, column=1, columnspan=2, padx=5, pady=7,
                                                                      sticky=W)
    # Lager Treeview-widget
    tree_emne = ttk.Treeview(adm_emne)

    tree_emne["columns"] = ("1", "2", "3")
    tree_emne.column("#0", anchor="w", width=0)
    tree_emne.column("#1", width=65)
    tree_emne.column("#2", width=175)
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


# MySQL-kode som legger til student i databasen
def add_stud():
    # Oppretter en cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    studentnr = studentnr_studadd.get()
    fornavn = fornavn_studadd.get()
    etternavn = etternavn_studadd.get()
    epost = epost_studadd.get()
    telefon = telefon_studadd.get()

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


# MySQL-kode som endrer student i databasen
def update_stud():
    # Oppretter en cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    studentnr = studentnr_studadd.get()
    fornavn = fornavn_studadd.get()
    etternavn = etternavn_studadd.get()
    epost = epost_studadd.get()
    telefon = telefon_studadd.get()

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


# MySQL-kode som sletter student i databasen
def delete_stud():
    # Oppretter en cursor
    marker = mydb.cursor()

    # Henter strengene og lagrer de som variabler
    studentnr = studentnr_stud_del.get()

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
    adm_stud.title('Administrasjon av Studenter')

    ttk.Label(adm_stud, text="Administrering av Studenter", font=('Calibri', '16')).grid(column=0, row=0, pady=15,
                                                                                         padx=15, sticky=(W, E))

    # Oppretter en Notebook-widget
    n = ttk.Notebook(adm_stud)
    n.grid(row=1, column=0, columnspan=4, rowspan=6, sticky='NESW')
    f1 = ttk.Frame(n)  # første side
    f2 = ttk.Frame(n)  # andre side

    n.add(f1, text='Legg til/oppdater student')
    n.add(f2, text='Slett eksisterende student')

    # Side 1 notebook
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
    ttk.Entry(f1, textvariable=studentnr_studadd, width=6).grid(row=3, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f1, text='Fornavn:').grid(row=4, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f1, textvariable=fornavn_studadd).grid(row=4, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f1, text='Etternavn:').grid(row=5, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f1, textvariable=etternavn_studadd).grid(row=5, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f1, text='Epost:').grid(row=6, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f1, textvariable=epost_studadd).grid(row=6, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f1, text='Telefonnr:').grid(row=7, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f1, textvariable=telefon_studadd, width=8).grid(row=7, column=2, padx=5, pady=7, sticky=W)

    ttk.Separator(f1).grid(row=8, column=1, columnspan=6, sticky=(W, E))

    # Oppretter button som legger inn strengene i databasen
    ttk.Button(f1, text='Legg til student', command=add_stud).grid(row=9, column=1, columnspan=2, pady=15, padx=5,
                                                                   sticky=W)

    # Oppretter button som legger inn de oppdaterte strengene i databasen
    ttk.Button(f1, text='Oppdater student', command=update_stud).grid(row=9, column=1, columnspan=2, pady=15, padx=5,
                                                                      sticky=E)

    # Side 2 notebook er slett student
    # Oppretter Panedwindow for Notebook side 2 og legger inn veiledende tekst
    p2 = ttk.Panedwindow(f2, orient=VERTICAL, width=280, height=70)
    p2.grid(row=3, column=3, padx=10, pady=5, sticky=E, rowspan=4, columnspan=3)
    l3 = ttk.Labelframe(p2, text='Info', width=280, height=70)
    p2.add(l3)
    label3 = Label(l3, justify='left', text="NB! Studenter med eksamensresultater\n"
                                            "går ikke å slette! \n"
                                            "Fyll inn studentnr og trykk 'Slett student'.")
    label3.grid(row=0, column=0)

    # Lables og Entries for Notebook side 2
    ttk.Label(f2, text='Studentnr:').grid(row=3, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f2, textvariable=studentnr_stud_del, width=6).grid(row=3, column=2, padx=5, pady=7, sticky=W)

    ttk.Separator(f2).grid(row=8, column=1, columnspan=7, sticky=(W, E))

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
root.title("Eksamens-applikasjon")

# innholdet i vinduet
mainframe = ttk.Frame(root, padding="6 6 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Tekst som Label, knapper som Button, med separators og plassering i grid
ttk.Label(mainframe, text="Administrering av eksamen ved HSN", font=('Calibri', '24')) \
    .grid(column=0, row=0, columnspan=3, pady=50)
ttk.Separator(mainframe, orient=HORIZONTAL) \
    .grid(column=0, row=1, columnspan=3, sticky=(W, E))

ttk.Label(mainframe, text="Administrer Studenter", font=1) \
    .grid(column=0, row=2, sticky=(E, W))
ttk.Button(mainframe, text="Studenter", width=30, command=adm_stud_gui) \
    .grid(column=1, row=2, padx=20, sticky=(N, S))

ttk.Label(mainframe, text="Administrer Emner", font=1) \
    .grid(column=0, row=3, sticky=(E, W))
ttk.Button(mainframe, text="Emner", width=30, command=adm_emne_gui) \
    .grid(column=1, row=3, padx=20, sticky=(N, S))

ttk.Label(mainframe, text="Administrer Rom", font=1) \
    .grid(column=0, row=4, sticky=(E, W))
ttk.Button(mainframe, text="Rom", width=30, command=adm_rom_gui) \
    .grid(column=1, row=4, padx=20, sticky=(N, S))

ttk.Label(mainframe, text="Administrer Eksamener", font=1) \
    .grid(column=0, row=5, sticky=(E, W))
ttk.Button(mainframe, text="Eksamener", width=30, command=adm_eksamen_gui) \
    .grid(column=1, row=5, padx=20, sticky=(N, S))

ttk.Label(mainframe, text="Administrer Karakterer", font=1) \
    .grid(column=0, row=6, sticky=(E, W))
ttk.Button(mainframe, text="Karakterer", width=30, command=adm_kar_gui) \
    .grid(column=1, row=6, padx=20, sticky=(N, S))

ttk.Separator(mainframe, orient=HORIZONTAL) \
    .grid(column=0, row=7, columnspan=3, pady=50, sticky=(W, E))

ttk.Label(mainframe, text="Utskrifter av oversikter", font=1) \
    .grid(column=0, row=8, sticky=(E, W))
ttk.Button(mainframe, text="Oversikter", width=30, command=utskrifter) \
    .grid(column=1, row=8, padx=20, sticky=(N, S))

ttk.Separator(mainframe, orient=HORIZONTAL) \
    .grid(column=0, row=9, columnspan=3, pady=20, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy, width=25) \
    .grid(column=2, row=10, padx=20, sticky=(N, S, E))

# Text-wigdets for informasjon av funksjoner i programmet
tekst1 = Text(mainframe, width=48, height=3, wrap="word", bg='lightgrey')
tekst1.grid(column=2, row=2)
tekst1.insert('1.0', '* Legge til studenter \n'
                     '* Endre studenter \n'
                     '* Slette studenter')

tekst2 = Text(mainframe, width=48, height=3, wrap="word", bg='lightgrey')
tekst2.grid(column=2, row=3)
tekst2.insert('1.0', '* Legge til emner \n'
                     '* Få utskrift av alle emner')

tekst3 = Text(mainframe, width=48, height=3, wrap="word", bg='lightgrey')
tekst3.grid(column=2, row=4)
tekst3.insert('1.0', '* Legge til rom \n'
                     '* Få utskrift av alle rom')

tekst4 = Text(mainframe, width=48, height=4, wrap="word", bg='lightgrey')
tekst4.grid(column=2, row=5)
tekst4.insert('1.0', '* Legge til eksamner \n'
                     '* Endre eksamner \n'
                     '* Utskrift av oppsatte eksamner og kandidater \n'
                     '* Melde opp kandidater til eksamen')

tekst5 = Text(mainframe, width=48, height=3, wrap="word", bg='lightgrey')
tekst5.grid(column=2, row=6)
tekst5.insert('1.0', '* Endre karakter på student \n'
                     '* Registrere karakterer for en avholdt eksamen')

tekst6 = Text(mainframe, width=48, height=3, wrap="word", bg='lightgrey')
tekst6.grid(column=2, row=8)
tekst6.insert('1.0', '* Utskrifter av informasjon om studenter, emner\n'
                     '  eksamner, karakterer og vitnemål')

for child in mainframe.winfo_children():
    child.grid_configure(pady=5)

# Strenger for student add/endre
studentnr_studadd = StringVar()
fornavn_studadd = StringVar()
etternavn_studadd = StringVar()
epost_studadd = StringVar()
telefon_studadd = StringVar()

# Strenger for student slett
studentnr_stud_del = StringVar()

# Strenger for emne
emnekode_add = StringVar()
emnenavn_add = StringVar()
studiepoeng_add = StringVar()

# Strenger for rom
romnr_add = StringVar()
antallplasser_add = StringVar()

# Strenger for oppsetting av eksamen
emnekode_eksamenadd = StringVar()
dato_aar_eksamenadd = StringVar()
dato_m_eksamenadd = StringVar()
dato_d_eksamenadd = StringVar()
romnr_eksamenadd = StringVar()

#Strenger for endring av eksamener
emnekode_eksamenendre = StringVar()
til_rom_eksamenendre = StringVar()
fra_rom_eksamenendre = StringVar()
til_dato_aar_eksamenendre = StringVar()
til_dato_m_eksamenendre = StringVar()
til_dato_d_eksamenendre = StringVar()
fra_dato_aar_eksamenendre = StringVar()
fra_dato_m_eksamenendre = StringVar()
fra_dato_d_eksamenendre = StringVar()

# Strenger for karakter endre
emnekode_karakterendre = StringVar()
studentnr_karakterendre = StringVar()
karakter_karakterendre = StringVar()

# Strenger for karakter add
emnekode_karakteradd = StringVar()
studentnr_karakteradd = StringVar()
karakter_karakteradd = StringVar()
dato_aar_karakteradd = StringVar()
dato_m_karakteradd = StringVar()
dato_d_karakteradd = StringVar()


# Strenger for utskrift side 1
emnekode_utskriftside1 = StringVar()

# Strenger for utskrift side 2
studentnr_utskriftside2 = StringVar()

# Strenger for utskrift side 5
emnekode_utskriftside5 = StringVar()

# Strenger for utskrift side 6
studentnr_utskriftside6 = StringVar()

# Starter programmet
root.mainloop()
