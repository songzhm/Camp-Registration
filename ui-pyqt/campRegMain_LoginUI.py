# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'campRegMain_Login.ui'
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

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.resize(993, 651)
        self.centralwidget = QtGui.QWidget(LoginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 90, 471, 151))
        self.label.setStyleSheet(_fromUtf8("font: 75 20pt \"Kristen ITC\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBoxList = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxList.setGeometry(QtCore.QRect(220, 270, 501, 301))
        self.groupBoxList.setTitle(_fromUtf8(""))
        self.groupBoxList.setObjectName(_fromUtf8("groupBoxList"))
        self.radioButtonDirector = QtGui.QRadioButton(self.groupBoxList)
        self.radioButtonDirector.setGeometry(QtCore.QRect(140, 50, 211, 41))
        self.radioButtonDirector.setObjectName(_fromUtf8("radioButtonDirector"))
        self.radioButtonRegClerk = QtGui.QRadioButton(self.groupBoxList)
        self.radioButtonRegClerk.setGeometry(QtCore.QRect(140, 90, 211, 41))
        self.radioButtonRegClerk.setObjectName(_fromUtf8("radioButtonRegClerk"))
        self.lineEditAccessCode = QtGui.QLineEdit(self.groupBoxList)
        self.lineEditAccessCode.setGeometry(QtCore.QRect(140, 180, 221, 21))
        self.lineEditAccessCode.setObjectName(_fromUtf8("lineEditAccessCode"))
        self.labelAccessCode = QtGui.QLabel(self.groupBoxList)
        self.labelAccessCode.setGeometry(QtCore.QRect(140, 140, 221, 16))
        self.labelAccessCode.setObjectName(_fromUtf8("labelAccessCode"))
        self.pushButtonLogin = QtGui.QPushButton(self.groupBoxList)
        self.pushButtonLogin.setGeometry(QtCore.QRect(200, 250, 101, 23))
        self.pushButtonLogin.setObjectName(_fromUtf8("pushButtonLogin"))
        self.labelLogin = QtGui.QLabel(self.groupBoxList)
        self.labelLogin.setGeometry(QtCore.QRect(120, 210, 281, 23))
        self.labelLogin.setText(_fromUtf8(""))
        self.labelLogin.setObjectName(_fromUtf8("labelLogin"))
        self.frameCheckList = QtGui.QFrame(self.centralwidget)
        self.frameCheckList.setGeometry(QtCore.QRect(280, 270, 391, 281))
        self.frameCheckList.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameCheckList.setFrameShadow(QtGui.QFrame.Raised)
        self.frameCheckList.setObjectName(_fromUtf8("frameCheckList"))
        self.textEditCheckList = QtGui.QTextEdit(self.frameCheckList)
        self.textEditCheckList.setGeometry(QtCore.QRect(10, 10, 361, 221))
        self.textEditCheckList.setObjectName(_fromUtf8("textEditCheckList"))
        self.pushButtonCheckList = QtGui.QPushButton(self.frameCheckList)
        self.pushButtonCheckList.setGeometry(QtCore.QRect(160, 240, 75, 23))
        self.pushButtonCheckList.setObjectName(_fromUtf8("pushButtonCheckList"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(290, 240, 351, 211))
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
        self.dateEditCamp2Start = QtGui.QDateEdit(self.frame)
        self.dateEditCamp2Start.setObjectName(_fromUtf8("dateEditCamp2Start"))
        self.gridLayout.addWidget(self.dateEditCamp2Start, 3, 1, 1, 1)
        self.dateEditCampStart = QtGui.QDateEdit(self.frame)
        self.dateEditCampStart.setObjectName(_fromUtf8("dateEditCampStart"))
        self.gridLayout.addWidget(self.dateEditCampStart, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.dateEditCamp3End = QtGui.QDateEdit(self.frame)
        self.dateEditCamp3End.setObjectName(_fromUtf8("dateEditCamp3End"))
        self.gridLayout.addWidget(self.dateEditCamp3End, 4, 2, 1, 1)
        self.dateEditCamp2End = QtGui.QDateEdit(self.frame)
        self.dateEditCamp2End.setObjectName(_fromUtf8("dateEditCamp2End"))
        self.gridLayout.addWidget(self.dateEditCamp2End, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.dateEditCamp3Start = QtGui.QDateEdit(self.frame)
        self.dateEditCamp3Start.setObjectName(_fromUtf8("dateEditCamp3Start"))
        self.gridLayout.addWidget(self.dateEditCamp3Start, 4, 1, 1, 1)
        self.dateEditCamp1End = QtGui.QDateEdit(self.frame)
        self.dateEditCamp1End.setObjectName(_fromUtf8("dateEditCamp1End"))
        self.gridLayout.addWidget(self.dateEditCamp1End, 1, 2, 1, 1)
        self.pushButtonCampDates = QtGui.QPushButton(self.frame)
        self.pushButtonCampDates.setObjectName(_fromUtf8("pushButtonCampDates"))
        self.gridLayout.addWidget(self.pushButtonCampDates, 5, 1, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(LoginWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LoginWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(LoginWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 993, 36))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuApplicant = QtGui.QMenu(self.menuBar)
        self.menuApplicant.setObjectName(_fromUtf8("menuApplicant"))
        self.menuSetting = QtGui.QMenu(self.menuBar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        LoginWindow.setMenuBar(self.menuBar)
        self.actionAdd_New = QtGui.QAction(LoginWindow)
        self.actionAdd_New.setObjectName(_fromUtf8("actionAdd_New"))
        self.actionLook_Up = QtGui.QAction(LoginWindow)
        self.actionLook_Up.setObjectName(_fromUtf8("actionLook_Up"))
        self.actionAdd_New_Applicant = QtGui.QAction(LoginWindow)
        self.actionAdd_New_Applicant.setObjectName(_fromUtf8("actionAdd_New_Applicant"))
        self.actionLook_Up_2 = QtGui.QAction(LoginWindow)
        self.actionLook_Up_2.setObjectName(_fromUtf8("actionLook_Up_2"))
        self.actionChange_Camp_Dates = QtGui.QAction(LoginWindow)
        self.actionChange_Camp_Dates.setObjectName(_fromUtf8("actionChange_Camp_Dates"))
        self.actionChange_Content_of_Checklist = QtGui.QAction(LoginWindow)
        self.actionChange_Content_of_Checklist.setObjectName(_fromUtf8("actionChange_Content_of_Checklist"))
        self.menuApplicant.addAction(self.actionAdd_New_Applicant)
        self.menuApplicant.addAction(self.actionLook_Up_2)
        self.menuSetting.addAction(self.actionChange_Camp_Dates)
        self.menuSetting.addAction(self.actionChange_Content_of_Checklist)
        self.menuBar.addAction(self.menuApplicant.menuAction())
        self.menuBar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login", None))
        self.label.setText(_translate("LoginWindow", "Gila Breath Camp", None))
        self.radioButtonDirector.setText(_translate("LoginWindow", "Director", None))
        self.radioButtonRegClerk.setText(_translate("LoginWindow", "Registration Clerk", None))
        self.labelAccessCode.setText(_translate("LoginWindow", "Access Code:", None))
        self.pushButtonLogin.setText(_translate("LoginWindow", "Login", None))
        self.pushButtonCheckList.setText(_translate("LoginWindow", "Submit", None))
        self.label_4.setText(_translate("LoginWindow", "Camp 1", None))
        self.label_3.setText(_translate("LoginWindow", "Camp 1", None))
        self.label_2.setText(_translate("LoginWindow", "Camp 1", None))
        self.label_6.setText(_translate("LoginWindow", "End Date", None))
        self.label_5.setText(_translate("LoginWindow", "Start Date", None))
        self.pushButtonCampDates.setText(_translate("LoginWindow", "Submit", None))
        self.menuApplicant.setTitle(_translate("LoginWindow", "Applicant", None))
        self.menuSetting.setTitle(_translate("LoginWindow", "Setting", None))
        self.actionAdd_New.setText(_translate("LoginWindow", "Add New Applicant", None))
        self.actionLook_Up.setText(_translate("LoginWindow", "Look Up", None))
        self.actionAdd_New_Applicant.setText(_translate("LoginWindow", "Add New Applicant", None))
        self.actionLook_Up_2.setText(_translate("LoginWindow", "Look Up", None))
        self.actionChange_Camp_Dates.setText(_translate("LoginWindow", "Change Camp Dates", None))
        self.actionChange_Content_of_Checklist.setText(_translate("LoginWindow", "Change Content of Checklist", None))

