import gameoflife_class
import gui
from Tkinter import *
from PyQt4 import QtCore, QtGui

filename = str(raw_input("file Name? "))
g_initial = gameoflife_class.Grid(filename)

app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = gui.GameofLifeGUI(Form, g_initial)
Form.show()
sys.exit(app.exec_())

#root=Tk()
# sending the root to the class.
#b = gui.GameofLifeGUI(root,g_initial)
#root.mainloop()