import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
# Importing parts of our application 
import mainMenu

mainApplication = tk.Tk()
mainApplication.geometry('1200x800')
mainApplication.title('Kpad text editor')


######################## Main Menu ################################
mainMenu = tk.Menu()
# File
file = tk.Menu(mainMenu, tearoff = False)


edit = tk.Menu(mainMenu, tearoff = False)
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