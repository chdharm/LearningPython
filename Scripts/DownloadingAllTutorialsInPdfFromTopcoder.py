import requests
import pdfcrowd
import urllib2
from bs4 import BeautifulSoup, SoupStrainer

url = "https://www.topcoder.com/community/data-science/data-science-tutorials/"


def save_as_pdf(link, fileName):
    try:
        # we can get user id and toeken by registering on pdfcrowd.com
        client = pdfcrowd.Client("USER_ID", "TOKEN")
        output_file = open(fileName, 'wb')
        page = requests.get(link)
        soup = BeautifulSoup(page.text)
        html = soup.find_all('div', {'class': 'container'})

        client.convertHtml(''.join(map(str, html)), output_file)
        output_file.close()
        print fileName, " saved"
    except pdfcrowd.Error, why:
        print 'Failed:', why


page = requests.get(url)
page_bs = BeautifulSoup(page.text)
tut_links = []
for link_detail in page_bs.select('a[href]'):
    link = link_detail.get('href')
    if link.startswith(url):
        tut_links.append(link)

for link in tut_links:
    fileName = link.split(r'/')[-2] + '.pdf'
    save_as_pdf(link, fileName)