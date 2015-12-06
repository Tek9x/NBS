# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\TekTonic\Desktop\ui_app.ui'
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
        MainWindow.resize(266, 149)
        MainWindow.setMinimumSize(QtCore.QSize(266, 149))
        MainWindow.setMaximumSize(QtCore.QSize(266, 149))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.SeasonBox = QtGui.QComboBox(self.centralwidget)
        self.SeasonBox.setGeometry(QtCore.QRect(70, 40, 121, 22))
        self.SeasonBox.setObjectName(_fromUtf8("SeasonBox"))
        self.watchButton = QtGui.QPushButton(self.centralwidget)
        self.watchButton.setGeometry(QtCore.QRect(20, 103, 75, 23))
        self.watchButton.setObjectName(_fromUtf8("watchButton"))
        self.downloadButton = QtGui.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(170, 103, 75, 23))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 266, 18))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuLoad = QtGui.QMenu(self.menuBar)
        self.menuLoad.setObjectName(_fromUtf8("menuLoad"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionSeason_1 = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        self.actionSeason_1.setFont(font)
        self.actionSeason_1.setObjectName(_fromUtf8("actionSeason_1"))
        self.menuLoad.addAction(self.actionSeason_1)
        self.menuBar.addAction(self.menuLoad.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NoBullshit Simpsons", None))
        self.watchButton.setText(_translate("MainWindow", "Watch", None))
        self.downloadButton.setText(_translate("MainWindow", "Download", None))
        self.menuLoad.setTitle(_translate("MainWindow", "load", None))
        self.actionSeason_1.setText(_translate("MainWindow", "Season 1", None))

