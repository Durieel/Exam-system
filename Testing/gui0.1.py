from tkinter import *
from tkinter import ttk
import pymysql





mydb = pymysql.connect(host='localhost', port=3306, user='Eksamenssjef', passwd='eksamen2017', db='Eksamen')

root = Tk()
root.title("Eksamensapplikasjon")
mainframe = ttk.Frame(root, padding="6 6 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Administrering") .grid(column= 0, row= 0)
ttk.Separator(mainframe) .grid(columnspan=2)
ttk.Button(mainframe, text="Registrer ny eksamen") .grid(column= 0, row= 1, sticky= (E, W))
ttk.Button(mainframe, text="Registrer karakter") .grid(column= 0, row= 2, sticky= (E, W))
ttk.Button(mainframe, text="Studentadministrasjon") .grid(column= 0, row= 3, sticky= (E, W))

ttk.Labelframe(mainframe, text='Pane1', width=100, height=100).grid(column= 1, row= 0, rowspan=4, sticky=W)
ttk.Label(mainframe, text='Fyll inn alle teksfelter og trykk Legg til student').grid(column= 2, row= 0, rowspan=4, sticky=W)

n = ttk.Notebook(mainframe, width=300, height=300).grid(column=0, row=4)
f1 = ttk.Frame(n)  # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)  # second page
f3 = ttk.Frame(n)  # second page
n.add(f1, text='Legg til ny student')
n.add(f2, text='Rediger eksisterende student')
n.add(f3, text='Slett eksisterende student')

"""
ttk.Label(mainframe, text="Utskrifter/oversikter") .grid(column= 1, row= 0)
ttk.Button(mainframe, text="Alle eksamen på en dag") .grid(column= 1, row= 1, sticky= (E, W))
ttk.Button(mainframe, text="Alle eksamen i en periode") .grid(column= 1, row= 2, sticky= (E, W))
ttk.Button(mainframe, text="Eksamensresultater i ett emne") .grid(column= 1, row= 3, sticky= (E, W))
ttk.Button(mainframe, text="Karakterstatistikk for gjennomført eksamen i ett emne") .grid(column= 1, row= 4, sticky= (E, W))
ttk.Button(mainframe, text="Alle eksamensresultater") .grid(column= 1, row= 5, sticky= (E, W))
ttk.Button(mainframe, text="Vitnemål for en student") .grid(column= 1, row= 6, sticky= (E, W))
"""

for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=5)






root.mainloop()