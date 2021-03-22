# Vi har lest oss opp på tk-docs for å se hva tk-modulen har av widgets og forstå hvordan man bruker de.
# Resten har vi brukt fra boka eller forelesninger.

# Vi har lagd en slett-funksjon for utlaan-tabellen, fordi for å slette en bok eller et eksemplar på riktig måte,
# må man først slette elementet i den nederste child-tabellen, som er utlaan.


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


def add_book_database():
    feil = False
    try:
        marker = my_database.cursor()

        isbn = isbn_bok.get()
        tittel = tittel_bok.get()
        forfatter = forfatter_bok.get()
        forlag = forlag_bok.get()
        utgitt_aar = utgitt_aar_bok.get()
        antall_sider = antall_sider_bok.get()

        m_bok = ('INSERT INTO Bok'
                 '(ISBN, Tittel, Forfatter, Forlag, UtgittAar, AntallSider)'
                 'VALUES(%s, %s, %s, %s, %s, %s)')
        d_bok = (isbn, tittel, forfatter, forlag, utgitt_aar, antall_sider)

        marker.execute(m_bok, d_bok)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prøv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Boken er lagt til')

        else:
            feil = False


def change_book_database():
    feil = False
    try:
        marker = my_database.cursor()

        isbn = isbn_bok.get()
        tittel = tittel_bok.get()
        forfatter = forfatter_bok.get()
        forlag = forlag_bok.get()
        utgitt_aar = utgitt_aar_bok.get()
        antall_sider = antall_sider_bok.get()

        m_bok = ('DELETE FROM Bok '
                 'WHERE ISBN = %s')
        d_bok = isbn

        marker.execute(m_bok, d_bok)
        my_database.commit()

        d_bok = ('INSERT INTO Bok'
                 '(ISBN, Tittel, Forfatter, Forlag, UtgittAar, AntallSider)'
                 'VALUES(%s, %s, %s, %s, %s, %s)')
        e_bok = (isbn, tittel, forfatter, forlag, utgitt_aar, antall_sider)

        marker.execute(d_bok, e_bok)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prøv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Boken er endret')

        else:
            feil = False


def delete_book_database():
    feil = False
    try:
        marker = my_database.cursor()

        isbn = isbn_bok.get()

        m_bok = ('DELETE FROM Bok '
                 'WHERE ISBN = %s')
        d_bok = isbn

        marker.execute(m_bok, d_bok)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prøv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Boken er slettet')

        else:
            feil = False


def add_eksemplar_database():
    feil = False
    try:
        marker = my_database.cursor()

        isbn = isbn_eks.get()
        eksnr = eksnr_eks.get()

        m_eks = ('INSERT INTO Eksemplar'
                 '(ISBN, EksNr)'
                 'VALUES(%s, %s)')
        d_eks = (isbn, eksnr)

        marker.execute(m_eks, d_eks)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prøv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Eksemplaret er lagt til')

        else:
            feil = False


def delete_eksemplar_database():
    feil = False
    try:
        marker = my_database.cursor()

        isbn = isbn_eks.get()
        eksnr = eksnr_eks.get()

        m_eks = ('DELETE FROM Eksemplar '
                 'WHERE ISBN = %s and EksNr = %s')
        d_eks = (isbn, eksnr)

        marker.execute(m_eks, d_eks)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prøv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Eksemplaret er slettet')

        else:
            feil = False


def add_laaner_database():
    feil = False
    try:
        marker = my_database.cursor()

        lnr = lnr_lnr.get()
        fornavn = fornavn_lnr.get()
        etternavn = etternavn_lnr.get()

        m_l = ('INSERT INTO Laaner'
               '(LNr, Fornavn, Etternavn)'
               'VALUES(%s, %s, %s)')
        d_l = (lnr, fornavn, etternavn)

        marker.execute(m_l, d_l)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prøv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Låner er lagt til')

        else:
            feil = False


def change_laaner_database():
    feil = False
    try:
        marker = my_database.cursor()

        lnr = lnr_lnr.get()
        fornavn = fornavn_lnr.get()
        etternavn = etternavn_lnr.get()

        m_l = ('DELETE FROM Laaner '
               'WHERE LNr = %s')
        d_l = lnr

        marker.execute(m_l, d_l)
        my_database.commit()

        m_l = ('INSERT INTO Laaner'
               '(LNr, Fornavn, Etternavn)'
               'VALUES(%s, %s, %s)')
        d_l = (lnr, fornavn, etternavn)

        marker.execute(m_l, d_l)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prøv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Låner er endret')

        else:
            feil = False


