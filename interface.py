from telnetlib import GA
from tkinter import *
from tkinter import font
from turtle import bgcolor
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from filter import get
import sqlite3
conn = sqlite3.connect("mails.db")
conn.row_factory = lambda cursor, row: row[0]
cur = conn.cursor()
root = Tk()

def printitem():
    get = listbox.curselection()
    for i in get:
        print(listbox.get(i))

def delitem():
    deleted = listbox.curselection()
    for i in deleted:
        listbox.delete(i)
        print('One item Deleted')

btn2 = ttk.Button(root, text='Segment', command=delitem,bootstyle="primary" ,font=('Helvetica', 12)).grid(row=0,column=5)
Change =ttk.Button(root, text='Change', command=printitem,bootstyle="success").grid(row=0,column=7,pady=(20,0))



# Pick up List
middle_click = ttk.Labelframe(
            root,
            text='Middle Click',
            padding=(15, 10)
        )

cbo = ttk.Combobox(
            root,
            values=['DZ', 'PRO', 'CASUAL','Garbage'], font=('Arial',15)
        )
cbo.current(0)
cbo.grid(row=0,column=8)
# Option
# Option = Listbox(root,width=15, height=4, selectmode=SINGLE)
# Option.grid(row=0,column=10,padx=(0,10),pady=(20,0))
# Option.insert(0, 'DZ')
# Option.insert(1, 'PRO')
# Option.insert(2, 'CASUAL')
# Option.insert(3, 'GARBAGE')
# DZ List
DZ = Listbox(root,width=30, height=20, selectmode=MULTIPLE,font=("Arial", 15))

# DZ.pack(padx=5, pady=20, side=LEFT)
labelDz = ttk.Label(root,
                    text = "DZ",font=("Arial", 15))
labelDz.grid(column=5, row=4,pady=(100,10))
DZ.grid(row=5,column=5,padx=(20,20))
dz_list_item=get(cur,'DZ')
i=0
for j in dz_list_item:

    DZ.insert(i, j)
    i=i+1


# PRO list
labelPRO = ttk.Label(root,
                    text = "PRO",font=("Arial", 15))
labelPRO.grid(column=6, row=4,pady=(100,10))
PRO = Listbox(root, width=30, height=20, selectmode=MULTIPLE,  font=("Arial", 15))
# PRO.pack(padx=5, pady=25, side=LEFT)
PRO.grid(row=5,column=6,padx=(20,20))
Pro_list_item=get(cur,'PRO')
for j in Pro_list_item:

    PRO.insert(i, j)
    i=i+1



# Casual List 
labelCasual = ttk.Label(root,
                    text = "Casual",font=("Arial", 15))
labelCasual.grid(column=7, row=4,pady=(100,10))
Casual = Listbox(root, width=30, height=20, selectmode=MULTIPLE,font=("Arial", 15))
# Casual.pack(padx=5, pady=25, side=LEFT)
Casual_list_item=get(cur,'CASUAL')
Casual.grid(row=5,column=7,padx=(20,20))
for j in Casual_list_item:

    Casual.insert(i, j)
    i=i+1

# Garbage List
labelGarbage = ttk.Label(root,
                    text = "Garbage",font=("Arial", 15))
labelGarbage.grid(column=8, row=4,pady=(100,10))
Garbage = Listbox(root, width=30, height=20, selectmode=MULTIPLE,font=("Arial", 15))
# Garbage.pack(padx=5, pady=30, side=LEFT)
Garbage.grid(row=5,column=8,padx=(20,20))
Garbage_list_item=get(cur,'ERROR')
for j in Garbage_list_item:

    Garbage.insert(i, j)
    i=i+1






root.geometry('1500x800')
root.resizable(width=0, height=0)
root.title('PythonLobby.com')
root.mainloop()


