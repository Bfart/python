#! /usr/bin/python
# _*_ coding:utf-8 _*_

import urllib2
import json
import threading

url = 'http://172.16.41.5:7980'
value = {'touser':'302764797','msgtype':'text','text':{'content':'hello'}}
def httpPost(url, value):
    jsonData = json.dumps(value)
    req = urllib2.Request(url, jsonData)
    response = urllib2.urlopen(req)
    #return response.read()
    res = response.read()
    print res
#res = httpPost()
#print res

threads = []
for i in range(100):
    thread = threading.Thread(target=httpPost, args=(url,value))
    threads.append(thread)

if __name__ == '__main__':
    for threadTest in threads:
        threadTest.setDaemon(True)
        threadTest.start()
    threadTest.join()


