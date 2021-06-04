import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from dotenv import load_dotenv

load_dotenv()
sender = os.environ.get('GMAIL_SENDER_EMAIL')
receiver = os.environ.get('GMAIL_RECEIVER_EMAIL')
password = os.environ.get('GMAIL_PASSWORD')
student_name = os.environ.get('NAME')
#SMTP Settings (Google as Sample)
smtpHost = "smtp.gmail.com"
smtpPort = 587
#SMTP Connection Account Settings
smtpUserName = sender
smtpUserPassword = password
#Email Account Setting
senderEmail = sender

receiverEmail = receiver
# receiverEmail = ["receiverOne@gmail.com", "receiverTwo@gmail.com"]
#Email Content and Message Setting

#Send Email As Plain Text
#message = MIMEText("Test Send Email By Python", "plain", "utf-8")

def send_email(time, status=0):
	# Send Email in HTML Format
	if status == '1':
		mail_msg = """
		<p>親愛的學員 """ + student_name +""" 您好：</p>
		<p><b>"""+ time +"""</b></p>
		"""
		# Get image
		img_path = './drive_snapshot/6.4/'
		img_file = 'daily_6.4_3_登入後_13:29:4.png'
		img_path += img_file
		
		with open(img_path, 'rb') as fp:
			img_data = fp.read()
		message = MIMEMultipart()
		image = MIMEImage(img_data, name=os.path.basename(img_path))
		message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
	
		message.attach(image)
	else:
		mail_msg = """
		<p>親愛的學員 """ + student_name +""" 您好：</p>
		<p><b>"""+ time +"""</b></p>
		"""
		message = MIMEMultipart()
		message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
	message['From'] = Header("歡迎使用 @x0mg 登入系統", "utf-8")
	message['To'] = Header("親愛的同學", "utf-8")
	subject = "[資策會]AI養成班課程遠距簽到 打卡成功"
	message['Subject'] = Header(subject, "utf-8")
	
	try:
		#smtpObj = smtplib.SMTP(smtpHost, smtpPort)
		smtpObj = smtplib.SMTP(smtpHost, smtpPort)
		# print ("SMTP Init")
		# print ("SMTP ehlo")
		smtpObj.ehlo()
		smtpObj.starttls()
		smtpObj.login(smtpUserName, smtpUserPassword)
		# print ("SMTP Login")
		smtpObj.sendmail(senderEmail, receiverEmail, message.as_string())
		# print ("Email Sent")
	except smtplib.SMTPException:
		# print str(error)
		print ("Error: Cannot Send Email")
if __name__ == '__main__':
	send_email('Input time here!')