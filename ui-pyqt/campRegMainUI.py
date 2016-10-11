# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'campReg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from campRegAddNewApplicantUI import *
from campRegLookUpApplicantUI import *

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(830, 462)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 120, 471, 151))
        self.label.setStyleSheet(_fromUtf8("font: 75 20pt \"Kristen ITC\";"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 36))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_New = QtGui.QAction(MainWindow)
        self.actionAdd_New.setObjectName(_fromUtf8("actionAdd_New"))
        ## trigger add new
        self.actionAdd_New.triggered.connect(self.showNewApplicantDialog)
        self.actionLook_Up = QtGui.QAction(MainWindow)
        self.actionLook_Up.setObjectName(_fromUtf8("actionLook_Up"))
        ## trigger add look up
        self.actionLook_Up.triggered.connect(self.showLookUpApplicant)
        self.menuFile.addAction(self.actionAdd_New)
        self.menuFile.addAction(self.actionLook_Up)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Main", None))
        self.label.setText(_translate("MainWindow", "Gila Breath Camp", None))
        self.menuFile.setTitle(_translate("MainWindow", "Applicant", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionAdd_New.setText(_translate("MainWindow", "Add New Applicant", None))
        self.actionLook_Up.setText(_translate("MainWindow", "Look Up", None))

    def showNewApplicantDialog(self):
        self.DialogAddNewApplicant = QtGui.QDialog()
        ui = Ui_DialogAddNewApplicant()
        ui.setupUi(self.DialogAddNewApplicant)
        self.DialogAddNewApplicant.show()
    
    def showLookUpApplicant(self):
        self.DialogLookUpApplicant = QtGui.QDialog()
        ui = Ui_DialogLookUpApplicant()
        ui.setupUi(self.DialogLookUpApplicant)
        self.DialogLookUpApplicant.show()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

