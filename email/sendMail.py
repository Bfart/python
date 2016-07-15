#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = 'ziliu1991@163.com'  
receiver = 'Bfart1991@163.com'  
subject = '放假通知'  
smtpserver = 'smtp.163.com'  
username = 'ziliu1991@163.com'  
password = 'liuhui520'  
  
msg = MIMEText('大家好，今晚聚餐','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')  
msg['From'] = 'ziliu1991@163.com'   
msg['To'] = 'Bfart1991@163.com'   
smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  
