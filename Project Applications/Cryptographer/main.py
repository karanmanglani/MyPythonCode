import tkinter as tk
from tkinter import Label, Menu, ttk
from tkinter import messagebox, font
import os
import basicTechniques
import intermediateTechniques
import advancedTechniques

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

notSelectedLabel = ttk.Label(mainApplication,text='Please Select Cryptographs from the above menu')
notSelectedLabel.pack(padx=30,pady=30)

## Creating Required Functions 

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

def underConstruction(root):
    underConstructionLabel = ttk.Label(root,text='This Feature is Under Construction!!!')
    underConstructionLabel.pack(padx=30,pady=30)

## Basic Cryptographs
# Reverse Cipher
def reverseCipher(event=None):
    removeChildrens(mainApplication)
    def encrypt():
        messageLabel = ttk.Label(reverseCipherFrame,text='Encrypted Text : ')
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


## Ceaser Cipher
def ceaserCipher(event = None):
    removeChildrens(mainApplication)
    def encrypt():
        messageLabel = ttk.Label(ceaserCipherFrame,text='Encrypted Message :')
        message =  basicTechniques.ceaserCipherEncrypt(messageInput.get(),int(keyInput.get()))
        messageElement = tk.Text(ceaserCipherFrame,height=3,width=50)
        messageElement.config(state="normal")
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)

    def decrypt():
        messageLabel = ttk.Label(ceaserCipherFrame,text='Decrypted Message :')
        message =  basicTechniques.ceaserCipherDecrypt(messageInput.get(),int(keyInput.get()))
        messageElement = tk.Text(ceaserCipherFrame,height=3,width=50)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)


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

    # Encrypt and Decrypt Buttons
    encryptButton = ttk.Button(ceaserCipherFrame,text='Encrypt',command=encrypt) 
    decryptButton = ttk.Button(ceaserCipherFrame,text='Decrypt',command=decrypt) 
    encryptButton.grid(row=2,column=0,padx=30,pady=30)
    decryptButton.grid(row=2,column=1,padx=30,pady=30)

## Transposition Cipher
def transpositionCipher(event = None):
    removeChildrens(mainApplication)
    # Encrypting Functionality 
    def encrypt():
        messageLabel = ttk.Label(transpositionCipherFrame,text='Encrypted Text : ')
        message = basicTechniques.transpositionCipherEncrypt(messageInput.get(),int(keyInput.get()))
        messageElement = tk.Text(transpositionCipherFrame,height=3,width=50)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
    # Decryption Functionality
    def decrypt():
        messageLabel = ttk.Label(transpositionCipherFrame,text='Decrypted Text : ')
        message = basicTechniques.transpositionCipherDecrypt(messageInput.get(),int(keyInput.get()))
        messageElement = tk.Text(transpositionCipherFrame,height=3,width=50)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')

        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
    
    ## GUI
    # Creating Transposition Cipher Label Frame
    transpositionCipherFrame = tk.LabelFrame(mainApplication,text='Transposition Cipher')
    transpositionCipherFrame.pack(padx=20,pady=20)

    # Creating Form Handling User Input
    message = ttk.Label(transpositionCipherFrame,text='Message to encrypt/Decrypt : ')
    message.grid(row=0,column=0,padx=30,pady=45)
    messageInput = ttk.Entry(transpositionCipherFrame,width = 50)
    messageInput.grid(row=0,column=1,padx=30,pady=45)

    key = ttk.Label(transpositionCipherFrame,text='Key : ')
    key.grid(row=1,column=0,padx=30,pady=5)
    keyInput = ttk.Entry(transpositionCipherFrame,width=50)
    keyInput.grid(row=1,column=1,padx=30,pady=5)
    
    # Encrypt and Decrypt Button
    encryptButton = tk.Button(transpositionCipherFrame,text='Encrypt',command=encrypt)
    decryptButton = tk.Button(transpositionCipherFrame,text='Decrypt',command=decrypt)
    encryptButton.grid(row=2,column=0,padx=30,pady=30)
    decryptButton.grid(row=2,column=1,padx=30,pady=30)

