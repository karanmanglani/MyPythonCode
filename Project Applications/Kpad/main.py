import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

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
fontSize = ttk.Combobox(toolBar, width = 20, textvariable = sizeVar, state = 'readonly')
fontSizeTuple = tuple(range(8,80,2))
fontSize['values'] = fontSizeTuple
fontSize.current(fontSizeTuple.index(12))
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

currentFontFamily = 'Arial'
currentFontSize = 12
def setFont(mainApplication):
    global currentFontFamily
    currentFontFamily = fontFamily.get()
    global currentFontSize
    currentFontSize = sizeVar.get()
    textEditor.configure(font=(currentFontFamily,currentFontSize))
fontBox.bind('<<ComboboxSelected>>',setFont)
fontSize.bind('<<ComboboxSelected>>',setFont)

###### Buttons Functionality
## Bold Button
def changeBold():
    textProperty = tk.font.Font(font=textEditor['font'])
    if(textProperty.actual()['weight'] == 'normal'):
        textEditor.configure(font=(currentFontFamily,currentFontSize,'bold'))
    else:
        textEditor.configure(font=(currentFontFamily,currentFontSize,'normal'))

boldBtn.configure(command=changeBold)

## Itallics Button
def changeItalic():
    textProperty = tk.font.Font(font=textEditor['font'])
    if(textProperty.actual()['slant'] == 'roman'):
        textEditor.config(font=(currentFontFamily,currentFontSize,'italic'))
    else:
        textEditor.config(font=(currentFontFamily,currentFontSize,'roman'))

italicBtn.configure(command=changeItalic)
## Underline Button
def changeUnderline():
    textProperty = tk.font.Font(font=textEditor['font'])
    if(textProperty.actual()['underline'] == 0):
        textEditor.config(font=(currentFontFamily,currentFontSize,'underline'))
    else:
        textEditor.config(font=(currentFontFamily,currentFontSize,'normal'))

underlineBtn.configure(command=changeUnderline)

## Font Color Functionality
def changeFontColor():
    colorVar = tk.colorchooser.askcolor()
    textEditor.configure(fg=colorVar[1])

fontColorBtn.configure(command = changeFontColor)
## Align Functionality
def alignLeft():
    textContent = textEditor.get(1.0,'end')
    textEditor.tag_config('left',justify=tk.LEFT)
    textEditor.delete(1.0,tk.END)
    textEditor.insert(tk.INSERT,textContent,'left')
alignLeftBtn.configure(command=alignLeft)

def alignRight():
    textContent = textEditor.get(1.0,'end')
    textEditor.tag_config('right',justify=tk.RIGHT)
    textEditor.delete(1.0,tk.END)
    textEditor.insert(tk.INSERT,textContent,'right')
alignRightBtn.configure(command=alignRight)

def alignCenter():
    textContent = textEditor.get(1.0,'end')
    textEditor.tag_config('center',justify=tk.CENTER)
    textEditor.delete(1.0,tk.END)
    textEditor.insert(tk.INSERT,textContent,'center')
alignCenterBtn.configure(command=alignCenter)

textEditor.configure(font=('Arial',12))

######################## Ending of text editor ######################

######################## StatusBar ################################

statusBar = ttk.Label(mainApplication, text='Status Bar')
statusBar.pack(side=tk.BOTTOM)

textChanged = False
def changed(event=None):
    if textEditor.edit_modified():
        global textChanged
        textChanged = True
        words = len(textEditor.get(1.0, 'end-1c').split())
        characters = len(textEditor.get(1.0,'end-1c'))
        charactersNoSpace = len(textEditor.get(1.0,'end-1c').replace(' ',''))
        statusBar.config(text=f'Characters : {characters} Characters(not space) : {charactersNoSpace} Words : {words} ')
    textEditor.edit_modified(False)

textEditor.bind('<<Modified>>',changed)
######################## Ending of StatusBar ######################

####################### Main Menu Functionality ##################
url = ''
# New functionality
def newFile(event = None):
    global url
    url = ''
    textEditor.delete(1.0,tk.END)

# Open Functionality
def openFile(event=None):
    global url,textChanged
    if textChanged:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file ??')
            if mbox is True:
                saveFile()
    
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File ','*.txt'), ('All Files ','*.*')))
    try:
        with open(url,'r') as fr:
            textEditor.delete(1.0,tk.END)
            textEditor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    mainApplication.title(os.path.basename(url))

# Save Functionality
def saveFile(event=None):
    global url
    try:
        if url:
            content = str(textEditor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
                mainApplication.title(os.path.basename(url))
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File ','*.txt'), ('All files ','*.*')))
            content = textEditor.get(1.0,tk.END)
            url.write(content)
            url.close()
            mainApplication.title(os.path.basename(url))
    except:
        return

def saveAsFile(event=None):
    global url
    try:
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(('Text Files ','*.txt'),('All files','*.*')))
        content = textEditor.get(1.0,tk.END)
        url.write(content)
        url.close()
        mainApplication.title(os.path.basename(url))
    except:
        return

## Exit Functionality
def exitFile(event=None):
    global url,textChanged
    try:
        if textChanged:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file ?? ')
            if mbox is True:
                saveFile()
                mainApplication.destroy()
            elif mbox is False:
                mainApplication.destroy()
            else:
                mainApplication.destroy()
    except:
        return

#### As in Procedural programming functions should be declared before use therefore file commands are added in the end and function is defined before
# Adding File Commands
file.add_command(label="New",image=newIcon, compound=tk.LEFT, accelerator='Ctrl+N', command = newFile)
file.add_command(label="Open",image=openIcon, compound=tk.LEFT, accelerator='Ctrl+O',command=openFile)
file.add_command(label="Save",image=saveIcon, compound=tk.LEFT, accelerator='Ctrl+S',command=saveFile)
file.add_command(label="Save As",image=saveAsIcon, compound=tk.LEFT, accelerator='Ctrl+Alt+S',command=saveAsFile)
file.add_command(label="Exit",image=exitIcon, compound=tk.LEFT, accelerator='Ctrl+Q',command=exitFile)

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