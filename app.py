from PyQt4.QtCore import QThread
from gui.ui_app import Ui_MainWindow
from PyQt4.QtWebKit import QWebView, QWebSettings
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL
import logging, sys, json
from util.util_downloader import Downloader
from gui.ui_watch import Ui_watchWindow
from collections import OrderedDict

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
logging.disable(logging.DEBUG)
logging.getLogger("requests").setLevel(logging.WARNING)

db = json.load(open('config/SimpsonData.json'), object_pairs_hook=OrderedDict)


class NoBs(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(NoBs, self).__init__(parent)
        self.setupUi(self)
        self.seasons = db['Simpsons']
        # self.SeasonBox.activated[str].connect(self.onActivated)
        self.connect(self.actionSeason_1, SIGNAL('triggered()'), self.seasonone)
        self.watchButton.clicked.connect(self.watch_handler)
        self.window2 = None
        self.watchButton.setEnabled(False)
        self.downloadButton.setEnabled(False)
        self.SeasonBox.setEnabled(False)

    def seasonone(self):
        self.SeasonBox.clear()
        self.SeasonBox.addItems(self.seasons['Season One'].keys())
        # self.downloadButton.setEnabled(True)
        self.watchButton.setEnabled(True)
        self.SeasonBox.setEnabled(True)

    def watch_handler(self):
        lin = self.get_url()
        print lin
        self.showWatch(lin[0], lin[1])

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

    def get_url(self):
        if self.window2 is None:
            text = self.SeasonBox.currentText()
            if unicode(text) in self.seasons['Season One'].keys():
                abd = self.seasons['Season One'][unicode(text)]['url']
                adg = self.seasons['Season One'][unicode(text)]['Title']
                test = Downloader(abd)
                lin = test.WebsiteEval()
                return lin, adg


class Watch(QtGui.QMainWindow, Ui_watchWindow):
    def __init__(self, parent=None):
        super(Watch, self).__init__(parent)
        self.setupUi(self)
        self.connect(self, SIGNAL('triggered()'), self.closeEvent)

    def closeEvent(self, event):
        print "Closing"
        self.webView.close()


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = NoBs()
    myapp.show()
    app.exec_()


if __name__ == '__main__':
    main()
