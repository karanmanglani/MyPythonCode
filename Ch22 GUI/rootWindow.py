from tkinter import *
from tkinter import font
root = Tk() # Creates the root window
root.title("GUI")
root.geometry("1300x800")
#root.wm_iconbitmap('1.ico') # To find latest way to add icons as this is not working
# listFonts = list(font.families())
# print(listFonts)


##################################### Canavas ###################################
c = Canvas(root, bg="blue", height="700", width="1200", cursor='pencil') # Creating canavas
id = c.create_line(50,50,200,50,200,150, width=4, fill = "white") # Line connecting 3 points A B C or connecting 2 lines AB and BC and with width and colour
id = c.create_oval(100,100,400,300, width=5, fill="yellow",outline = "red" , activefill = "green")# Create oval inside rectangle with diagnol A(x,y)B(z,v) activefill is hover 
id = c.create_polygon(10,10,200,200,300,200,width = 3, fill = "green", outline = "red", activefill = "yellow")
id = c.create_rectangle(500,200,700,600, width=2, fill = 'gray', outline = "black", activefill= "yellow")
fnt = ('Times', 40 , 'bold italic underline')
id = c.create_text(500,100, text="My Canavas", font = fnt, fill="yellow", activefill="green")





c.pack() #To show canavas

root.mainloop() # Shows the loop windows(Always type in end)