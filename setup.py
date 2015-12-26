from distutils.core import setup

import os
import pytz
import shutil
import sys

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True,"includes":["sip", "PyQt4.QtNetwork","js2py.pyjs","PyQt4.QtCore","PyQt4.QtGui"],"dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"], "excludes": ["pytz"]}},
    windows = [{'script': "app.py"}],
    zipfile = None,
)

srcDir = os.path.dirname( pytz.__file__ )
dstDir = os.path.join( 'dist', 'pytz' )
shutil.copytree( srcDir, dstDir, ignore = shutil.ignore_patterns('*.py') )