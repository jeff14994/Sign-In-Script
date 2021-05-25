import smtplib
from email.mime.text import MIMEText
from email.header import Header
from dotenv import load_dotenv

load_dotenv()
#SMTP Settings (Google as Sample)
smtpHost = "smtp.gmail.com"
smtpPort = 587
#SMTP Connection Account Settings
smtpUserName = "connectionAccount@gmail.com"
smtpUserPassword = "connectionAccountPassword"
#Email Account Setting
senderEmail = "senderEmail@gmail.com"
senderEmailPassword = "senderPassword"
receiverEmail = ["receiverOne@gmail.com", "receiverTwo@gmail.com"]
#Email Content and Message Setting

#Send Email As Plain Text
#message = MIMEText("Test Send Email By Python", "plain", "utf-8")

#Send Email in HTML Format
mail_msg = """
<p>Testing Sending Email By Python in HTML Format</p>
<p><b>This is a Bold Line</b></p>
<p><a href="https://www.google.com/">This is a link to Google</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("SenderName", "utf-8")
message['To'] = Header("ReceiverName", "utf-8")
subject = "Python SMTP Email Test"
message['Subject'] = Header(subject, "utf-8")
#smtpObj = smtplib.SMTP( [host [, post [, local_hostname]]])

try:
	#smtpObj = smtplib.SMTP(smtpHost, smtpPort)
	smtpObj = smtplib.SMTP()
	print ("SMTP Init")
	smtpObj.connect(smtpHost, smtpPort)
	print ("SMTP Connect")
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.ehlo()
	print ("SMTP ehlo")
	smtpObj.login(smtpUserName, smtpUserPassword)
	print ("SMTP Login")
	smtpObj.sendmail(senderEmail, receiverEmail, message.as_string())
	print ("Email Sent")
except smtplib.SMTPException:
	# print str(error)
	print ("Error: Cannot Send Email")