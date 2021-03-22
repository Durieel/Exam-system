from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def add_stud():
    #Oppretter en cursor
    marker = mydb.cursor()

    #Henter strengene og lagrer de som variabler
    studentnr = studentnr_1.get()
    fornavn = fornavn_1.get()
    etternavn = etternavn_1.get()
    epost = epost_1.get()
    telefon = telefon_1.get()

    #Setter opp database strukturen for tabellen
    m_stud = ('INSERT INTO Student'
             '(Studentnr, Fornavn, Etternavn, Epost, Telefon)'
             'VALUES(%s, %s, %s, %s, %s)')
    d_stud = (studentnr, fornavn, etternavn, epost, telefon)

    #Legger strengene inn i databasen
    marker.execute(m_stud, d_stud)
    mydb.commit()

    #Lukker cursor
    marker.close()


def update_stud():
    #Oppretter en cursor
    marker = mydb.cursor()

    #Henter strengene og lagrer de som variabler
    studentnr = studentnr_1.get()
    fornavn = fornavn_1.get()
    etternavn = etternavn_1.get()
    epost = epost_1.get()
    telefon = telefon_1.get()

    #Setter opp database strukturen for tabellen
    m_stud = ('UPDATE Student '
              'SET Fornavn = %s, Etternavn = %s, Epost = %s, Telefon = %s '
              'WHERE Studentnr = %s')

    d_stud = (fornavn, etternavn, epost, telefon, studentnr)

    #Legger strengene inn i databasen
    marker.execute(m_stud, d_stud)
    mydb.commit()

    #Lukker cursor
    marker.close()



# GUI for administrering av student
def adm_stud_gui():
    #Oppretter en toplevel-frame
    adm_stud = Toplevel()
    adm_stud.title('Eksamensadministrasjonsapplikasjon')


    ttk.Label(adm_stud, text="Administrering av Studenter").grid(column=0, row=0, pady=15, padx=15, sticky='WE')

    #Oppretter en Notebook-widget
    n = ttk.Notebook(adm_stud)
    n.grid(row=1, column=0, columnspan=4, rowspan=10, sticky='NESW')
    f1 = ttk.Frame(n)  # første side
    f2 = ttk.Frame(n)  # andre side
    f3 = ttk.Frame(n)  # tredje side

    n.add(f1, text='Legg til ny student')
    n.add(f2, text='Rediger eksisterende student')
    n.add(f3, text='Slett eksisterende student')

    #Oppretter Panedwindow for Notebook side 1 og legger inn veiledende tekst
    p1 = ttk.Panedwindow(f1, orient=VERTICAL)
    p1.grid(row=3, column=3, columnspan=3, rowspan=3, padx=20, pady=10)
    l1 = ttk.Labelframe(p1, text='Info', width=125, height=100)
    p1.add(l1)
    label = Label(l1, text="Fyll inn alle feltene med riktig \n"
                       "informasjon om studenten, \n"
                       "og klikk 'Legg til student'!")
    label.grid(row=0, column=0)

    #Lables og Entries for Notebook side 1
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

    #Oppretter button som legger inn strengene i databasen
    ttk.Button(f1, text='Legg til studenten', command=add_stud).grid(row=9, column=1, columnspan=2, pady=15, padx=5, sticky=W)

    # Oppretter Panedwindow for Notebook side 2 og legger inn veiledende tekst
    p2 = ttk.Panedwindow(f2, orient=VERTICAL)
    p2.grid(row=3, column=3, columnspan=3, rowspan=3, padx=20, pady=10)
    l2 = ttk.Labelframe(p2, text='Info', width=125, height=100)
    p2.add(l2)
    label2 = Label(l2, text="Fyll inn studentnr på studenten, \n"
                            "og fyll inn endringene i de andre \n"
                            "feltene. \n"
                            "Deretter klikk 'Oppdater student")
    label2.grid(row=0, column=0)

    #Lables og Entries for Notebook side 2
    ttk.Label(f2, text='Studentnr:').grid(row=3, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f2, textvariable=studentnr_1, width=6).grid(row=3, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f2, text='Fornavn:').grid(row=4, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f2, textvariable=fornavn_1).grid(row=4, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f2, text='Etternavn:').grid(row=5, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f2, textvariable=etternavn_1).grid(row=5, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f2, text='Epost:').grid(row=6, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f2, textvariable=epost_1).grid(row=6, column=2, padx=5, pady=7, sticky=W)

    ttk.Label(f2, text='Telefonnr:').grid(row=7, column=1, padx=5, pady=7, sticky=W)
    ttk.Entry(f2, textvariable=telefon_1, width=8).grid(row=7, column=2, padx=5, pady=7, sticky=W)

    ttk.Separator(f2).grid(row=8, column=1, columnspan=6, sticky=(W, E))

    # Oppretter button som legger inn de oppdaterte strengene i databasen
    ttk.Button(f2, text='Oppdater student', command=update_stud).grid(row=9, column=1, columnspan=2, pady=15, padx=5,
                                                                     sticky=W)

    #Button som avslutter programmet
    ttk.Button(adm_stud, text='Lukk vinduet', command=adm_stud.destroy).grid(row=11, column=3, pady=15, padx=5, sticky=E)

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
ttk.Button(mainframe, text="Studenter", command=adm_stud_gui).grid(column=1, row=2, sticky=W)

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
ttk.Button(mainframe, text="Oversikter").grid(column=1, row=8, sticky=W)

ttk.Separator(mainframe, orient=HORIZONTAL).grid(column=0, row=9, columnspan=2, sticky=(W, E))
ttk.Button(mainframe, text="Avslutt", command=root.destroy).grid(column=1, row=10, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(pady=5)

studentnr_1 = StringVar()
fornavn_1 = StringVar()
etternavn_1 = StringVar()
epost_1 = StringVar()
telefon_1 = StringVar()


# Boolske verdier
feil = False


root.mainloop()
