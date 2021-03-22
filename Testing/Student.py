from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql





telefon = StringVar()
epost = StringVar()
etternavn = StringVar()
fornavn = StringVar()
studentnr = StringVar()

add_student = Toplevel()
add_student.title('Student')

ttk.Label(add_student, text='Administrering av bok i databasen: Eksamen').grid(row=1, column=1,
                                                                                    columnspan=2, pady=15)
ttk.Separator(add_student).grid(row=2, column=1, columnspan=2, pady=5, sticky=(W, E))

ttk.Label(add_student, text='Studentnr').grid(row=3, column=1, padx=5, pady=5, sticky=W)
ttk.Entry(add_student, textvariable=studentnr).grid(row=3, column=2)


ttk.Label(add_student, text='Fornavn').grid(row=4, column=1, padx=5, pady=5, sticky=W)
ttk.Entry(add_student, textvariable=fornavn).grid(row=4, column=2)


ttk.Label(add_student, text='Etternavn').grid(row=5, column=1, padx=5, pady=5, sticky=W)
ttk.Entry(add_student, textvariable=etternavn).grid(row=5, column=2)


ttk.Label(add_student, text='Epost').grid(row=6, column=1, padx=5, pady=5, sticky=W)
ttk.Entry(add_student, textvariable=epost).grid(row=6, column=2)


ttk.Label(add_student, text='Telefon').grid(row=7, column=1, padx=5, pady=5, sticky=W)
ttk.Entry(add_student, textvariable=telefon).grid(row=7, column=2)

ttk.Separator(add_student).grid(row=8, column=1, columnspan=2, pady=5, sticky=(W, E))

ttk.Button(add_student, text='Legg til bok').grid(row=9, column=1, padx=5,
                                                                          pady=5, sticky=W)
ttk.Button(add_student, text='Endre bok').grid(row=9, column=1, columnspan=2,
                                                                          padx=105, pady=5, sticky=E)
ttk.Button(add_student, text='Slett bok').grid(row=9, column=2, padx=5, pady=5,
                                                                             columnspan=2, sticky=E)

ttk.Button(add_student, text='Tilbake', command=add_student.destroy).grid(row=10, column=2, padx=5, pady=5, sticky=E)






