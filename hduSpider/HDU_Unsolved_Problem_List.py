import requests, re
from bs4 import BeautifulSoup


def unsolved_problem():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 '
                      'Safari/537.36'
    }
    url = 'http://acm.hdu.edu.cn/userstatus.php?user=YTMartian'
    data = requests.get(url = url, headers = headers).text
    soup = BeautifulSoup(data, 'html.parser')
    soup = soup.select('p')
    reg = '[0-9]{4}'
    soup = re.findall(re.compile(reg), str(soup))
    x = range(1000, 6100)
    ans = []
    for i in x:
        if (str(i) in soup):
            continue
        ans.append(i)
    print(len(ans))
    return ans
unsolved_problem()