## Multiplicative Cipher 

def multiplicativeCipher(event=None):
    removeChildrens(mainApplication)
    def encrypt():
        # Creating Widgets
        messageLabel = tk.Label(multiplicativeCipherFrame,text='Encrypted text : ')
        message = basicTechniques.multiplicativeCipherEncrypt(messageInput.get(),int(keyInput.get()))
        messageText = tk.Text(multiplicativeCipherFrame,width=50,height=3)
        messageText.config(state='normal')
        messageText.insert(tk.END,message)
        messageText.config(state='disabled')

        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageText.grid(row=3,column=1,padx=30,pady=30)

    def decrypt():
        messageLabel = tk.Label(multiplicativeCipherFrame,text='Decrypted text : ')
        message = basicTechniques.multiplicativeCipherDecrypt(messageInput.get(),int(keyInput.get()))
        messageText = tk.Text(multiplicativeCipherFrame,width=50,height=3)
        messageText.config(state='normal')
        messageText.insert(tk.END,message)
        messageText.config(state='disabled')

        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageText.grid(row=3,column=1,padx=30,pady=30)

    
    ## GUI
    # Creating Label Frame for multiplicative cipher
    multiplicativeCipherFrame = ttk.LabelFrame(mainApplication,text='Multiplicative Cipher')
    multiplicativeCipherFrame.pack(padx=20,pady=20)

    # Creating form and handling user input
    messageLabel = tk.Label(multiplicativeCipherFrame,text='Message to encrypt/decrypt : ')
    messageInput = ttk.Entry(multiplicativeCipherFrame,width=50)
    messageLabel.grid(row=0,column=0,padx=30,pady=45)
    messageInput.grid(row=0,column=1,padx=30,pady=45)

    keyLabel = tk.Label(multiplicativeCipherFrame,text='Key : ')
    keyInput = ttk.Entry(multiplicativeCipherFrame,width=50)
    keyLabel.grid(row=1,column=0,padx=30,pady=5)
    keyInput.grid(row=1,column=1,padx=30,pady=5)
    
    # Creating encrypt and decrypt buttons
    encryptButton = ttk.Button(multiplicativeCipherFrame,text='Encrypt',command=encrypt)
    decryptButton = ttk.Button(multiplicativeCipherFrame,text='Decrypt',command=decrypt)
    encryptButton.grid(row=2,column=0,padx=30,pady=30)
    decryptButton.grid(row=2,column=1,padx=30,pady=30)
    

## Affine Cipher
def affineCipher(event = None):
    removeChildrens(mainApplication)
    def encrypt():
        # Creating Widgets
        messageLabel = tk.Label(affineCipherFrame,text='Encrypted text : ')
        message = basicTechniques.affineCipherEncrypt(messageInput.get(),[int(keyOneInput.get()),int(keyTwoInput.get())])
        messageText = tk.Text(affineCipherFrame,width=50,height=3)
        messageText.config(state='normal')
        messageText.insert(tk.END,message)
        messageText.config(state='disabled')

        # Positioning Widgets
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageText.grid(row=4,column=1,padx=30,pady=30)

    def decrypt():
        messageLabel = tk.Label(affineCipherFrame,text='Decrypted text : ')
        message = basicTechniques.affineCipherDecrypt(messageInput.get(),[int(keyOneInput.get()),int(keyTwoInput.get())])
        messageText = tk.Text(affineCipherFrame,width=50,height=3)
        messageText.config(state='normal')
        messageText.insert(tk.END,message)
        messageText.config(state='disabled')

        # Positioning Widgets
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageText.grid(row=4,column=1,padx=30,pady=30)

    
    ## GUI
    # Creating Label Frame for multiplicative cipher
    affineCipherFrame = ttk.LabelFrame(mainApplication,text='Multiplicative Cipher')
    affineCipherFrame.pack(padx=20,pady=20)

    # Creating form and handling user input
    messageLabel = tk.Label(affineCipherFrame,text='Message to encrypt/decrypt : ')
    messageInput = ttk.Entry(affineCipherFrame,width=50)
    messageLabel.grid(row=0,column=0,padx=30,pady=45)
    messageInput.grid(row=0,column=1,padx=30,pady=45)

    keyOneLabel = tk.Label(affineCipherFrame,text='Key 1 : ')
    keyOneInput = ttk.Entry(affineCipherFrame,width=50)
    keyOneLabel.grid(row=1,column=0,padx=30,pady=5)
    keyOneInput.grid(row=1,column=1,padx=30,pady=5)
    
    keyTwoLabel = tk.Label(affineCipherFrame,text='Key 2 : ')
    keyTwoInput = ttk.Entry(affineCipherFrame,width=50)
    keyTwoLabel.grid(row=2,column=0,padx=30,pady=5)
    keyTwoInput.grid(row=2,column=1,padx=30,pady=5)
    
    # Creating encrypt and decrypt buttons
    encryptButton = ttk.Button(affineCipherFrame,text='Encrypt',command=encrypt)
    decryptButton = ttk.Button(affineCipherFrame,text='Decrypt',command=decrypt)
    encryptButton.grid(row=3,column=0,padx=30,pady=30)
    decryptButton.grid(row=3,column=1,padx=30,pady=30)

