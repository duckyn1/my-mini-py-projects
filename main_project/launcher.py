# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testlau.ui'

# Created by: PyQt5 UI code generator 5.15.11

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(280, 20, 151, 41))
        self.welcome.setAutoFillBackground(False)
        self.welcome.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-color: rgb(176, 176, 176);")
        self.welcome.setObjectName("welcome")
        self.notes_btn = QtWidgets.QPushButton(self.centralwidget)
        self.notes_btn.setGeometry(QtCore.QRect(320, 80, 75, 24))
        self.notes_btn.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-color: rgb(176, 176, 176);")
        self.notes_btn.setObjectName("notes_btn")
        self.slot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.slot_btn.setGeometry(QtCore.QRect(320, 130, 75, 24))
        self.slot_btn.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-color: rgb(176, 176, 176);")
        self.slot_btn.setObjectName("slot_btn")
        self.encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_btn.setGeometry(QtCore.QRect(290, 180, 129, 24))
        self.encrypt_btn.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-color: rgb(176, 176, 176);")
        self.encrypt_btn.setCheckable(False)
        self.encrypt_btn.setObjectName("encrypt_btn")
        self.calc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calc_btn.setGeometry(QtCore.QRect(320, 380, 75, 24))
        self.calc_btn.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-color: rgb(176, 176, 176);")
        self.calc_btn.setObjectName("calc_btn")
        self.clock_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clock_btn.setGeometry(QtCore.QRect(320, 230, 75, 24))
        self.clock_btn.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-color: rgb(176, 176, 176);")
        self.clock_btn.setObjectName("clock_btn")
        self.blud_btn = QtWidgets.QPushButton(self.centralwidget)
        self.blud_btn.setGeometry(QtCore.QRect(320, 280, 75, 24))
        self.blud_btn.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-color: rgb(176, 176, 176);")
        self.blud_btn.setObjectName("blud_btn")
        self.bank_btn = QtWidgets.QPushButton(self.centralwidget)
        self.bank_btn.setGeometry(QtCore.QRect(320, 330, 75, 24))
        self.bank_btn.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-color: rgb(176, 176, 176);")
        self.bank_btn.setObjectName("bank_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(320, 460, 75, 24))
        self.exit_btn.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Sans Serif\";\n"
"border-color: rgb(176, 176, 176);")
        self.exit_btn.setObjectName("exit_btn")
        self.slot_btn.raise_()
        self.notes_btn.raise_()
        self.welcome.raise_()
        self.encrypt_btn.raise_()
        self.calc_btn.raise_()
        self.clock_btn.raise_()
        self.blud_btn.raise_()
        self.bank_btn.raise_()
        self.exit_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "Welcome to DuckyTools!"))
        self.notes_btn.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>test</p></body></html>"))
        self.notes_btn.setText(_translate("MainWindow", "Notes"))
        self.slot_btn.setText(_translate("MainWindow", "Slots"))
        self.encrypt_btn.setText(_translate("MainWindow", "Encrypt and Decrypt"))
        self.calc_btn.setText(_translate("MainWindow", "Calculator"))
        self.clock_btn.setText(_translate("MainWindow", "Clock"))
        self.blud_btn.setText(_translate("MainWindow", "Blud Game"))
        self.bank_btn.setText(_translate("MainWindow", "Bank"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
