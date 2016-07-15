#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = '***@163.com'  
receiver = '***@163.com'  
subject = '放假通知'  
smtpserver = 'smtp.163.com'  
username = '***@163.com'  
password = '****'  
  
msg = MIMEText('大家好，今晚聚餐','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')  
msg['From'] = '***@163.com'   
msg['To'] = '*****@163.com'   
smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  
