# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'letterofcancellation.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import datetime 


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

class DialogCancellation(object):
    def setupUi(self, DialogCancellation):
        DialogCancellation.setObjectName(_fromUtf8("DialogCancellation"))
        DialogCancellation.resize(621, 601)
        self.label = QtGui.QLabel(DialogCancellation)
        self.label.setGeometry(QtCore.QRect(60, 40, 221, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.dateEditCancellation = QtGui.QDateEdit(DialogCancellation)
        self.dateEditCancellation.setGeometry(QtCore.QRect(340, 40, 121, 21))
        self.dateEditCancellation.setObjectName(_fromUtf8("dateEditCancellation"))
        self.dateEditCancellation.setDate(QtCore.QDate(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day))
        self.textEditCancellationLetter = QtGui.QTextEdit(DialogCancellation)
        self.textEditCancellationLetter.setGeometry(QtCore.QRect(30, 110, 561, 421))
        self.textEditCancellationLetter.setObjectName(_fromUtf8("textEditCancellationLetter"))

        self.retranslateUi(DialogCancellation)
        QtCore.QMetaObject.connectSlotsByName(DialogCancellation)

    def retranslateUi(self, DialogCancellation):
        DialogCancellation.setWindowTitle(_translate("DialogCancellation", "DialogCancellation", None))
        self.label.setText(_translate("DialogCancellation", "Cancellation Date:", None))

