import tkinter as tk
from tkinter import Label, Menu, ttk
from tkinter import messagebox, font
import os
from tkinter.constants import COMMAND
import basicTechniques

### Impoerting Crytographer Functions 
## Basic Cryptographers :-
    # Reverse Cipher
    # Ceaser Cipher
    # Transposition Cipher

## Creating Application
mainApplication = tk.Tk()
mainApplication.geometry('1200x800')
mainApplication.title('All in One Cryptographer')
mainApplication.wm_iconbitmap('icon.ico')


## Creating empty main menu
    # Getting all childrens packed
def allChildren(root):
    list = root.winfo_children()

    for item in list:
        if item.winfo_children():
            list.extend(item.winfo_children())
    
    return list

def removeChildrens(root):
    widgetList = allChildren(root)
    for item in widgetList:
        item.pack_forget()

## Creating Required Functions 
def reverseCipher(event=None):
    removeChildrens(mainApplication)
    def encrypt():
        messageLabel = ttk.Label(reverseCipherFrame,text='Encrypted Message')
        message =  basicTechniques.reverseCipher(messageInput.get())
        messageElement = tk.Text(reverseCipherFrame,height=3,width=50)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        messageLabel.grid(row=2,column=0,padx=30,pady=30)
        messageElement.grid(row=2,column=1,padx=30,pady=30)    
    def decrypt():
        messageLabel = ttk.Label(reverseCipherFrame,text='Decrypted Text : ')
        message =  basicTechniques.reverseCipher(messageInput.get())
        messageElement = tk.Text(reverseCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        messageLabel.grid(row=2,column=0,padx=30,pady=30)
        messageElement.grid(row=2,column=1,padx=30,pady=30)



    ## Creating reverseCipher Label Frame 
    reverseCipherFrame = ttk.LabelFrame(mainApplication,text='Reverse Cipher')
    reverseCipherFrame.pack(pady=20,padx=20)

    ## Creating a form and handling user input
    message = ttk.Label(reverseCipherFrame,text='Message to encrypt/Decrypt : ')
    message.grid(row=0,column=0,padx=30,pady=50)
    messageInput = ttk.Entry(reverseCipherFrame,width = 50)
    messageInput.grid(row=0,column=1,padx=30,pady=50)

    ## Encrypt and decrypt buttons
    encryptButton = ttk.Button(reverseCipherFrame,text='Encrypt',command=encrypt) 
    decryptButton = ttk.Button(reverseCipherFrame,text='Decrypt',command=decrypt) 
    encryptButton.grid(row=1,column=0,padx=30,pady=30)
    decryptButton.grid(row=1,column=1,padx=30,pady=30)


# Ceaser Cipher
def ceaserCipher(event = None):
    removeChildrens(mainApplication)
    def encrypt():
        messageLabel = ttk.Label(ceaserCipherFrame,text='Encrypted Message :')
        message =  basicTechniques.ceaserCipherEncrypt(messageInput.get(),int(keyInput.get()),alphabetListInput.get())
        messageElement = tk.Text(ceaserCipherFrame,height=3,width=50)
        messageElement.config(state="normal")
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageElement.grid(row=4,column=1,padx=30,pady=30)

    def decrypt():
        messageLabel = ttk.Label(ceaserCipherFrame,text='Decrypted Message :')
        message =  basicTechniques.ceaserCipherDecrypt(messageInput.get(),int(keyInput.get()),alphabetListInput.get())
        messageElement = tk.Text(ceaserCipherFrame,height=3,width=50)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageElement.grid(row=4,column=1,padx=30,pady=30)


    # Creating ceaser Cipher label frame
    ceaserCipherFrame = tk.LabelFrame(mainApplication,text='Ceaser Cipher')
    ceaserCipherFrame.pack(pady=20,padx=20)
    
    # Creating form and handling user input
    message = ttk.Label(ceaserCipherFrame,text='Message to encrypt/Decrypt : ')
    message.grid(row=0,column=0,padx=30,pady=45)
    messageInput = ttk.Entry(ceaserCipherFrame,width = 50)
    messageInput.grid(row=0,column=1,padx=30,pady=45)

    key = ttk.Label(ceaserCipherFrame,text='Key : ')
    key.grid(row=1,column=0,padx=30,pady=5)
    keyInput = ttk.Entry(ceaserCipherFrame,width=50)
    keyInput.grid(row=1,column=1,padx=30,pady=5)

    alphabetList = ttk.Label(ceaserCipherFrame,text='Alphabet List : ')
    alphabetList.grid(row=2,column=0,pady=45,padx=30)
    alphabetListInput = ttk.Entry(ceaserCipherFrame,width=50)
    alphabetListInput.grid(row=2,column=1,pady=45,padx=30)
    

    # Encrypt and Decrypt Buttons
    encryptButton = ttk.Button(ceaserCipherFrame,text='Encrypt',command=encrypt) 
    decryptButton = ttk.Button(ceaserCipherFrame,text='Decrypt',command=decrypt) 
    encryptButton.grid(row=3,column=0,padx=30,pady=30)
    decryptButton.grid(row=3,column=1,padx=30,pady=30)

    

# Basic Cryptographs


## Creating the main menu
mainMenu = tk.Menu()

# Creating menu tabs
basicCryptographs = tk.Menu(mainMenu,tearoff=False)
intermediateCryptographs = tk.Menu(mainMenu,tearoff=False)
advancedCryptographs = tk.Menu(mainMenu,tearoff=False)

# Adding menu items to basic menu
basicCryptographs.add_command(label='Revere Cipher',command=reverseCipher)
basicCryptographs.add_command(label='Ceaser Cipher',command=ceaserCipher)

# cascading menu tabs
mainMenu.add_cascade(label='Basic',menu=basicCryptographs)
mainMenu.add_cascade(label='Intermediate',menu = intermediateCryptographs)
mainMenu.add_cascade(label='Advanced',menu=advancedCryptographs)


## Creating requited buttons

mainApplication.config(menu=mainMenu)
mainApplication.mainloop()