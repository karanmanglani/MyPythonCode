import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
# Importing parts of our application 
import mainMenu
import toolbar
import textEditor
import statusBar

mainApplication = tk.Tk()
mainApplication.geometry('1200x800')
mainApplication.title('Kpad text editor')


######################## Main Menu ################################
mainMenu = tk.Menu()

# File
# File Icons
newIcon = tk.PhotoImage(file='./Icons/new.png')
openIcon = tk.PhotoImage(file='./Icons/open.png')
saveIcon = tk.PhotoImage(file='./Icons/save.png')
saveAsIcon = tk.PhotoImage(file='./Icons/save_as.png')
exitIcon = tk.PhotoImage(file='./Icons/exit.png')

file = tk.Menu(mainMenu, tearoff = False) # Creatin File Menu
# Adding Commands
file.add_command(label="New",image=newIcon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label="Open",image=openIcon, compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label="Save",image=saveIcon, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label="Save As",image=saveAsIcon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label="Exit",image=exitIcon, compound=tk.LEFT, accelerator='Ctrl+Q')

# Edit
# Edit Icons
copyIcon = tk.PhotoImage(file='./Icons/copy.png')
pasteIcon = tk.PhotoImage(file='./Icons/paste.png')
cutIcon = tk.PhotoImage(file='./Icons/cut.png')
clearAllIcon = tk.PhotoImage(file='./Icons/clear_all.png')
findIcon = tk.PhotoImage(file='./Icons/find.png')

edit = tk.Menu(mainMenu, tearoff = False)

edit.add_command(label="Copy" , image=copyIcon, compound = tk.LEFT, accelerator = 'Ctrl + O')
edit.add_command(label="Paste" , image=pasteIcon, compound = tk.LEFT, accelerator = 'Ctrl + V')
edit.add_command(label="Cut" , image=cutIcon, compound = tk.LEFT, accelerator = 'Ctrl + X')
edit.add_command(label="Clear All" , image=clearAllIcon, compound = tk.LEFT, accelerator = 'Ctrl + Alt + C')
edit.add_command(label="Find" , image=findIcon, compound = tk.LEFT, accelerator = 'Ctrl + F')

view = tk.Menu(mainMenu, tearoff = False)
colorTheme = tk.Menu(mainMenu, tearoff = False)

# cascade
mainMenu.add_cascade(label='File',menu = file)
mainMenu.add_cascade(label='Edit',menu = edit)
mainMenu.add_cascade(label='View',menu = view)
mainMenu.add_cascade(label='Color Theme',menu = colorTheme)
######################## Ending of main menu ######################

######################## toolbar ################################

######################## Ending of toolbar ######################

######################## text editor ################################

######################## Ending of text editor ######################

######################## StatusBar ################################

######################## Ending of StatusBar ######################

mainApplication.config(menu=mainMenu)
mainApplication.mainloop()