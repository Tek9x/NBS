from PyQt4.QtCore import QThread
from PyQt4 import QtCore
import requests, re, js2py, time


class geturl(QThread):


    def __init__(self, url):
        QThread.__init__(self)
        self.url = url

    def __del__(self):
        self.wait()

    def run(self):
        pass
