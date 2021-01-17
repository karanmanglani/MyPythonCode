import tkinter as tk
from tkinter import ttk
import os
import pyperclip
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

# Program for under construction parts
def underConstruction(root):
    removeChildrens(mainApplication)
    c = tk.Canvas(mainApplication, height="700", width="1200")
    fnt = ('Times', 25 , 'bold italic underline')
    text = c.create_text(500,100, text="Under construction please select other technique from the menu", font = fnt, fill="red", activefill="green")
    c.pack()

## Asking user to select a technique
removeChildrens(mainApplication)
c = tk.Canvas(mainApplication, height="700", width="1200")
fnt = ('Times', 40 , 'bold italic underline')
text = c.create_text(500,100, text="Please select technique from the menu", font = fnt, fill="red", activefill="green")
c.pack()

## Basic Cryptographs
# Reverse Cipher
def reverseCipher(event=None):
    removeChildrens(mainApplication)
    def encrypt(event=None):
        # Creating Widgets
        messageLabel = ttk.Label(reverseCipherFrame,text='Encrypted Text : ')
        message =  basicTechniques.reverseCipher(messageInput.get())
        messageElement = tk.Text(reverseCipherFrame,height=3,width=50)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(reverseCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))
        
        # Positioning Widgets
        messageLabel.grid(row=2,column=0,padx=30,pady=30)
        messageElement.grid(row=2,column=1,padx=30,pady=30)  
        copyButton.grid(row=3,column=0,padx=30,pady=30)  

        

    def decrypt():
        # Creating Widgets
        messageLabel = ttk.Label(reverseCipherFrame,text='Decrypted Text : ')
        message =  basicTechniques.reverseCipher(messageInput.get())
        messageElement = tk.Text(reverseCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(reverseCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))
        
        # Positioning Widgets
        messageLabel.grid(row=2,column=0,padx=30,pady=30)
        messageElement.grid(row=2,column=1,padx=30,pady=30)
        copyButton.grid(row=3,column=0,padx=30,pady=30) 

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

    # Binding Shortcut Key
    reverseCipherFrame.bind('<enter>',encrypt)


