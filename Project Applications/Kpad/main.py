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
################ GUI
mainMenu = tk.Menu()

# File
# File Icons
newIcon = tk.PhotoImage(file='./Icons/new.png')
openIcon = tk.PhotoImage(file='./Icons/open.png')
saveIcon = tk.PhotoImage(file='./Icons/save.png')
saveAsIcon = tk.PhotoImage(file='./Icons/save_as.png')
exitIcon = tk.PhotoImage(file='./Icons/exit.png')

file = tk.Menu(mainMenu, tearoff = False) # Creatin File Menu


# Edit
# Edit Icons
copyIcon = tk.PhotoImage(file='./Icons/copy.png')
pasteIcon = tk.PhotoImage(file='./Icons/paste.png')
cutIcon = tk.PhotoImage(file='./Icons/cut.png')
clearAllIcon = tk.PhotoImage(file='./Icons/clear_all.png')
findIcon = tk.PhotoImage(file='./Icons/find.png')

edit = tk.Menu(mainMenu, tearoff = False) #Creating edit  Menu


#View 
#View Icons
toolBarIcon = tk.PhotoImage(file="./Icons/tool_bar.png")
statusBarIcon = tk.PhotoImage(file="./Icons/status_bar.png")

view = tk.Menu(mainMenu, tearoff = False) # Creating view menu


# Color Themes
# Color theme icons
lightDefaultIcon = tk.PhotoImage(file='./Icons/light_default.png')
lightPlusIcon = tk.PhotoImage(file='./Icons/light_plus.png')
darkIcon = tk.PhotoImage(file='./Icons/dark.png')
redIcon = tk.PhotoImage(file='./Icons/red.png')
monokaiIcon = tk.PhotoImage(file='./Icons/monokai.png')
nightBlueIcon = tk.PhotoImage(file='./Icons/night_blue.png')

colorTheme = tk.Menu(mainMenu, tearoff = False) # Creating color theme icons


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

####################### Main Menu Functionality ##################

# Adding File Commands
file.add_command(label="New",image=newIcon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label="Open",image=openIcon, compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label="Save",image=saveIcon, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label="Save As",image=saveAsIcon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label="Exit",image=exitIcon, compound=tk.LEFT, accelerator='Ctrl+Q')

# Adding Edit Commands
edit.add_command(label="Copy" , image=copyIcon, compound = tk.LEFT, accelerator = 'Ctrl + O')
edit.add_command(label="Paste" , image=pasteIcon, compound = tk.LEFT, accelerator = 'Ctrl + V')
edit.add_command(label="Cut" , image=cutIcon, compound = tk.LEFT, accelerator = 'Ctrl + X')
edit.add_command(label="Clear All" , image=clearAllIcon, compound = tk.LEFT, accelerator = 'Ctrl + Alt + C')
edit.add_command(label="Find" , image=findIcon, compound = tk.LEFT, accelerator = 'Ctrl + F')

# Adding view commands
view.add_checkbutton(label="Tool Bar", image=toolBarIcon, compound=tk.LEFT)
view.add_checkbutton(label="Status Bar", image=statusBarIcon, compound=tk.LEFT)

# Adding color theme comamnds
themeChoice = tk.StringVar()
colorIcons = (lightDefaultIcon, lightPlusIcon, darkIcon, redIcon, monokaiIcon, nightBlueIcon)

colorDict = {
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2'),
}

count = 0
for i in colorDict:
    colorTheme.add_radiobutton(label=i,image = colorIcons[count],variable = themeChoice, compound = tk.LEFT)
    count += 1

####################### Ending of Main Menu Functionality ##################

mainApplication.config(menu=mainMenu)
mainApplication.mainloop()