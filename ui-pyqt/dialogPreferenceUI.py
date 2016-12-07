# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogPreference.ui'
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

class Ui_DialogPreference(object):
    def setupUi(self, DialogPreference):
        DialogPreference.setObjectName(_fromUtf8("DialogPreference"))
        DialogPreference.resize(733, 665)
        self.textBrowser = QtGui.QTextBrowser(DialogPreference)
        self.textBrowser.setGeometry(QtCore.QRect(80, 130, 221, 381))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(DialogPreference)
        self.textBrowser_2.setGeometry(QtCore.QRect(420, 130, 221, 381))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.label = QtGui.QLabel(DialogPreference)
        self.label.setGeometry(QtCore.QRect(80, 70, 221, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DialogPreference)
        self.label_2.setGeometry(QtCore.QRect(420, 70, 221, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(DialogPreference)
        self.pushButton.setGeometry(QtCore.QRect(290, 580, 131, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(DialogPreference)
        QtCore.QMetaObject.connectSlotsByName(DialogPreference)

    def retranslateUi(self, DialogPreference):
        DialogPreference.setWindowTitle(_translate("DialogPreference", "Preference", None))
        self.label.setText(_translate("DialogPreference", "Have to Stay with:", None))
        self.label_2.setText(_translate("DialogPreference", "Cannot Stay with:", None))
        self.pushButton.setText(_translate("DialogPreference", "Submit", None))

