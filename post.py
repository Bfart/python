#! /usr/bin/python
# _*_ coding:utf-8 _*_
import urllib2
import threading

url = "http://172.16.41.5:7980"
values = "<xml><ToUserName>302764797</ToUserName><FromUserName>938019899</FromUserName><CreateTime>2016-15-45</CreateTime><MsgType>1</MsgType><Content>你好</Content></xml>"


threads = []

def postRequest(url,data):
    req = urllib2.Request(url = url,headers = {'Content-Type' : 'text/xml'},data = values)
    response = urllib2.urlopen(req)
    res = response.read()
    print(res)


for i in range(100):
    thread = threading.Thread(target=postRequest,args=(url,values))
    print values
    threads.append(thread)

if __name__ == '__main__':
    for threadTest in threads:
        threadTest.setDaemon(True)
        threadTest.start()
    threadTest.join() #阻塞主线程，只有全部子线程执行完了，才执行主线程


