#!/usr/bin/python3.5

import time
import datetime

timestamp = time.time()
print(timestamp)

tm = time.localtime()
print(tm)

tm2 = time.localtime(time.time())
print(tm2)

formatTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(formatTime)

nowTime = time.strftime('%Y-%m-%d %H:%M:%S')
print(nowTime)

nowTime2 = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
print(nowTime2)

nowTime3 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(nowTime3)

nowTime4 = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print(nowTime4)


print("the program execute time....")
startTime = time.time()
#time.sleep(10)
endTime = time.time()

print(endTime - startTime)

print('the datetime execute the difftime....')
startTime2 = datetime.datetime.now()
time.sleep(6)
endTime2 = datetime.datetime.now()
print((endTime2 - startTime2).seconds)

print('add execute day')
day = datetime.datetime.now()
yesterday = day - datetime.timedelta(days=1)
nextDay = day - datetime.timedelta(days=-1)
print(day)
print(yesterday)
print(nextDay)

print("change the time for struct_time")
sturctTime = datetime.datetime.now().timetuple()
print(sturctTime)

stampTime = time.mktime(datetime.datetime.now().timetuple())
print(stampTime)

print("strptime time ....")
strTime = time.strftime('%Y-%m-%d %H:%M:%S')
print(strTime)

sturctTime2 = time.strptime('2014-08-15 10:23:34','%Y-%m-%d %H:%M:%S')
print(sturctTime2)


