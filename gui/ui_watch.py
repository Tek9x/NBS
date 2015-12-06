# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\TekTonic\Desktop\ui_watch.ui'
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

class Ui_watchWindow(object):
    def setupUi(self, watchWindow):
        watchWindow.setObjectName(_fromUtf8("watchWindow"))
        watchWindow.resize(528, 336)
        watchWindow.setMinimumSize(QtCore.QSize(528, 336))
        watchWindow.setMaximumSize(QtCore.QSize(528, 336))
        self.centralwidget = QtGui.QWidget(watchWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(-4, -5, 533, 346))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        watchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(watchWindow)
        QtCore.QMetaObject.connectSlotsByName(watchWindow)

    def retranslateUi(self, watchWindow):
        watchWindow.setWindowTitle(_translate("watchWindow", "@showtitle", None))

from PyQt4 import QtWebKit
