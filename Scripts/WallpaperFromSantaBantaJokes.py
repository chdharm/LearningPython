import requests
import os
import logging
import threading
import bs4
import requests
import pprint


def download_img(start, end, baseurl):
    folder = baseurl.split(r'/')[-1]
    complete_path = os.path.join("santabanta", folder)
    if (not os.path.exists(complete_path)):
        os.makedirs(complete_path)
    for i in range(start, end):
        url = baseurl + "-" + str(i) + "a.jpg"
        fileName = url.split(r'/')[-1]
        complete_fileName = os.path.join("santabanta", folder, fileName)
        failed = 0
        if (os.path.isfile(complete_fileName)):
            logging.debug("%s exists already" % (fileName))
        else:
            res = requests.get(url)
            try:
                res.raise_for_status()
                logging.debug("%s downloaded" % (fileName))
            except Exception as exc:
                logging.error("%s for %s" % (exc, fileName))
                continue
            imgFile = open(complete_fileName, 'wb')
            for chunk in res.iter_content(100000):
                imgFile.write(chunk)
            imgFile.close();


def download_using_threads(baseurl):
    downloadThreads = []
    for i in range(0, 200, 10):
        downloadThread = threading.Thread(target=download_img, args=(i, i + 10, baseurl))
        downloadThreads.append(downloadThread)
        downloadThread.start()


requests_log = logging.getLogger("requests")
requests_log.addHandler(logging.NullHandler())
requests_log.propagate = False
logging.basicConfig(filename=r'report.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

_url = "http://www.santabanta.com/wallpapers/indian-celebrities(f)/2/?page="
for page in range(1, 2):
    page_url = _url + str(page)
    page = requests.get(page_url)
    page_bs = bs4.BeautifulSoup(page.text)
    actress_list = []
    for link in page_bs.select('a[href]'):
        href = link.get('href')
        if link.get('href').startswith(r'/wallpapers/') and link.get('title') is not None:
            actress_list.append(link.getText())

    for actress in actress_list:
        first = actress.title().replace(' ', '%20')
        second = actress.replace(' ', '-')
        baseurl = "http://media1.santabanta.com/full6/Indian%20%20Celebrities(F)/" + first + "/"\
                  + second Logging Resources and Information.("fetching %s" % (baseurl))
        download_using_threads(baseurl)