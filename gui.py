from Tkinter import *
import gameoflife_class
import tkFont
from time import sleep
import mainwindow

class GameofLifeGUI(mainwindow.Ui_Form):

    def __init__(self, Form, grid):
        #self.master = master
        self.grid = grid
        self.setupUi(Form)
        self.textBrowser.setText(self.grid.stringGrid())
        self.animateButton.clicked.connect(self.refresh_GUI)
        self.addButton.clicked.connect(self.add)
        #self.pushButton_2.pack(side=LEFT)
        # quit .. breaks the mainloop
        #self.stopButton = Button(bottomframe, text="Stop", command=bottomframe.quit)

    def refresh_GUI(self, event=None):
        for i in range(1):
            self.textBrowser.clear()
            self.grid.generation_evolution()
            self.textBrowser.setText(self.grid.stringGrid())

    def add(self, event=None):
        sum = float(self.inputNum1.toPlainText())+float(self.inputNum2.toPlainText())
        self.outputSum.setText(str(sum))

def createFrame(self, master):
    topframe = Frame(master, width=700, height=700)
    topframe.pack()

    self.canvas = Canvas(topframe, width=700, height=700)
    self.canvas.pack()
    bottomframe = Frame(master, width=100, height=100)
    bottomframe.pack()
    # this makes a button and assigns it to a function
    self.startButton = Button(bottomframe, text="Start", command=self.refresh_GUI)
    self.startButton.pack(side=LEFT)
    # quit .. breaks the mainloop
    self.stopButton = Button(bottomframe, text="Stop", command=bottomframe.quit)
    self.stopButton.pack(side=LEFT)

    # self.label_1 = Label(master, text="Rows")
    # self.entry_1 = Entry(master)
    # self.entry_1.pack()
    # self.label_2 = Label(master, text="Columns")
    # self.label_1.pack()
    # self.label_2.pack()
    # self.entry_2 = Entry(master)
    # self.entry_2.pack()
    # if you need user input, you use entry

    # self.entry_2 = Entry(master)
    # E = east, grid is a matrix
    # self.label_1.grid(row=0, sticky=E)
    # self.label_2.grid(row=1, sticky=E)
    # self.entry_1.grid(row=0, column=1)
    # self.entry_2.grid(row=1, column=1)

    #  Creation of grid
    tempfont = tkFont.Font(family='Helvetica',
                           size=8, weight='bold')
    self.text = self.canvas.create_text(100, 350, anchor=W, font=tempfont,
                                        text=self.grid.stringGrid())


