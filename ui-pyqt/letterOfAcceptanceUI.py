# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'letterOfAcceptance.ui'
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

class Ui_DialogLetterOfAcceptance(object):
    def setupUi(self, DialogLetterOfAcceptance):
        DialogLetterOfAcceptance.setObjectName(_fromUtf8("DialogLetterOfAcceptance"))
        DialogLetterOfAcceptance.resize(443, 348)
        self.textBrowserLetterOfAcceptance = QtGui.QTextBrowser(DialogLetterOfAcceptance)
        self.textBrowserLetterOfAcceptance.setGeometry(QtCore.QRect(40, 20, 371, 271))
        self.textBrowserLetterOfAcceptance.setObjectName(_fromUtf8("textBrowserLetterOfAcceptance"))
        self.pushButtonOkay = QtGui.QPushButton(DialogLetterOfAcceptance)
        self.pushButtonOkay.setGeometry(QtCore.QRect(190, 310, 75, 23))
        self.pushButtonOkay.setObjectName(_fromUtf8("pushButtonOkay"))

        self.retranslateUi(DialogLetterOfAcceptance)
        QtCore.QMetaObject.connectSlotsByName(DialogLetterOfAcceptance)

    def retranslateUi(self, DialogLetterOfAcceptance):
        DialogLetterOfAcceptance.setWindowTitle(_translate("DialogLetterOfAcceptance", "Letter of Acceptance", None))
        self.pushButtonOkay.setText(_translate("DialogLetterOfAcceptance", "Okay", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogLetterOfAcceptance = QtGui.QDialog()
    ui = Ui_DialogLetterOfAcceptance()
    ui.setupUi(DialogLetterOfAcceptance)
    DialogLetterOfAcceptance.show()
    sys.exit(app.exec_())

