from urllib.request import Request, urlopen
import requests
import html2text
from h import  text
import time
import os
from urllist import list,list2
from deal_html_to_txt import  *
import shutil



class Internet:

    def __init__(self):
        self.username = '02512578466'
        self.passwd = '683772'
    def outLine(self):
        cmd_str0 = "rasdial/DISCONNECT"
        not_found = os.system(cmd_str0)

    def onLine(self):
        cmd_str1 = "rasdial" + " " + "宽带连接" + " " + self.username + " " + self.passwd
        not_found = os.system(cmd_str1)


str_for_search ="a href=\"/judgement/"
def get_cookie():
        #global JSESSIONID
        JSESSIONID = []
        re = requests
        url = "http://openlaw.cn/search/judgement/type?causeId=270cfcd1df47453d9ff4b8d40901a587"
        req = re.get(url, headers={'Host': 'openlaw.cn',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36',
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                'Referer': url,
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',})

        # if req.cookies.get("JSESSIONID") == None:
        #     pass
        # else:
        JSESSIONID.append(req.cookies.get("JSESSIONID"))
        js = req.text
        if js.find("window.v")==-1:
            return -1
        s = js[js.find("window.v")+10:js.find("window.v")+10+len("_9d439082580f9b6f68e89c09f9b37c43")]
        s1 = s[2:4]
        s2 = "n"
        s3 = s[0:1]
        s4 = "p"
        s5 = s[4:8]
        s6 = "e"
        s7 = s[1:2]
        s8 = s[16:]
        s9 = s[8:16]
        j_token = s1+s2+s3+s4+s5+s6+s7+s8+s9
        cookie = "j_token"+"="+j_token +';'+ "JSESSIONID"+'='+JSESSIONID[0]+';'
        time.sleep(3)
        print(cookie)

        return cookie
def search(str,str2):
    list = []
    key =1
    i =0
    while key!=-1:
        key = str.find(str2,i,len(str))
        i = key+ len(str2)
        list.append(key)
        print(key)
    list2= []
    for i in list:
        if i ==-1:
            return list2
        list2.append(str[i+19:i+19+32])

def changeip():
    line = Internet()
    line.outLine()
    time.sleep(1)
    line.onLine()
    time.sleep(5)
def spid(url,cookie):
    try:
        session = requests
        print('spidcookie',cookie)
        req = session.get(url, headers={'User-Agent': 'Mozilla/5.0',"Cookie":cookie})
        str = req.text
        listid = search(str,str_for_search)
        return listid
    except:
        return -1


def get_data(url,cookie):
    try:
        session = requests
        data = session.get(url, headers={
                                        'Host': 'openlaw.cn',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36',
                "Cookie": cookie,
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                'Referer': url,
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                                         })

        return data.text
    except:
        return -1


def main(url, cookie,num):
    for page in range(1,100):
        print('================plase input page===================')
        pageurl = url + "&page=" + str(page)
        print(pageurl)
        listid = spid(pageurl, cookie)
        key3 =0
        while listid==-1 or len(listid)==0 or len(listid)==1:
                changeip()
                cookie = get_cookie()
                listid = spid(pageurl, cookie)
                key3 = key3+1
                print("key3")
                if key3 ==5:
                    break

        print(listid)
        wpath = str(num)+"/"+"page"+str(page)
        os.mkdir(str(num)+"/"+"page"+str(page))

        for i in range(1, len(listid)):
            id = listid[i]
            print(id)
            urldata = "http://openlaw.cn/judgement/" + str(id)
            html = get_data(urldata, cookie)
            key2 = 0
            while html ==-1:
                key2 = key2+1
                changeip()
                cookie = get_cookie()
                html = get_data(urldata, cookie)
                print('key2')
                print(html)
                if key2 == 2:
                    print(urldata,'====wrong===')
                    break
            a = to_txt(html,wpath)
            key1 = 0
            while a == -1:
                key1 = key1+1
                changeip()
                cookie = get_cookie()
                a = to_txt(html,wpath)
                print('key1')
                print(id)
                if key1==2:
                    break
                    # changeip()
                    # cookie = get_cookie()
            time.sleep(1)
            print(cookie)
        try:
            shutil.move("name.txt",wpath+"/"+"name.txt")
        except:
            pass
        print('==========page',page,' have download finish============')



if __name__=="__main__":
    for num in range(1,9):
        os.mkdir(str(num))
        print('==============input number============')
        changeip()
        cookie = get_cookie()
        key = 0
        while cookie==-1:
            changeip()
            cookie = get_cookie()
        url = list2[num]
        main(url,cookie,num)





