# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'campRegMain_Director.ui'
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
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(270, 110, 261, 151))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateEdit_4 = QtGui.QDateEdit(self.frame)
        self.dateEdit_4.setObjectName(_fromUtf8("dateEdit_4"))
        self.gridLayout.addWidget(self.dateEdit_4, 3, 1, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.frame)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.dateEdit_6 = QtGui.QDateEdit(self.frame)
        self.dateEdit_6.setObjectName(_fromUtf8("dateEdit_6"))
        self.gridLayout.addWidget(self.dateEdit_6, 4, 2, 1, 1)
        self.dateEdit_3 = QtGui.QDateEdit(self.frame)
        self.dateEdit_3.setObjectName(_fromUtf8("dateEdit_3"))
        self.gridLayout.addWidget(self.dateEdit_3, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.dateEdit_5 = QtGui.QDateEdit(self.frame)
        self.dateEdit_5.setObjectName(_fromUtf8("dateEdit_5"))
        self.gridLayout.addWidget(self.dateEdit_5, 4, 1, 1, 1)
        self.dateEdit_2 = QtGui.QDateEdit(self.frame)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.gridLayout.addWidget(self.dateEdit_2, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(210, 70, 391, 281))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textEdit = QtGui.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 361, 221))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 240, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_New = QtGui.QAction(MainWindow)
        self.actionAdd_New.setObjectName(_fromUtf8("actionAdd_New"))
        self.actionLook_Up = QtGui.QAction(MainWindow)
        self.actionLook_Up.setObjectName(_fromUtf8("actionLook_Up"))
        self.actionChange_Number_of_Camps = QtGui.QAction(MainWindow)
        self.actionChange_Number_of_Camps.setObjectName(_fromUtf8("actionChange_Number_of_Camps"))
        self.actionChange_Content_of_Acceptance_Letter = QtGui.QAction(MainWindow)
        self.actionChange_Content_of_Acceptance_Letter.setObjectName(_fromUtf8("actionChange_Content_of_Acceptance_Letter"))
        self.actionChange_Content_of_Check_List = QtGui.QAction(MainWindow)
        self.actionChange_Content_of_Check_List.setObjectName(_fromUtf8("actionChange_Content_of_Check_List"))
        self.menuFile.addAction(self.actionAdd_New)
        self.menuFile.addAction(self.actionLook_Up)
        self.menuSetting.addAction(self.actionChange_Number_of_Camps)
        self.menuSetting.addAction(self.actionChange_Content_of_Acceptance_Letter)
        self.menuSetting.addAction(self.actionChange_Content_of_Check_List)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Main", None))
        self.label.setText(_translate("MainWindow", "Gila Breath Camp", None))
        self.label_4.setText(_translate("MainWindow", "Camp 1", None))
        self.label_3.setText(_translate("MainWindow", "Camp 1", None))
        self.label_2.setText(_translate("MainWindow", "Camp 1", None))
        self.label_6.setText(_translate("MainWindow", "End Date", None))
        self.label_5.setText(_translate("MainWindow", "Start Date", None))
        self.pushButton.setText(_translate("MainWindow", "Submit", None))
        self.pushButton_2.setText(_translate("MainWindow", "Submit", None))
        self.menuFile.setTitle(_translate("MainWindow", "Applicant", None))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting", None))
        self.actionAdd_New.setText(_translate("MainWindow", "Add New Applicant", None))
        self.actionLook_Up.setText(_translate("MainWindow", "Look Up", None))
        self.actionChange_Number_of_Camps.setText(_translate("MainWindow", "Change Camps Dates", None))
        self.actionChange_Content_of_Acceptance_Letter.setText(_translate("MainWindow", "Change Content of Acceptance Letter", None))
        self.actionChange_Content_of_Check_List.setText(_translate("MainWindow", "Change Content of Check List", None))

