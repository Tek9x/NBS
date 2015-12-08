# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\TekTonic\Desktop\Programming\Python\programs\NBS\designer\ui_app.ui'
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
        MainWindow.resize(473, 309)
        MainWindow.setMinimumSize(QtCore.QSize(473, 309))
        MainWindow.setMaximumSize(QtCore.QSize(473, 309))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.watchButton = QtGui.QPushButton(self.centralwidget)
        self.watchButton.setGeometry(QtCore.QRect(46, 193, 75, 23))
        self.watchButton.setObjectName(_fromUtf8("watchButton"))
        self.downloadButton = QtGui.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(46, 216, 75, 23))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(215, 198, 78, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.episodeLIST = QtGui.QListWidget(self.centralwidget)
        self.episodeLIST.setGeometry(QtCore.QRect(41, 40, 83, 149))
        self.episodeLIST.setObjectName(_fromUtf8("episodeLIST"))
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(178, 8, 260, 16))
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.descLabel = QtGui.QLabel(self.centralwidget)
        self.descLabel.setGeometry(QtCore.QRect(140, 216, 242, 57))
        self.descLabel.setWordWrap(True)
        self.descLabel.setObjectName(_fromUtf8("descLabel"))
        self.imgLabel = QtGui.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(138, 32, 214, 149))
        self.imgLabel.setText(_fromUtf8(""))
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setObjectName(_fromUtf8("imgLabel"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 270, 93, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(2, 272, 54, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 473, 21))
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
        self.label.setText(_translate("MainWindow", "Description", None))
        self.titleLabel.setText(_translate("MainWindow", "@showtitle", None))
        self.descLabel.setText(_translate("MainWindow", "@desc", None))
        self.label_2.setText(_translate("MainWindow", "pre-alpha 0.1a", None))
        self.label_3.setText(_translate("MainWindow", "[RunDLC]", None))
        self.menuLoad.setTitle(_translate("MainWindow", "load", None))
        self.actionSeason_1.setText(_translate("MainWindow", "Season 1", None))