## Ceaser Cipher
def ceaserCipher(event = None):
    removeChildrens(mainApplication)
    def encrypt():
        # Creating Widgets
        messageLabel = ttk.Label(ceaserCipherFrame,text='Encrypted Message :')
        message =  basicTechniques.ceaserCipherEncrypt(messageInput.get(),int(keyInput.get()))
        messageElement = tk.Text(ceaserCipherFrame,height=3,width=50)
        messageElement.config(state="normal")
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(ceaserCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))
       
        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30) 

    def decrypt():
        # Creating Widgets
        messageLabel = ttk.Label(ceaserCipherFrame,text='Decrypted Message :')
        message =  basicTechniques.ceaserCipherDecrypt(messageInput.get(),int(keyInput.get()))
        messageElement = tk.Text(ceaserCipherFrame,height=3,width=50)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(ceaserCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))
        
        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30) 


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
        # Creating Widgets
        messageLabel = ttk.Label(transpositionCipherFrame,text='Encrypted Text : ')
        message = basicTechniques.transpositionCipherEncrypt(messageInput.get(),int(keyInput.get()))
        messageElement = tk.Text(transpositionCipherFrame,height=3,width=50)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(transpositionCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))
        
        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30) 
    # Decryption Functionality
    def decrypt():
        # Creating Widgets
        messageLabel = ttk.Label(transpositionCipherFrame,text='Decrypted Text : ')
        message = basicTechniques.transpositionCipherDecrypt(messageInput.get(),int(keyInput.get()))
        messageElement = tk.Text(transpositionCipherFrame,height=3,width=50)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(transpositionCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30) 
    
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
        copyButton = tk.Button(multiplicativeCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageText.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30) 

    def decrypt():
        messageLabel = tk.Label(multiplicativeCipherFrame,text='Decrypted text : ')
        message = basicTechniques.multiplicativeCipherDecrypt(messageInput.get(),int(keyInput.get()))
        messageText = tk.Text(multiplicativeCipherFrame,width=50,height=3)
        messageText.config(state='normal')
        messageText.insert(tk.END,message)
        messageText.config(state='disabled')
        copyButton = tk.Button(multiplicativeCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageText.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30) 

    
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
        copyButton = tk.Button(affineCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageText.grid(row=4,column=1,padx=30,pady=30)
        copyButton.grid(row=5,column=0,padx=30,pady=30) 

    def decrypt():
        messageLabel = tk.Label(affineCipherFrame,text='Decrypted text : ')
        message = basicTechniques.affineCipherDecrypt(messageInput.get(),[int(keyOneInput.get()),int(keyTwoInput.get())])
        messageText = tk.Text(affineCipherFrame,width=50,height=3)
        messageText.config(state='normal')
        messageText.insert(tk.END,message)
        messageText.config(state='disabled')
        copyButton = tk.Button(affineCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageText.grid(row=4,column=1,padx=30,pady=30)
        copyButton.grid(row=5,column=0,padx=30,pady=30) 

    
    ## GUI
    # Creating Label Frame for multiplicative cipher
    affineCipherFrame = ttk.LabelFrame(mainApplication,text='Affine Cipher')
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
    def encrypt():
        # Creating Widgets
        messageLabel = tk.Label(substitutionCipherFrame,text='Encrypted Message : ')
        message = basicTechniques.substitutionCipherEncrypt(lettersInput.get(),keyInput.get(),messageInput.get())
        messageElement = tk.Text(substitutionCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(substitutionCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageElement.grid(row=4,column=1,padx=30,pady=30)
        copyButton.grid(row=5,column=0,padx=30,pady=30) 

    def decrypt():
        # Creating Widgets
        messageLabel = tk.Label(substitutionCipherFrame,text='Decrypted Message : ')
        message = basicTechniques.substitutionCipherDecrypt(lettersInput.get(),keyInput.get(),messageInput.get())
        messageElement = tk.Text(substitutionCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(substitutionCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageElement.grid(row=4,column=1,padx=30,pady=30)
        copyButton.grid(row=5,column=0,padx=30,pady=30) 
    
    ## GUI
    # Creating Label Frame
    substitutionCipherFrame = tk.LabelFrame(mainApplication,text='Substitution Cipher')
    substitutionCipherFrame.pack(pady=20)

    # Creating Form for handling user input
    messageLabel = tk.Label(substitutionCipherFrame,text='Message to Encrypt/Decrypt : ')
    messageInput = tk.Entry(substitutionCipherFrame,width=50)
    messageLabel.grid(row=0,column=0,padx=30,pady=45)
    messageInput.grid(row=0,column=1,padx=30,pady=45)

    lettersLabel = tk.Label(substitutionCipherFrame,text='Letters to be replaced : ')
    lettersInput = tk.Entry(substitutionCipherFrame,width=50)
    lettersLabel.grid(row=1,column=0,padx=30,pady=5)
    lettersInput.grid(row=1,column=1,padx=30,pady=5)

    keyLabel = tk.Label(substitutionCipherFrame,text='Key for replacing letters(string) : ')
    keyInput = tk.Entry(substitutionCipherFrame,width=50)
    keyLabel.grid(row=2,column=0,padx=30,pady=45)
    keyInput.grid(row=2,column=1,padx=30,pady=45)

    # Creating Encrypt and Decrypt Buttons
    encryptButton = tk.Button(substitutionCipherFrame,text='Encrypt',command=encrypt)
    decryptButton = tk.Button(substitutionCipherFrame,text='Decrypt',command=decrypt)
    encryptButton.grid(row=3,column=0,padx=30,pady=5)
    decryptButton.grid(row=3,column=1,padx=30,pady=5)

### Intermediate Ciphers

## Vernam Cipher
def vernamCipher(event=None):
    removeChildrens(mainApplication)
    def encrypt():
        # Creating Widgets
        messageLabel = tk.Label(vernamCipherFrame,text='Encrypted Message : ')
        message = intermediateTechniques.vernamCipherEncrypt(messageInput.get(),keyInput.get())
        messageElement = tk.Text(vernamCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(vernamCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30)
    def decrypt():
        # Creating Widgets
        messageLabel = tk.Label(vernamCipherFrame,text='Encrypted Message : ')
        message = intermediateTechniques.vernamCipherDecrypt(messageInput.get(),keyInput.get())
        messageElement = tk.Text(vernamCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(vernamCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30)
    
    ### Creating GUI for the vernam cipher
    ## Creating Label Frame for the vernam cipher
    vernamCipherFrame = tk.LabelFrame(mainApplication,text='Vernam Cipher')
    vernamCipherFrame.pack(pady=20)
    
    ### Creating form for handling user input
    messageLabel = tk.Label(vernamCipherFrame,text='Message to Encrypt/Decrypt : ')
    messageInput = tk.Entry(vernamCipherFrame,width=50)
    messageLabel.grid(row=0,column=0,padx=30,pady=45)
    messageInput.grid(row=0,column=1,padx=30,pady=45)

    keyLabel = tk.Label(vernamCipherFrame,text='Key(string) : ')
    keyInput = tk.Entry(vernamCipherFrame,width=50)
    keyLabel.grid(row=1,column=0,padx=30,pady=5)
    keyInput.grid(row=1,column=1,padx=30,pady=5)

    # Creating Encrypt and Decrypt Buttons
    encryptButton = tk.Button(vernamCipherFrame,text='Encrypt',command=encrypt)
    decryptButton = tk.Button(vernamCipherFrame,text='Decrypt',command=decrypt)
    encryptButton.grid(row=2,column=0,padx=30,pady=5)
    decryptButton.grid(row=2,column=1,padx=30,pady=5)
    

## Vignere Cipher
def vignereCipher(event=None):
    removeChildrens(mainApplication)
    def encrypt():
        # Creating Widgets
        messageLabel = tk.Label(vignereCipherFrame,text='Encrypted Message : ')
        message = intermediateTechniques.vignereCipherEncrypt(messageInput.get(),keyInput.get())
        messageElement = tk.Text(vignereCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(vignereCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30)
    def decrypt():
        # Creating Widgets
        messageLabel = tk.Label(vignereCipherFrame,text='Encrypted Message : ')
        message = intermediateTechniques.vernamCipherDecrypt(messageInput.get(),keyInput.get())
        messageElement = tk.Text(vignereCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(vignereCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=3,column=0,padx=30,pady=30)
        messageElement.grid(row=3,column=1,padx=30,pady=30)
        copyButton.grid(row=4,column=0,padx=30,pady=30)
    
    ### Creating GUI for the vernam cipher
    ## Creating Label Frame for the vernam cipher
    vignereCipherFrame = tk.LabelFrame(mainApplication,text='Vernam Cipher')
    vignereCipherFrame.pack(pady=20)
    
    ### Creating form for handling user input
    messageLabel = tk.Label(vignereCipherFrame,text='Message to Encrypt/Decrypt : ')
    messageInput = tk.Entry(vignereCipherFrame,width=50)
    messageLabel.grid(row=0,column=0,padx=30,pady=45)
    messageInput.grid(row=0,column=1,padx=30,pady=45)

    keyLabel = tk.Label(vignereCipherFrame,text='Key(string) : ')
    keyInput = tk.Entry(vignereCipherFrame,width=50)
    keyLabel.grid(row=1,column=0,padx=30,pady=5)
    keyInput.grid(row=1,column=1,padx=30,pady=5)

    # Creating Encrypt and Decrypt Buttons
    encryptButton = tk.Button(vignereCipherFrame,text='Encrypt',command=encrypt)
    decryptButton = tk.Button(vignereCipherFrame,text='Decrypt',command=decrypt)
    encryptButton.grid(row=2,column=0,padx=30,pady=5)
    decryptButton.grid(row=2,column=1,padx=30,pady=5)

## Playfair Cipher
def playfairCipher(event=None):
    removeChildrens(mainApplication)
    def encrypt():
        # Creating Widgets
        messageLabel = tk.Label(playfairCipherFrame,text='Encrypted Message : ')
        message = intermediateTechniques.playfairCipherEncrypt(keyInput.get(),messageInput.get(),alphabetToRemoveInput.get())
        messageElement = tk.Text(playfairCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(playfairCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageElement.grid(row=4,column=1,padx=30,pady=30)
        copyButton.grid(row=5,column=0,padx=30,pady=30)
    def decrypt():
        # Creating Widgets
        messageLabel = tk.Label(playfairCipherFrame,text='Encrypted Message : ')
        message = intermediateTechniques.playfairCipherDecrypt(keyInput.get(),messageInput.get(),alphabetToRemoveInput.get())
        messageElement = tk.Text(playfairCipherFrame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')
        copyButton = tk.Button(playfairCipherFrame,text='Copy',command=lambda:pyperclip.copy(message))

        # Positioning Widgets
        messageLabel.grid(row=4,column=0,padx=30,pady=30)
        messageElement.grid(row=4,column=1,padx=30,pady=30)
        copyButton.grid(row=5,column=0,padx=30,pady=30)
    
    ### Creating GUI for the vernam cipher
    ## Creating Label Frame for the vernam cipher
    playfairCipherFrame = tk.LabelFrame(mainApplication,text='Playfair Cipher(No spaces or x or j)')
    playfairCipherFrame.pack(pady=20)
    
    ### Creating form for handling user input
    messageLabel = tk.Label(playfairCipherFrame,text='Message to Encrypt/Decrypt : ')
    messageInput = tk.Entry(playfairCipherFrame,width=50)
    messageLabel.grid(row=0,column=0,padx=30,pady=45)
    messageInput.grid(row=0,column=1,padx=30,pady=45)

    keyLabel = tk.Label(playfairCipherFrame,text='Key(string) : ')
    keyInput = tk.Entry(playfairCipherFrame,width=50)
    keyLabel.grid(row=1,column=0,padx=30,pady=5)
    keyInput.grid(row=1,column=1,padx=30,pady=5)

    alphabetToRemoveLabel = tk.Label(playfairCipherFrame,text='AlphabetToRemove : ')
    alphabetToRemoveInput = tk.Entry(playfairCipherFrame,width=50)
    alphabetToRemoveLabel.grid(row=2,column=0,padx=30,pady=30)
    alphabetToRemoveInput.grid(row=2,column=1,padx=30,pady=30)

    # Creating Encrypt and Decrypt Buttons
    encryptButton = tk.Button(playfairCipherFrame,text='Encrypt',command=encrypt)
    decryptButton = tk.Button(playfairCipherFrame,text='Decrypt',command=decrypt)
    encryptButton.grid(row=3,column=0,padx=30,pady=5)
    decryptButton.grid(row=3,column=1,padx=30,pady=5)

## Base64
def base64(event=None):
    removeChildrens(mainApplication)
    def encode():
        messageLabel = tk.Label(base64Frame,text='Encrypted Message : ')
        message = intermediateTechniques.base64Encode(messageInput.get())
        messageElement = tk.Text(base64Frame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')

        # Positioning Widgets
        messageLabel.grid(row=2,column=0,padx=30,pady=30)
        messageElement.grid(row=2,column=1,padx=30,pady=30)
    def decode():
        messageLabel = tk.Label(base64Frame,text='Encrypted Message : ')
        message = intermediateTechniques.base64Decode(messageInput.get())
        messageElement = tk.Text(base64Frame,width=50,height=3)
        messageElement.config(state='normal')
        messageElement.insert(tk.END,message)
        messageElement.config(state='disabled')

        # Positioning Widgets
        messageLabel.grid(row=2,column=0,padx=30,pady=30)
        messageElement.grid(row=2,column=1,padx=30,pady=30)
    
    ### GUI 
    ## Creating Label Frame for base64 encoding
    base64Frame = ttk.LabelFrame(mainApplication,text='base64 Encoding and Decoding')
    base64Frame.pack(pady=20)

    ## Creating form for handling user input
    messageLabel = tk.Label(base64Frame,text='Message to Encrypt/Decrypt : ')
    messageInput = tk.Entry(base64Frame,width=50)
    messageLabel.grid(row=0,column=0,padx=30,pady=45)
    messageInput.grid(row=0,column=1,padx=30,pady=45)

    # Creating Encode and Decode Buttons
    encryptButton = tk.Button(base64Frame,text='Encode',command=encode)
    decryptButton = tk.Button(base64Frame,text='Decode',command=decode)
    encryptButton.grid(row=1,column=0,padx=30,pady=5)
    decryptButton.grid(row=1,column=1,padx=30,pady=5)



### Advanced Encryption 

## MD5
def md5(event=None):
    removeChildrens(mainApplication)
    def hasher():
        # Creating Widgets
        hashedText = advancedTechniques.md5Hasher(messageInput.get())
        hashLabel = tk.Label(md5Frame,text='Hashed Hexadecimal : ')
        hashElement = tk.Text(md5Frame,width=50,height=3)
        hashElement.config(state='normal')
        hashElement.insert(tk.END,hashedText)
        hashElement.config(state='disabled')
        copyButton = tk.Button(md5Frame,text='Copy',command=lambda:pyperclip.copy(hashedText))

        # Positioning Widgets
        hashLabel.grid(row=2,column=0,padx=30,pady=30)
        hashElement.grid(row=2,column=1,padx=30,pady=30)
        copyButton.grid(row=3,column=0,padx=30,pady=30)
    
    
    ## Creating GUI
    # Label Form for md5 hasher
    md5Frame = ttk.LabelFrame(mainApplication,text='MD5 Hasher')
    md5Frame.pack(pady=20)

    # Creating the form
    messageLabel = tk.Label(md5Frame,text='Message to hash: ')
    messageInput = tk.Entry(md5Frame,width=50)
    hashButton = tk.Button(md5Frame,text='Hash',command=hasher)

    # Positioning Widgets
    messageLabel.grid(row=0,column=0,padx=30,pady=30)
    messageInput.grid(row=0,column=1,padx=30,pady=30)
    hashButton.grid(row=1,column=0,padx=30,pady=30)



## SHA256
def sha256(event=None):
    removeChildrens(mainApplication)
    def hasher():
        # Creating Widgets
        hashedText = advancedTechniques.sha256Hasher(messageInput.get())
        hashLabel = tk.Label(sha256Frame,text='Hashed Hexadecimal : ')
        hashElement = tk.Text(sha256Frame,width=50,height=3)
        hashElement.config(state='normal')
        hashElement.insert(tk.END,hashedText)
        hashElement.config(state='disabled')
        copyButton = tk.Button(sha256Frame,text='Copy',command=lambda:pyperclip.copy(hashedText))

        # Positioning Widgets
        hashLabel.grid(row=2,column=0,padx=30,pady=30)
        hashElement.grid(row=2,column=1,padx=30,pady=30)
        copyButton.grid(row=3,column=0,padx=30,pady=30)
    
    
    ## Creating GUI
    # Label Form for md5 hasher
    sha256Frame = ttk.LabelFrame(mainApplication,text='SHA256 Hasher')
    sha256Frame.pack(pady=20)

    # Creating the form
    messageLabel = tk.Label(sha256Frame,text='Message to hash: ')
    messageInput = tk.Entry(sha256Frame,width=50)
    hashButton = tk.Button(sha256Frame,text='Hash',command=hasher)

    # Positioning Widgets
    messageLabel.grid(row=0,column=0,padx=30,pady=30)
    messageInput.grid(row=0,column=1,padx=30,pady=30)
    hashButton.grid(row=1,column=0,padx=30,pady=30)

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
intermediateCryptographs.add_command(label='Playfair Cipher',command=playfairCipher)
intermediateCryptographs.add_command(label='Base64',command=base64)


# Adding menu items to advanced menu
advancedCryptographs.add_command(label='MD5',command=md5)
advancedCryptographs.add_command(label='sha256',command=sha256)
#advancedCryptographs.add_command(label='RSA',command=rsa)

# cascading menu tabs
mainMenu.add_cascade(label='Basic',menu=basicCryptographs)
mainMenu.add_cascade(label='Intermediate',menu = intermediateCryptographs)
mainMenu.add_cascade(label='Advanced',menu=advancedCryptographs)


## Creating requited buttons
mainApplication.config(menu=mainMenu)
mainApplication.mainloop()