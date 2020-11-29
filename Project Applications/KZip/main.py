import tkinter as tk
from tkinter import ttk , filedialog , messagebox
import os
import file as f
import edit as e
import view as v
import taskbar as tbar
import body as bd
import statusbar as sbar 

mainApplication = tk.Tk()
mainApplication.geometry('1200x800')
mainApplication.title('Kzip file Archiver')
mainApplication.wm_iconbitmap('icon.ico')

####################### Main Menu ##################################
mainMenu = tk.Menu()

## File


# Adding File Menu
file = tk.Menu(mainMenu, tearoff = False)
# Adding File Commands
file.add_command(label='Open' , accelerator='Enter')
file.add_command(label='See/Edit', accelerator='F3')
file.add_command(label='Rename' , accelerator='F2')
file.add_command(label='Copy to',accelerator='F5')
file.add_command(label='Move to',accelerator='F6')
file.add_command(label='Delete',accelerator='Del')
file.add_command(label='Properties',accelerator='Alt+Enter')

## Edit
# Adding Edit Menu
edit = tk.Menu(mainMenu, tearoff = False)
# Adding Edit Commands
edit.add_command(label='Select All', accelerator='Ctrl+A')
edit.add_command(label='Deselect All', accelerator='Ctrl+D')
edit.add_command(label='Invert All',accelerator='Ctrl+I')

#Add Cascades
mainMenu.add_cascade(label='File',menu = file)
mainMenu.add_cascade(label='Edit',menu = edit)
#-------------&& End of main menu && -----------------------------#

##################### TaskBar ########################################

## Adding Icons
addIcon = tk.PhotoImage(file='')
extractIcon = tk.PhotoImage(file='')
copyIcon = tk.PhotoImage(file='')
moveIcon = tk.PhotoImage(file='')
deleteIcon = tk.PhotoImage(file='')
infoIcon = tk.PhotoImage(file='')
previousDirectoryIcon = tk.PhotoImage(file='')
## 
#------------------&& End of TaskBar &&------------------------------#

##################### Body ########################################
## Creating Container
body = tk.Listbox(mainApplication,bg='#857f7f')
body.pack(fill=tk.BOTH, expand=True)
## Gettng and seperating files and folders
currentDirectory = os.getcwd()
files = [f for f in os.listdir(currentDirectory) if os.path.isfile(os.path.join(currentDirectory, f))]
folders = [o for o in os.listdir(currentDirectory) if os.path.isdir(os.path.join(currentDirectory,o))]
## Adding Icons
folderIcon = tk.PhotoImage()
fileIcon = tk.PhotoImage()
## Inserting folders and files
count = 1
for f in folders:
    body.insert(count, f)
#------------------&& End of body &&------------------------------#

##################### Status Bar ##################################
statusBar = ttk.Label(mainApplication,text='Status Bar')
statusBar.pack(side=tk.BOTTOM)
#------------------&& End of Status Bar &&-------------------------

################## Working of main menu ###########################

#---------------- && End &&---------------------------------------#

mainApplication.config(menu=mainMenu)
mainApplication.mainloop()
