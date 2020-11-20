import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
# Importing parts of our application 
import mainMenu as mm
import toolbar as tb
import textEditor as te
import statusBar as sb

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
##### GUI #####
toolBar = ttk.Label(mainApplication)
toolBar.pack(side=tk.TOP, fill = tk.X)

## Font Box
fontTuple = tk.font.families()
fontFamily = tk.StringVar()
fontBox = ttk.Combobox(toolBar, width = 30, textvariable = fontFamily, state = 'readonly')
fontBox['values'] = fontTuple
fontBox.current(fontTuple.index('Arial'))
fontBox.grid(row = 0, column = 0, padx = 5)

## Size Box
sizeVar = tk.IntVar()
fontSize = ttk.Combobox(toolBar, width = 20, textvariable = sizeVar)
fontSize['values'] = tuple(range(8,80,2))
fontSize.current = 32
fontSize.grid(row=0, column=1, padx = 5)

## bold button
boldIcon = tk.PhotoImage(file='./Icons/bold.png')
boldBtn = ttk.Button(toolBar, image=boldIcon)
boldBtn.grid(row=0, column=2, padx = 5)

## Italic Button
italicIcon = tk.PhotoImage(file='./Icons/italic.png')
italicBtn = ttk.Button(toolBar, image=italicIcon)
italicBtn.grid(row=0, column=3, padx = 5)

## Underline button
underlineIcon = tk.PhotoImage(file='./Icons/underline.png')
underlineBtn = ttk.Button(toolBar, image = underlineIcon)
underlineBtn.grid(row=0, column=4, padx = 5)

## Font Colour Button
fontColorIcon = tk.PhotoImage(file='./Icons/font_color.png')
fontColorBtn = ttk.Button(toolBar, image=fontColorIcon)
fontColorBtn.grid(row=0,column=5,padx= 5)

## Align Left Button
alignLeftIcon = tk.PhotoImage(file='./Icons/align_left.png')
alignLeftBtn = ttk.Button(toolBar, image= alignLeftIcon)
alignLeftBtn.grid(row=0, column=6, padx = 5)

## Align Center Button
alignCenterIcon = tk.PhotoImage(file='./Icons/align_center.png')
alignCenterBtn = ttk.Button(toolBar, image= alignCenterIcon)
alignCenterBtn.grid(row=0,column=7,padx=5)

## Align Right Button
alignRightIcon = tk.PhotoImage(file='./Icons/align_right.png')
alignRightBtn = ttk.Button(toolBar, image=alignRightIcon)
alignRightBtn.grid(row=0,column=8,padx=5)

######################## Ending of toolbar ######################

######################## text editor ################################
###### GUI ###########

textEditor = tk.Text(mainApplication)
textEditor.config(wrap='word',relief=tk.FLAT)

scrollBar = tk.Scrollbar(mainApplication)
textEditor.focus_set()
scrollBar.pack(side=tk.RIGHT, fill = tk.Y)
textEditor.pack(fill=tk.BOTH, expand=True)
scrollBar.config(command=textEditor.yview)
textEditor.config(yscrollcommand=scrollBar.set)

######################## Ending of text editor ######################

######################## StatusBar ################################

statusBar = ttk.Label(mainApplication, text='Status Bar')
statusBar.pack(side=tk.BOTTOM)

######################## Ending of StatusBar ######################

####################### Main Menu Functionality ##################



#### As in Procedural programming functions should be declared before use therefore file commands are added in the end and function is defined before
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