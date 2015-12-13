
# Imports #
from Tkinter import *
from Constants import *

# ========================================
# Class: Interface
#   This class is responsible for
# interacting with users. It encapsulates
# some tkinter widgets used to get input
# from users and give output to users.
# ========================================

class Interface:
    
    #. Constructor .#
    def __init__ (self, buttonCallBack):
        self.root = Tk()               # Create a Tk
        self.root.title(windowName)    # Rename the tk window
        #- Create widgets and layout them -#
        photo = PhotoImage(file=imageName)
        subwayGraph = Label(image=photo)
        subwayGraph.image = photo
        subwayGraph.grid(row=0, column=0, columnspan=3, sticky=W+E+N+S, padx=5, pady=5)
        Label(self.root, text=startEntryReminder).grid(row=1, column=0)
        Label(self.root, text=destEntryReminder).grid(row=2, column=0)
        self.startEntry = Entry(self.root)
        self.destEntry = Entry(self.root)
        self.startEntry.grid(row=1, column=1)
        self.destEntry.grid(row=2, column=1)
        searchButton = Button(self.root, text=searchButtonText, width=20, command=buttonCallBack)
        searchButton.grid(row=3, column=0, columnspan=2)
        Label(self.root, text=resultReminder).grid(row=1, column=2, sticky=W, padx=5)
        self.text = Text(self.root, width=40, height=5)
        self.text.grid(row=2, column=2, rowspan=2 ,padx=5, pady=5)

    #. Get value of entries .#
    def getStartEntry(self):
        return self.startEntry.get()
    def getDestEntry(self):
        return self.destEntry.get()

    #. Update the content of the text .#
    def updateText(self, newContent):
        self.text.delete(0.0, END)
        self.text.insert(INSERT, newContent)
