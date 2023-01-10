# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(708, 599)
        self.animateButton = QtGui.QPushButton(Form)
        self.animateButton.setGeometry(QtCore.QRect(170, 570, 75, 23))
        self.animateButton.setObjectName(_fromUtf8("animateButton"))
        self.tickButton = QtGui.QPushButton(Form)
        self.tickButton.setGeometry(QtCore.QRect(260, 570, 75, 23))
        self.tickButton.setObjectName(_fromUtf8("tickButton"))
        self.stopButton = QtGui.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(350, 570, 75, 23))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.inputNum1 = QtGui.QPlainTextEdit(Form)
        self.inputNum1.setGeometry(QtCore.QRect(570, 110, 104, 31))
        self.inputNum1.setObjectName(_fromUtf8("inputNum1"))
        self.inputNum2 = QtGui.QPlainTextEdit(Form)
        self.inputNum2.setGeometry(QtCore.QRect(580, 170, 104, 31))
        self.inputNum2.setObjectName(_fromUtf8("inputNum2"))
        self.addButton = QtGui.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(590, 230, 75, 23))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.outputSum = QtGui.QTextBrowser(Form)
        self.outputSum.setGeometry(QtCore.QRect(570, 300, 121, 31))
        self.outputSum.setObjectName(_fromUtf8("outputSum"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 521, 541))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.animateButton.raise_()
        self.tickButton.raise_()
        self.stopButton.raise_()
        self.inputNum1.raise_()
        self.inputNum2.raise_()
        self.addButton.raise_()
        self.outputSum.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.animateButton.setText(_translate("Form", "Animate", None))
        self.tickButton.setText(_translate("Form", "Tick", None))
        self.stopButton.setText(_translate("Form", "Stop", None))
        self.addButton.setText(_translate("Form", "Add", None))

