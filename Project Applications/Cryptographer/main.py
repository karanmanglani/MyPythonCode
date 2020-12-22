import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font
import os
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

## Creating Required Functions 
def reverseCipher(event=None):
    def encrypt():
        message =  basicTechniques.reverseCipher(messageInput.get())
        messageElement = ttk.Label(reverseCipherFrame,text=message)
        messageElement.grid(row=2,column=0,padx=30,pady=30)
    
    def decrypt():
        message =  basicTechniques.reverseCipher(messageInput.get())
        messageElement = ttk.Label(reverseCipherFrame,text=message)
        messageElement.grid(row=2,column=0,padx=30,pady=30)

    ## Creating reverse cipher dialogue
    reverseCipherDialogue = tk.Toplevel()
    reverseCipherDialogue.geometry('1200x800')
    reverseCipherDialogue.wm_iconbitmap('icon.ico')
    reverseCipherDialogue.title('Reverse Cipher')

    ## Creating reverseCipher Label Frame 
    reverseCipherFrame = ttk.LabelFrame(reverseCipherDialogue,text='Reverse Cipher')
    reverseCipherFrame.pack(pady=20)

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

    reverseCipherDialogue.mainloop()

# Ceaser Cipher
def ceaserCipher(event = None):

    def encrypt():
        message =  basicTechniques.ceaserCipherEncrypt(messageInput.get(),int(keyInput.get()),alphabetListInput.get())
        messageElement = ttk.Label(ceaserCipherFrame,text=message)
        messageElement.grid(row=4,column=0,padx=30,pady=30)

    def decrypt():
        message =  basicTechniques.ceaserCipherDecrypt(messageInput.get(),int(keyInput.get()),alphabetListInput.get())
        messageElement = ttk.Label(ceaserCipherFrame,text=message)
        messageElement.grid(row=4,column=0,padx=30,pady=30)

    # Creating a new window for ceaser cipher
    ceaserCipherDialogue = tk.Toplevel()
    ceaserCipherDialogue.geometry('1200x800')
    ceaserCipherDialogue.wm_iconbitmap('icon.ico')
    ceaserCipherDialogue.title('Ceaser Cipher')

    # Creating ceaser Cipher label frame
    ceaserCipherFrame = tk.LabelFrame(ceaserCipherDialogue,text='Ceaser Cipher')
    ceaserCipherFrame.pack(pady=20)
    
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

    ceaserCipherDialogue.mainloop()

# Basic Cryptographs

def basicCryptographs(event = None):
    # Creating buttons
    reverseCipherBtn = ttk.Button(mainApplication,text='Perform Reverse Cipher',command=reverseCipher)
    ceaserCipherBtn = ttk.Button(mainApplication,text='Perform Ceaser Cipher',command=ceaserCipher)
    #Positioning Buttons
    reverseCipherBtn.grid(row=0,column=1,pady=20)
    ceaserCipherBtn.grid(row=1,column=1,pady=0)


# Good Cryptographers

def goodCryptographs(event=None):
    return None

# Advanced Cryptographs

def advancedCryptographs(event = None):
    return None

## Creating requited buttons
basicBtn = ttk.Button(mainApplication,text='Basic Cryptographers',command=basicCryptographs)
basicBtn.grid(row=0,column=0,pady=20,padx=10)

goodBtn = ttk.Button(mainApplication,text='Good Cryptographers',command=goodCryptographs)
goodBtn.grid(row=1,column=0,pady=0,padx=10)

advancedBtn = ttk.Button(mainApplication,text='advanced Cryptographers',command=advancedCryptographs)
advancedBtn.grid(row=2,column=0,pady=20,padx=10)

mainApplication.mainloop()