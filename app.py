import json
import logging
import os
from collections import OrderedDict

import requests
import sys
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal, SIGNAL
from PyQt4.QtWebKit import QWebSettings

from gui.ui_app import Ui_MainWindow
from gui.ui_watch import Ui_watchWindow
from util.util_downloader import Downloader

basePath = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.insert(0, basePath)

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
logging.disable(logging.DEBUG)
logging.getLogger("requests").setLevel(logging.WARNING)

db = json.load(open('config/SimpsonData.json'), object_pairs_hook=OrderedDict)


class NoBs(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(NoBs, self).__init__(parent)
        self.setupUi(self)
        self.seasons = db['Simpsons']
        self.episodeLIST.itemActivated.connect(self.listhandler)
        self.connect(self.actionSeason_1, SIGNAL('triggered()'), self.seasonone)
        self.watchButton.clicked.connect(self.watch_handler)
        self.window2 = None
        self.watchButton.setEnabled(False)
        self.downloadButton.setEnabled(False)

    def seasonone(self):
        self.episodeLIST.clear()
        self.episodeLIST.addItems(self.seasons['Season One'].keys())
        # self.downloadButton.setEnabled(True)

    def listhandler(self, item):
        url = self.seasons['Season One'][unicode(item.text())]['thumb']


        title = self.seasons['Season One'][unicode(item.text())]['Title']
        desc = self.seasons['Season One'][unicode(item.text())]['desc']
        self.titleLabel.setText(title)
        self.descLabel.setText(desc)
        data = requests.get(url)
        content = data.content

        image = QtGui.QImage()
        image.loadFromData(content)
        self.imgLabel.setPixmap(QtGui.QPixmap(image))
        self.watchButton.setEnabled(True)

    def watch_handler(self):
        lin = self.get_url()
        print lin
        try:
            self.showWatch(lin[0], lin[1])
        except TypeError:
            logging.info('[debug]: episode already playing, please close that episode before starting another.')

    def onFinished(self):
        self.window2 = None

    def showWatch(self, url, Title):
        if self.window2 is None:
            self.window2 = Watch(self)
            self.window2.setWindowTitle(Title)
            self.window2.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
            self.window2.webView.setHtml('''<html>
<body>

<iframe width="520" height="309"
src="%s">
</iframe>

</body>
</html>''' % url)
        self.window2.show()
        self.window2.taskFinished.connect(self.onFinished)

    def get_url(self):
        if self.window2 is None:
            text = self.episodeLIST.currentItem().text()
            if unicode(text) in self.seasons['Season One'].keys():
                abd = self.seasons['Season One'][unicode(text)]['url']
                adg = self.seasons['Season One'][unicode(text)]['Title']
                test = Downloader(abd)
                lin = test.WebsiteEval()
                return lin, adg


class Watch(QtGui.QMainWindow, Ui_watchWindow):

    taskFinished = pyqtSignal()

    def __init__(self, parent=None):
        super(Watch, self).__init__(parent)
        self.setupUi(self)
        self.connect(self, SIGNAL('triggered()'), self.closeEvent)


    def closeEvent(self, event):
        self.taskFinished.emit()
        print "Closing"
        self.deleteLater()




def main():
    app = QtGui.QApplication(sys.argv)
    myapp = NoBs()
    myapp.show()
    app.exec_()


if __name__ == '__main__':
    main()
