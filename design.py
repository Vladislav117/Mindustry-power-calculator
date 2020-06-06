# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 469)
        MainWindow.setStyleSheet("background-color:#1C1C1B")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.generators = QtWidgets.QListWidget(self.centralwidget)
        self.generators.setGeometry(QtCore.QRect(10, 10, 191, 251))
        self.generators.setStyleSheet("QListWidget {color: #429F42 ; background-color: #2D2D2D; border: none;}\n"
"QListWidget:hover {color: #5BD75B ; background-color: #3A3A39; border: none;}")
        self.generators.setMovement(QtWidgets.QListView.Static)
        self.generators.setFlow(QtWidgets.QListView.TopToBottom)
        self.generators.setObjectName("generators")
        self.solve = QtWidgets.QPushButton(self.centralwidget)
        self.solve.setGeometry(QtCore.QRect(10, 310, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.solve.setFont(font)
        self.solve.setStyleSheet("QPushButton {color: #429F42 ; background-color: #2D2D2D; border: none;}\n"
" QPushButton:hover {color: #5BD75B ; background-color: #3A3A39; border: none;} \n"
"QPushButton:pressed {color: #6CFF6C ; background-color: #474746; border: none;}")
        self.solve.setObjectName("solve")
        self.power = QtWidgets.QLineEdit(self.centralwidget)
        self.power.setGeometry(QtCore.QRect(10, 270, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.power.setFont(font)
        self.power.setStyleSheet("QLineEdit {color: #429F42 ; background-color: #2D2D2D; border: none;} \n"
"QLineEdit:hover {color: #5BD75B ; background-color: #3A3A39; border: none;}")
        self.power.setText("")
        self.power.setObjectName("power")
        self.solution = QtWidgets.QTextBrowser(self.centralwidget)
        self.solution.setGeometry(QtCore.QRect(220, 40, 521, 301))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.solution.setFont(font)
        self.solution.setStyleSheet("QTextBrowser {color: #429F42 ; background-color: #2D2D2D; border: none;}\n"
"QTextBrowser:hover {color: #5BD75B ; background-color: #3A3A39; border: none;}")
        self.solution.setObjectName("solution")
        self.solution_text = QtWidgets.QLabel(self.centralwidget)
        self.solution_text.setGeometry(QtCore.QRect(226, 2, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.solution_text.setFont(font)
        self.solution_text.setStyleSheet("QLabel {color: #D1D152}")
        self.solution_text.setObjectName("solution_text")
        self.ru_button = QtWidgets.QPushButton(self.centralwidget)
        self.ru_button.setGeometry(QtCore.QRect(670, 0, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ru_button.setFont(font)
        self.ru_button.setStyleSheet("QPushButton {color: #429F42 ; background-color: #2D2D2D; border: none;}\n"
" QPushButton:hover {color: #5BD75B ; background-color: #3A3A39; border: none;} \n"
"QPushButton:pressed {color: #6CFF6C ; background-color: #474746; border: none;}")
        self.ru_button.setObjectName("ru_button")
        self.en_button = QtWidgets.QPushButton(self.centralwidget)
        self.en_button.setGeometry(QtCore.QRect(590, 0, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.en_button.setFont(font)
        self.en_button.setStyleSheet("QPushButton {color: #429F42 ; background-color: #2D2D2D; border: none;}\n"
" QPushButton:hover {color: #5BD75B ; background-color: #3A3A39; border: none;} \n"
"QPushButton:pressed {color: #6CFF6C ; background-color: #474746; border: none;}")
        self.en_button.setObjectName("en_button")
        self.round = QtWidgets.QRadioButton(self.centralwidget)
        self.round.setGeometry(QtCore.QRect(10, 360, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.round.setFont(font)
        self.round.setStyleSheet("QRadioButton {color: #429F42}")
        self.round.setObjectName("round")
        self.selected_type = QtWidgets.QLineEdit(self.centralwidget)
        self.selected_type.setGeometry(QtCore.QRect(220, 350, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.selected_type.setFont(font)
        self.selected_type.setStyleSheet("QLineEdit {color: #429F42 ; background-color: #2D2D2D; border: none;}\\nQTextBrowser:hover {color: #5BD75B ; background-color: #3A3A39; border: none;}")
        self.selected_type.setText("")
        self.selected_type.setReadOnly(True)
        self.selected_type.setObjectName("selected_type")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 25))
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
        self.solve.setText(_translate("MainWindow", "Calculate"))
        self.power.setPlaceholderText(_translate("MainWindow", "Energy per second"))
        self.solution_text.setText(_translate("MainWindow", "Solution:"))
        self.ru_button.setText(_translate("MainWindow", "RU"))
        self.en_button.setText(_translate("MainWindow", "EN"))
        self.round.setText(_translate("MainWindow", "Round"))
