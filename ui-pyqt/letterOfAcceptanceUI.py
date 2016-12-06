# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'letterofcancellation.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(621, 601)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 221, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.dateEditCancellation = QtGui.QDateEdit(Dialog)
        self.dateEditCancellation.setGeometry(QtCore.QRect(340, 40, 121, 21))
        self.dateEditCancellation.setObjectName(_fromUtf8("dateEditCancellation"))
        self.textEditCancellationLetter = QtGui.QTextEdit(Dialog)
        self.textEditCancellationLetter.setGeometry(QtCore.QRect(30, 110, 561, 421))
        self.textEditCancellationLetter.setObjectName(_fromUtf8("textEditCancellationLetter"))
        self.pushButtonSubmit = QtGui.QPushButton(Dialog)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(240, 550, 131, 40))
        self.pushButtonSubmit.setObjectName(_fromUtf8("pushButtonSubmit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Cancellation Date:", None))
        self.pushButtonSubmit.setText(_translate("Dialog", "Submit", None))

