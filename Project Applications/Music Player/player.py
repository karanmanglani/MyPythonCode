from tkinter import *

mainApplication = Tk()
mainApplication.title('MP3 Player')
mainApplication.geometry('500x400')

# Create playlist box
playlistBox  = Listbox(mainApplication,bg = 'black',fg = "green", width=60)
playlistBox.pack(pady=20)

# Define button Images 
backImg = PhotoImage(file='images/back50.png')
forwardImg = PhotoImage(file='images/forward50.png')
playImg = PhotoImage(file='images/play50.png')
pauseImg = PhotoImage(file='images/pause50.png')
stopImg = PhotoImage(file='images/stop50.png')

# Create button frame
controlFrame = Frame()
controlFrame.pack(pady=20)

# Create buttons
backButton = Button(controlFrame,image=backImg,borderwidth=0) 
forwardButton = Button(controlFrame,image=forwardImg,borderwidth=0)
playButton =Button(controlFrame,image=playImg,borderwidth=0)
pauseButton =Button(controlFrame,image=pauseImg,borderwidth=0)
stopButton =Button(controlFrame,image=stopImg,borderwidth=0)

backButton.grid(row=0,column=0,padx=10)
forwardButton.grid(row=0,column=1,padx=10)
playButton.grid(row=0,column=2,padx=10)
pauseButton.grid(row=0,column=3,padx=10)
stopButton.grid(row=0,column=4,padx=10)

# Adding Menu
mainMenu = Menu(mainApplication)

## Creating dropdowns
# Add Song
addSongMenu = Menu(mainMenu,tearoff=False)
addSongMenu.add_cascade(label="Add Songs",menu=addSongMenu)


mainApplication.config(menu=mainMenu)
mainApplication.mainloop()