import requests
import re
import js2py


class Downloader(object):
    def __init__(self, url):
        self.url = url

    def WebsiteURL(self):
        videomegaUrlRegex = '(https?:\/\/(www\.)?videomega\.tv\/(view|iframe|cdn)\.php\?ref=([A-Za-z0-9]+))'
        u = requests.get(self.url)
        r = re.findall(videomegaUrlRegex, u.content)[0]
        b = r[0]
        return b

    def WebsiteDownload(self):
        header = {"Referer": "http://google.com/"}
        findeval = '(eval[^<]+)'
        yx = self.WebsiteURL()
        ldo = requests.get(yx, headers=header)
        eV = re.findall(findeval, ldo.content)[0]
        return eV

    def WebsiteEval(self):
        rr = '(\$\("\d"\).\d)'
        eV = self.WebsiteDownload()
        js = re.sub(rr, '', eV)
        downloadURL = js2py.eval_js(js)
        return downloadURL



#test = Downloader('http://www.wtso.cc/video/vip/992/eng/season_1/season_1_episode_6_moaning_lisa')
#test.WebsiteEval()