## Substitution Cipher
def substitutionCipher(event= None):
    removeChildrens(mainApplication)
    underConstruction(mainApplication)

### Intermediate Ciphers

## Vernam Cipher
def vernamCipher(event=None):
    removeChildrens(mainApplication)
    underConstruction(mainApplication)

## Vignere Cipher
def vignereCipher(event=None):
    removeChildrens(mainApplication)
    underConstruction(mainApplication)

## Base64
def base64(event=None):
    removeChildrens(mainApplication)
    underConstruction(mainApplication)

## MD5 and SHA
def md5sha(event=None):
    removeChildrens(mainApplication)
    underConstruction(mainApplication)

### Advanced Encryption 

## XOR Type
def xorType(event=None):
    removeChildrens(mainApplication)
    underConstruction(mainApplication)

## RSA
def rsa(event=None):
    removeChildrens(mainApplication)
    underConstruction(mainApplication)

## Creating the main menu
mainMenu = tk.Menu()

# Creating menu tabs
basicCryptographs = tk.Menu(mainMenu,tearoff=False)
intermediateCryptographs = tk.Menu(mainMenu,tearoff=False)
advancedCryptographs = tk.Menu(mainMenu,tearoff=False)

# Adding menu items to basic menu
basicCryptographs.add_command(label='Revere Cipher',command=reverseCipher)
basicCryptographs.add_command(label='Ceaser Cipher',command=ceaserCipher)
basicCryptographs.add_command(label='Transposition Cipher',command=transpositionCipher)
basicCryptographs.add_command(label='Multiplicative Cipher',command=multiplicativeCipher)
basicCryptographs.add_command(label='Affine Cipher',command=affineCipher)
basicCryptographs.add_command(label='Substitution Cipher',command=substitutionCipher)

# Addin menu items to intermediate menu
intermediateCryptographs.add_command(label='Vernam Cipher',command=vernamCipher)
intermediateCryptographs.add_command(label='Vignere Cipher',command=vignereCipher)
intermediateCryptographs.add_command(label='Base64',command=base64)
intermediateCryptographs.add_command(label='MD5 and SHA Hashes',command=md5sha)

# Adding menu items to advanced menu
advancedCryptographs.add_command(label='XOR Type',command=xorType)
advancedCryptographs.add_command(label='RSA',command=rsa)

# cascading menu tabs
mainMenu.add_cascade(label='Basic',menu=basicCryptographs)
mainMenu.add_cascade(label='Intermediate',menu = intermediateCryptographs)
mainMenu.add_cascade(label='Advanced',menu=advancedCryptographs)


## Creating requited buttons

mainApplication.config(menu=mainMenu)
mainApplication.mainloop()