def delete_laaner_database():
    feil = False
    try:
        marker = my_database.cursor()

        lnr = lnr_lnr.get()

        m_l = ('DELETE FROM Laaner '
               'WHERE LNr = %s')
        d_l = lnr

        marker.execute(m_l, d_l)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prøv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Låner er slettet')

        else:
            feil = False


def add_utlaan_database():
    feil = False
    try:
        marker = my_database.cursor()

        marker.execute('SELECT UtlaansNr '
                       'FROM Utlaan')

        liste = []
        hold = 999
        for row in marker:
            liste = list(row)
            for r in liste:
                bruk = int(r)
                if hold < bruk:
                    hold = bruk
        hold += 1

        utlaansnr = hold
        lnr = lnr_utlaan.get()
        isbn = isbn_utlaan.get()
        eksnr = eksnr_utlaan.get()
        utlaansdato = utlaansdato_utlaan.get()
        innleveringsdato = None

        m_l = ('INSERT INTO Utlaan'
               '(UtlaansNr, LNr, ISBN, EksNr, Utlaansdato, Innleveringsdato)'
               'VALUES(%s, %s, %s, %s, %s, %s)')
        d_l = (utlaansnr, lnr, isbn, eksnr, utlaansdato, innleveringsdato)

        marker.execute(m_l, d_l)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prOv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Utlaanet er registrert')

        else:
            feil = False


def innlevering_utlaan_database():
    feil = False
    try:
        marker = my_database.cursor()

        isbn = isbn_utlaan.get()
        eksnr = eksnr_utlaan.get()
        innleveringsdato = innlevering_utlaan.get()

        m_l = ('UPDATE Utlaan '
               'SET Innleveringsdato = %s '
               'WHERE Innleveringsdato IS NULL AND ISBN = %s AND EksNr = %s')

        d_l = (innleveringsdato, isbn, eksnr)

        marker.execute(m_l, d_l)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prOv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Innleveringen er registrert')

        else:
            feil = False


def delete_utlaan_database():

    feil = False
    try:
        marker = my_database.cursor()

        isbn = isbn_utlaan.get()

        m_l = ('DELETE FROM Utlaan '
               'WHERE ISBN = %s'
               'AND Innleveringsdato IS NOT NULL')
        d_l = isbn

        marker.execute(m_l, d_l)
        my_database.commit()

        marker.close()

    except:
        messagebox.showinfo(message='Noe gikk galt, prøv igjen!')
        feil = True

    finally:
        if feil == False:
            messagebox.showinfo(message='Utlaanet er slettet')

        else:
            feil = False


