import urllib.request, urllib.parse
import http.cookiejar, time
import HDU_Answer_Spider, HDU_Unsolved_Problem_List

host_url = 'http://acm.hdu.edu.cn/userloginex.php?action=login'
sub_url = 'http://acm.hdu.edu.cn/submit.php?action=submit'
# 登陆
cj = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)
postdata = {
    'username': '******', 'userpass': '******', 'login': 'Sign In' # 太粗心了，忘记去掉密码了！！
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
}
postdata = urllib.parse.urlencode(postdata).encode(encoding = 'utf8')
r = urllib.request.Request(host_url, postdata, headers)
res = urllib.request.urlopen(r)
if res.getcode() == 200:
    print ('Sign In OK')
else:
    print ('Sign In False')

'''
头次提交即可AC, 若头次提交未AC，将下面代码注释掉，执行‘头次提交未AC’处的代码
'''

for problem in range(6117, 6276): # 题目编号范围
    urllist = HDU_Answer_Spider.get_CSDN_url(problem)
    h = urllist[1]
    code = HDU_Answer_Spider.Download_CSDN_Answer(h)
    #提交代码
    postData = {'check':'0',
          'problemid':problem,
          'language':'0',
          'usercode':code,
    }
    postData = urllib.parse.urlencode(postData).encode(encoding = 'utf8')
    request = urllib.request.Request(sub_url, postData, headers)
    response = urllib.request.urlopen(request)
    print (problem, 'Submit OK')
    time.sleep(20)


'''
头次提交未AC
'''
'''
p = HDU_Unsolved_Problem_List.unsolved_problem()
for problem in p:
    if problem < 3798:
        continue
    urllist = HDU_Answer_Spider.get_CSDN_url(problem)
    if len(urllist) == 0:
        continue
    if len(urllist) > 3:
        k = 3
    else:
        k = len(urllist)
    for j in range(0, k):
        h = urllist[j]
        try:
            code = HDU_Answer_Spider.Download_CSDN_Answer(h)
        except Exception as e:
            print(e)
        if code == None:
            print('None')
            continue
        if 'include' not in code:
            print('Not Code')
            continue
        postData = {
            'check': '0', 'problemid': problem, 'language': '0', 'usercode': code,
        }
        postData = urllib.parse.urlencode(postData).encode(encoding = 'utf8')
        request = urllib.request.Request(sub_url, postData, headers)
        try:
            response = urllib.request.urlopen(request)
        except Exception as e:
            print(e)
        print(problem, 'Submit OK')

'''
