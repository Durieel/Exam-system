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

    # Lager button som gjør at brukeren kan gå tilbake til hovedmeny
    ttk.Button(adm_emne, text='Gå tilbake', command=adm_emne.destroy).grid(row=9, column=4, padx=5, pady=5, sticky=E)
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
    f1 = ttk.Frame(n)  # første side
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
    label2 = Label(l2, text="Fyll ut studentnr på studenten som       \n"
                            "skal endres, og fyll ut resterende          \n"
                            "felter med oppdatert informasjon.         \n"
                            "Og klikk på 'Oppdater student'              ")
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
                            "går ikke å slette!                                    \n"
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

    p1 = ttk.Panedwindow(ramme, orient=VERTICAL)
    p1.grid(row=2, column=0, rowspan=2, padx=5, pady=5)
    l1 = ttk.Labelframe(p1, text='Info', width=150, height=100)
    p1.add(l1)
    label = Label(l1, text="Ved eksamen i en periode velg fra og til dato.      \n"
                           "  Hvis du vil ha en spesifikk dag bruk kun fra dato     \n")
    label.grid(row=0, column=0)

    dag = StringVar()
    combo1 = ttk.Combobox(ramme, textvariable=dag, width=4)
    combo1.grid(column=2, row=2, sticky=(W, E))
    ttk.Label(ramme, text="Fra") .grid(column=1, row=2, sticky=W, padx=5)
    combo1['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                     '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')

    #combo1.bind('<<ComboboxSelected>>', dag1)

    maaned = StringVar()
    combo2 = ttk.Combobox(ramme, textvariable=maaned, width=4, state="readonly")
    combo2.grid(column=3, row=2, sticky=W)
    combo2['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
    maaned1 = maaned.get()

    aar = StringVar()
    combo3 = ttk.Combobox(ramme, textvariable=aar, width=6, state="readonly")
    combo3.grid(column=4, row=2, sticky=W,)
    combo3['values'] = ('2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                      '2017')
    aar1 = aar.get()

    dag2 = StringVar()
    combo4 = ttk.Combobox(ramme, textvariable=dag2, width=4, state="readonly")
    combo4.grid(column=2, row=3, sticky=(W, E))
    ttk.Label(ramme, text="Til").grid(column=1, row=3, sticky=(W, E), padx=5)
    combo4['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                     '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    # dag2.bind('<<ComboboxSelected>>', utskrift_eks)


    maaned2 = StringVar()
    maaned2 = ttk.Combobox(ramme, textvariable=maaned2, width=4, state="readonly")
    maaned2.grid(column=3, row=3, sticky=(W, E))
    maaned2['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

    aar2 = StringVar()
    aar2 = ttk.Combobox(ramme, textvariable=aar2, width=6, state="readonly")
    aar2.grid(column=4, row=3, sticky=W)
    aar2['values'] = ('2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'
                      '2017')

    tekst1 = Text(ramme, width=40, height=10, wrap="word")
    tekst1.grid(column=0, row=4, sticky=(W, E), columnspan=5)
    tekst1.insert('1.0', 'Her kommer utskriftene')

    ttk.Button(ramme, text='Utfør', command=lambda: info(dag1, maaned1, aar1)).grid(column=4, row=5, sticky=E)

    for child in ramme.winfo_children():
        child.grid_configure(pady=2, padx=5)
    return dag1, maaned1, aar1

def info(dag1, maaned1, aar1):
    dag1 = dag.get()
    print(dag1)
    print(maaned1)
    print(aar1)


















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
tekst.insert('1.0', 'Fra denne siden kan du redigere alle aspekter av eksamensinformasjonen. På administrer studenter'
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
dag1 = StringVar()
dag = StringVar()
maaned1 = StringVar()
aar1 = StringVar()
root.mainloop()