def add_book_gui():
    add_book = Toplevel()
    add_book.title('Bokadministrasjon')

    ttk.Label(add_book, text='Administrering av bok i databasen: Fagbokbibliotek').grid(row=1, column=1,
                                                                                        columnspan=2, pady=15)
    ttk.Separator(add_book).grid(row=2, column=1, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(add_book, text='ISBN(13)(*)').grid(row=3, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_book, textvariable=isbn_bok).grid(row=3, column=2)

    ttk.Label(add_book, text='Tittel').grid(row=4, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_book, textvariable=tittel_bok).grid(row=4, column=2)

    ttk.Label(add_book, text='Forfatter').grid(row=5, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_book, textvariable=forfatter_bok).grid(row=5, column=2)

    ttk.Label(add_book, text='Forlag').grid(row=6, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_book, textvariable=forlag_bok).grid(row=6, column=2)

    ttk.Label(add_book, text='UtgittAar').grid(row=7, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_book, textvariable=utgitt_aar_bok).grid(row=7, column=2)

    ttk.Label(add_book, text='Antall Sider').grid(row=8, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_book, textvariable=antall_sider_bok).grid(row=8, column=2)

    ttk.Separator(add_book).grid(row=9, column=1, columnspan=2, pady=5, sticky=(W, E))

    ttk.Button(add_book, text='Legg til bok', command=add_book_database).grid(row=10, column=1, padx=5,
                                                                              pady=5, sticky=W)
    ttk.Button(add_book, text='Endre bok', command=change_book_database).grid(row=10, column=1, columnspan=2,
                                                                              padx=105, pady=5, sticky=E)
    ttk.Button(add_book, text='Slett bok(*)', command=delete_book_database).grid(row=10, column=2, padx=5, pady=5,
                                                                                 columnspan=2, sticky=E)

    ttk.Button(add_book, text='Tilbake', command=add_book.destroy).grid(row=11, column=2, padx=5, pady=5, sticky=E)


def add_eksemplar_gui():
    add_eksemplar = Toplevel()
    add_eksemplar.title('Eksemplar Administrasjon')

    ttk.Label(add_eksemplar, text='Administrering av eksemplar i databasen: Fagbokbibliotek').grid(row=1,
                                                                                                   column=1,
                                                                                                   columnspan=2,
                                                                                                   pady=15)
    ttk.Separator(add_eksemplar).grid(row=2, column=1, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(add_eksemplar, text='ISBN(13)').grid(row=3, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_eksemplar, textvariable=isbn_eks).grid(row=3, column=2)

    ttk.Label(add_eksemplar, text='EksNr').grid(row=4, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_eksemplar, textvariable=eksnr_eks).grid(row=4, column=2)

    ttk.Separator(add_eksemplar).grid(row=5, column=1, columnspan=2, pady=5, sticky=(W, E))

    ttk.Button(add_eksemplar, text='Legg til eksemplar', command=add_eksemplar_database).grid(row=6, column=1, padx=5,
                                                                                              pady=5, sticky=W)
    ttk.Button(add_eksemplar, text='Slett eksemplar', command=delete_eksemplar_database).grid(row=6, column=2, padx=5,
                                                                                              pady=5, columnspan=2,
                                                                                              sticky=E)

    ttk.Button(add_eksemplar, text='Tilbake', command=add_eksemplar.destroy).grid(row=7, column=2, padx=5, pady=5,
                                                                                  sticky=E)


def add_laanetager_gui():
    add_laanetager = Toplevel()
    add_laanetager.title('Laaner Administrasjon')

    ttk.Label(add_laanetager, text='Administrering av laanetager i databasen: Fagbokbibliotek').grid(row=1, column=1,
                                                                                                     columnspan=2,
                                                                                                     pady=15)
    ttk.Separator(add_laanetager).grid(row=2, column=1, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(add_laanetager, text='LNr(4)(*)').grid(row=3, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_laanetager, textvariable=lnr_lnr).grid(row=3, column=2)

    ttk.Label(add_laanetager, text='Fornavn').grid(row=4, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_laanetager, textvariable=fornavn_lnr).grid(row=4, column=2)

    ttk.Label(add_laanetager, text='Etternavn').grid(row=5, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_laanetager, textvariable=etternavn_lnr).grid(row=5, column=2)

    ttk.Separator(add_laanetager).grid(row=6, column=1, columnspan=2, pady=5, sticky=(W, E))

    ttk.Button(add_laanetager, text='Legg til laaner', command=add_laaner_database).grid(row=7, column=1,
                                                                                         padx=5, pady=5, sticky=W)
    ttk.Button(add_laanetager, text='Endre laaner', command=change_laaner_database).grid(row=7, column=1, columnspan=2,
                                                                                         padx=5, pady=5)
    ttk.Button(add_laanetager, text='Slett laaner(*)', command=delete_laaner_database).grid(row=7, column=2,
                                                                                            padx=5, pady=5, sticky=E)

    ttk.Button(add_laanetager, text='Tilbake', command=add_laanetager.destroy).grid(row=8, column=2,
                                                                                    padx=5, pady=5, sticky=E)


def add_utlaan_gui():
    add_utlaan = Toplevel()
    add_utlaan.title('Utlaan Administrasjon')

    ttk.Label(add_utlaan, text='Administrering av utlaan i databasen: Fagbokbibliotek').grid(row=1, column=1,
                                                                                             columnspan=2, pady=15)
    ttk.Separator(add_utlaan).grid(row=2, column=1, columnspan=2, pady=5, sticky=(W, E))

    ttk.Label(add_utlaan, text='LNr(4)').grid(row=4, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_utlaan, textvariable=lnr_utlaan).grid(row=4, column=2)

    ttk.Label(add_utlaan, text='ISBN(13)(*)(-)').grid(row=5, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_utlaan, textvariable=isbn_utlaan).grid(row=5, column=2)

    ttk.Label(add_utlaan, text='EksNr(*)(-)').grid(row=6, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_utlaan, textvariable=eksnr_utlaan).grid(row=6, column=2)

    ttk.Label(add_utlaan, text='Utlaansdato').grid(row=7, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_utlaan, textvariable=utlaansdato_utlaan).grid(row=7, column=2)

    ttk.Label(add_utlaan, text='Innleveringsdato(-)').grid(row=8, column=1, padx=5, pady=5, sticky=W)
    ttk.Entry(add_utlaan, textvariable=innlevering_utlaan).grid(row=8, column=2)

    ttk.Separator(add_utlaan).grid(row=9, column=1, columnspan=2, pady=5, sticky=(W, E))

    ttk.Button(add_utlaan, text='Laan ut bok', command=add_utlaan_database).grid(row=10, column=1, padx=5, pady=5,
                                                                                 sticky=W)
    ttk.Button(add_utlaan, text='Slett utlaan(*)', command=delete_utlaan_database).grid(row=10, column=1, columnspan=2,
                                                                                     padx=5, pady=5)
    ttk.Button(add_utlaan, text='Innlevering(-)', command=innlevering_utlaan_database).grid(row=10, column=2, padx=5,
                                                                                            pady=5, sticky=E)

    ttk.Button(add_utlaan, text='Tilbake', command=add_utlaan.destroy).grid(row=11, column=2, padx=5, pady=5, sticky=E)


def oversikt_gui():
    oversikt = Toplevel()
    oversikt.title('Oversikter')

    ttk.Label(oversikt, text="Oversikter").grid(row=0, column=1, padx=5, pady=15)
    ttk.Separator(oversikt).grid(row=1, column=1, columnspan=5, pady=5, ipadx=300, sticky=(W, E))

    ttk.Label(oversikt, text="Alle utlaan som ikke er levert tilbake med info om laanetager:").grid(row=2, column=1,
                                                                                                    padx=5, pady=5,
                                                                                                    sticky=W)
    ttk.Button(oversikt, text='Klikk her', command=ovr1).grid(row=2, column=2, padx=5, pady=5, sticky=E)

    ttk.Label(oversikt, text="BOker som aldri har vaert utlaant:").grid(row=3, column=1, padx=5, pady=5, sticky=W)
    ttk.Button(oversikt, text='Klikk her', command=ovr2).grid(row=3, column=2, padx=5, pady=5, sticky=E)

    ttk.Label(oversikt, text="Utlaansstatistikk for alle bOker samlet:").grid(row=4, column=1, padx=5, pady=5, sticky=W)
    ttk.Button(oversikt, text='Klikk her', command=ovr3).grid(row=4, column=2, padx=5, pady=5, sticky=E)

    global listbox
    listbox = Listbox(oversikt, height=20)
    listbox.grid(row=5, column=1, columnspan=3, sticky=(N, W, E, S))

    s = ttk.Scrollbar(oversikt, orient=VERTICAL, command=listbox.yview)
    s.grid(row=5, column=3, sticky=(N, S, E))
    listbox['yscrollcommand'] = s.set
    ttk.Sizegrip().grid(row=5, column=1, sticky=(S, E))
    oversikt.grid_columnconfigure(1, weight=1)
    oversikt.grid_rowconfigure(1, weight=1)

    ttk.Button(oversikt, text="Tilbake", command=oversikt.destroy).grid(row=6, column=3, padx=5, pady=10, stick=E)


def ovr1():
    listbox.delete(0, 'end')
    marker = my_database.cursor()

    marker.execute(
        'SELECT U.UtlaansNr, U.LNr, U.ISBN, U.EksNr, U.Utlaansdato, L.Fornavn, L.Etternavn '
        'FROM Utlaan AS U, Laaner AS L '
        'WHERE U.LNr = L.LNr AND U.Innleveringsdato IS NULL')
    listbox.insert('end', 'UtlaansNr ' 'LNr ' 'ISBN ' 'EksNr ' 'Utlaansdato ' 'Fornavn ' 'Etternavn')

    for row in marker:
        listbox.insert('end', row)

    marker.close()


def ovr2():
    listbox.delete(0, 'end')
    marker = my_database.cursor()

    marker.execute(
        'SELECT * '
        'FROM Bok AS B '
        'WHERE B.ISBN NOT IN (SELECT U.ISBN FROM Utlaan AS U WHERE (B.ISBN = U.ISBN))')
    listbox.insert('end', 'ISBN ' 'Tittel ' 'Forfatter ' 'Forlag ' 'UtgittAar ' 'AntallSider ')

    for row in marker:
        listbox.insert('end', row)

    marker.close()


def ovr3():
    listbox.delete(0, 'end')
    marker = my_database.cursor()

    marker.execute(
        'SELECT B.ISBN, Tittel, Forfatter, Forlag, UtgittAar, AntallSider, COUNT(*) '
        'FROM Bok AS B, Utlaan AS U '
        'WHERE B.ISBN = U.ISBN '
        'GROUP BY B.ISBN')
    listbox.insert('end', 'ISBN ' 'Tittel ' 'Forfatter ' 'Forlag ' 'UtgittAar ' 'AntallSider ' 'AntallGangerLaant')

    for row in marker:
        listbox.insert('end', row)

    marker.close()


my_database = pymysql.connect(host='localhost', port=3306, user='Biblioteksjef', passwd='bibliotek2017',
                              db='Fagbokbibliotek')
root = Tk()
fag = root.title("Fagbokbibliotek")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(row=0, column=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Administrering for databasen Fagbibliotek').grid(row=0, column=0, columnspan=3, pady=5,
                                                                            sticky=(W, E))

ttk.Separator(mainframe, orient=HORIZONTAL).grid(row=1, column=0, columnspan=4, pady=3, sticky=(W, E))

lbl_adm_book = Label(mainframe, text='Administrasjon av Bok: ').grid(row=2, column=0, padx=5, pady=3, sticky=W)
btn_adm_book = Button(mainframe, text='Bokadministrasjon', command=add_book_gui).grid(row=2, column=1, pady=3, padx=5,
                                                                                      sticky=(W, E))

lbl_adm_eks = Label(mainframe, text='Administrasjon av Eksemplar:').grid(row=3, column=0, padx=5, pady=3, sticky=W)
btn_adm_eks = Button(mainframe, text='Eksemplaradministrasjon', command=add_eksemplar_gui).grid(row=3, column=1, pady=3,
                                                                                                padx=5, sticky=(W, E))

lbl_adm_loaners = Label(mainframe, text='Administrasjon av Laaner: ').grid(row=4, column=0, padx=5, pady=3,
                                                                                sticky=W)
btn_adm_loaners = Button(mainframe, text='Laanetageradministrasjon', command=add_laanetager_gui).grid(row=4, column=1,
                                                                                                      padx=5, pady=3,
                                                                                                      sticky=(W, E))

lbl_adm_loan = Label(mainframe, text='Administrasjon av Utlaan: ').grid(row=5, column=0, padx=5, pady=3, sticky=W)
btn_adm_loan = Button(mainframe, text='Utlaanadministrasjon', command=add_utlaan_gui).grid(row=5, column=1, padx=5,
                                                                                           pady=3, sticky=(W, E))

lbl_adm_stats = Label(mainframe, text='Oversikter/Statistikker: ').grid(row=6, column=0, padx=5, pady=3, sticky=W)
btn_adm_stats = Button(mainframe, text='Oversikt/Statistikker', command=oversikt_gui).grid(row=6, column=1, padx=5,
                                                                                           pady=3, sticky=(W, E))

ttk.Separator(mainframe, orient=HORIZONTAL).grid(row=7, column=0, columnspan=4, pady=3, sticky=(W, E))

btn_close = Button(mainframe, text='Avslutt', command=root.destroy).grid(row=8, column=2, padx=5, pady=3, sticky=(W, E))

# StringVar verdier
isbn_bok = StringVar()
tittel_bok = StringVar()
forfatter_bok = StringVar()
forlag_bok = StringVar()
utgitt_aar_bok = StringVar()
antall_sider_bok = StringVar()

isbn_eks = StringVar()
eksnr_eks = StringVar()

lnr_lnr = StringVar()
fornavn_lnr = StringVar()
etternavn_lnr = StringVar()

utlaansnr_utlaan = StringVar()
lnr_utlaan = StringVar()
isbn_utlaan = StringVar()
eksnr_utlaan = StringVar()
utlaansdato_utlaan = StringVar()
innlevering_utlaan = StringVar()

# Boolske verdier
feil = False

root.mainloop()

my_database.close()
