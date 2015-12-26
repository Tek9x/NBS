import re

import js2py
import requests


class Downloader(object):
    def __init__(self, url):
        self.url = url

    def WebsiteURL(self):
        videomegaUrlRegex = '(https?:\/\/(www\.)?videomega\.tv\/(view|iframe|cdn)\.php\?ref=([A-Za-z0-9]+))'
        s = requests.Session()
        u = s.get(self.url)
        r = re.findall(videomegaUrlRegex, u.content)[0]
        b = r[0]
        return b

    def WebsiteDownload(self):
        header = {"Referer": "http://google.com/"}
        findeval = '(eval[^<]+)'
        yx = self.WebsiteURL()
        s = requests.Session()
        ldo = s.get(yx, headers=header)
        eV = re.findall(findeval, ldo.content)[0]
        return eV

    def WebsiteEval(self):
        rr = '(\$\("\d"\).\d)'
        eV = self.WebsiteDownload()
        js = re.sub(rr, '', eV)
        downloadURL = js2py.eval_js(js)
        return downloadURL


test = Downloader('http://www.wtso.cc/video/vip/1170/eng/season_9/season_9_episode_3_lisa_39_s_sax')
print test.WebsiteEval()
