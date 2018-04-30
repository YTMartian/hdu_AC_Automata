import urllib.request, urllib, requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com/s?wd=hdu'
session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 '
                  'Safari/537.36'
}


def Download_CSDN_Answer(url):
    data = session.get(url, headers = headers).text
    soup = BeautifulSoup(data, 'html.parser')
    inf = soup.select('pre.cpp')
    for i in inf:
        return i.get_text()


def get_CSDN_url(problem):
    urllist = []
    baidu = url + str(problem) + '%20csdn'
    data = session.get(baidu, headers = headers).text
    soup = BeautifulSoup(data, 'html.parser')
    soup = soup.select('h3.t > a')
    for i in soup:
        i = i.get('href')
        urllist.append(i)
    return urllist