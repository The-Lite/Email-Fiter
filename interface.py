from telnetlib import GA
from tkinter import *
from tkinter import ttk

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
btn = Button(root, text='Clear', command=printitem).grid(row=0,column=0, padx=(20,10))
btn2 = Button(root, text='Segment', command=delitem).grid(row=0,column=1)
Change = Button(root, text='Change', command=printitem).grid(row=0,column=8,pady=(20,0))




# Option
Option = Listbox(root,width=15, height=4, selectmode=SINGLE)
Option.grid(row=0,column=10,padx=(0,10),pady=(20,0))
Option.insert(0, 'DZ')
Option.insert(1, 'PRO')
Option.insert(2, 'CASUAL')
Option.insert(3, 'GARBAGE')
# DZ List
DZ = Listbox(root,width=30, height=20, selectmode=MULTIPLE)

# DZ.pack(padx=5, pady=20, side=LEFT)
labelDz = ttk.Label(root,
                    text = "DZ")
labelDz.grid(column=5, row=4,pady=(200,10))
DZ.grid(row=5,column=5,padx=(20,20))
DZ.insert(0, 'C')
DZ.insert(1, 'C++')
DZ.insert(2, 'Java')
DZ.insert(3, 'Python')

# PRO list
labelPRO = ttk.Label(root,
                    text = "PRO")
labelPRO.grid(column=6, row=4,pady=(200,10))
PRO = Listbox(root, width=30, height=20, selectmode=MULTIPLE)
# PRO.pack(padx=5, pady=25, side=LEFT)
PRO.grid(row=5,column=6,padx=(20,20))
PRO.insert(0, 'C')
PRO.insert(1, 'C++')
PRO.insert(2, 'Java')
PRO.insert(3, 'Python')

# Casual List 
labelCasual = ttk.Label(root,
                    text = "Casual")
labelCasual.grid(column=7, row=4,pady=(200,10))
Casual = Listbox(root, width=30, height=20, selectmode=MULTIPLE)
# Casual.pack(padx=5, pady=25, side=LEFT)
Casual.grid(row=5,column=7,padx=(20,20))
Casual.insert(0, 'C')
Casual.insert(1, 'C++')
Casual.insert(2, 'Java')
Casual.insert(3, 'Python')

# Garbage List
labelGarbage = ttk.Label(root,
                    text = "Garbage")
labelGarbage.grid(column=8, row=4,pady=(200,10))
Garbage = Listbox(root, width=30, height=20, selectmode=MULTIPLE)
# Garbage.pack(padx=5, pady=30, side=LEFT)
Garbage.grid(row=5,column=8,padx=(20,20))

Garbage.insert(0, 'C')
Garbage.insert(1, 'C++')
Garbage.insert(2, 'Java')
Garbage.insert(3, 'Python')





Exit=Button(root,text="Search").grid(row=10,column=12,pady=(10,0))
root.geometry('1280x720')
root.title('PythonLobby.com')
root.mainloop()


