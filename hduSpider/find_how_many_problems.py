import requests, threading, time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/59.0.3071.115 Safari/537.36'
}

f = open('existed_problems.txt', 'a')


def crawler(url):
    global headers
    global f
    data = requests.get(url = url, headers = headers).text
    soup = BeautifulSoup(data, 'html.parser').select('div')
    if 'No such problem' in str(soup):
        print("no such problem")
    else:
        f.write(url[-4:] + '\n')
    print(url[-4:])


def main():
    u = 'http://acm.hdu.edu.cn/showproblem.php?pid='
    threads = []
    for i in range(5242, 6120): # 题目范围
        url = u + str(i)
        t = threading.Thread(target = crawler, args = (url,))
        threads.append(t)
    for t in threads:
        t.start()
        while True:
            if (len(threading.enumerate()) < 20):
                break
            else:
                time.sleep(1)
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
    f.close()
    f = open('existed_problems.txt', 'r')
    f=f.readline()
    print(f)