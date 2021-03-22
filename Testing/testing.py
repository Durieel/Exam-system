from tkinter import *
from tkinter import ttk

import pymysql

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


# Lager Treeview-widget
tree = ttk.Treeview(mainframe)

tree["columns"]=("1","2","3","4","5","6")
tree.column("#0", anchor="w", width=0)
tree.column("#1", width=100)
tree.column("#2", width=100)
tree.column("#3", width=100)
tree.column("#4", width=100)
tree.column("#5", width=100)
#tree.column("#6", width=100)
#tree.heading("#0", text='ID', anchor='w')
tree.heading("#1", text="Emnekode")
tree.heading("#2", text="Emnenavn")
tree.heading("#3", text="Studiepoeng")
tree.heading("#4", text="Dato")
tree.heading("#5", text="Karakter")
#tree.heading("#6", text="Studiepoeng Totalt")

ysb = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
tree['yscroll'] = ysb.set

# add tree and scrollbars to frame
tree.grid(row=3, column=0, sticky=NSEW)
ysb.grid(row=3, column=1, sticky=NS)



marker = mydb.cursor()

marker.execute(
    'SELECT * '
    'FROM Student ')

teller = 0 # Teller som holder styr på første kolonne
for row in marker:
   tree.insert('', 'end', text=str(teller), values=(row[0], row[1]))
   teller += 1 # Øking for hver gjennomgang

marker.close()

# set frame resize priorities
mainframe.rowconfigure(1, weight=1)
mainframe.columnconfigure(1, weight=1)




for child in mainframe.winfo_children():
    child.grid_configure(pady=5)

# Strenger for student
studentnr_1 = StringVar()





root.mainloop()




