import os
import re
import glob
import smtplib
from time import localtime, time
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

def send_email(sign_time, status=0):
	# Send Email in HTML Format
	# status = 1 -> send image; status = 0 -> send without image
	if status == '1':
		mail_msg = """
		<p>親愛的學員 """ + student_name + """ 您好：</p>
		<p><b>""" + sign_time + """</b></p>
		<h4>大家簽到狀況：</h4>
		"""
		# Get image
		date = localtime(time())
		month = str(date.tm_mon)
		day = str(date.tm_mday)
		hour = str(date.tm_hour)
		# Get image path 
		img_path = './drive_snapshot/' +  month + '.' + day + '/'
		# print(img_path)
		# Set get image rule
		re_rule = 'daily_' + month + '.' + day + '_4'
		re_rule += '*.png'
		# print(re_rule)
		# files = [f for f in os.listdir(img_path) if re.match(r'[daily_6.4_1*.png]', f)]
		# files = [f for f in os.listdir(img_path) ]
		# Sort glob by last modified time
		files = sorted(glob.glob(img_path + re_rule + '*', ), key=os.path.getmtime)
		# print(files)
		# Choose to send afternoon image or morning image
		if hour == "13":
			try:
				# Select image name
				img_file = files[1].split('/')[-1]
			except:
				print('No image in the morning!')
		else:
			# Select image name
			img_file = files[0].split('/')[-1]
		# print(img_file)
		img_path += img_file
		
		with open(img_path, 'rb') as fp:
			img_data = fp.read()
		message = MIMEMultipart()
		image = MIMEImage(img_data, name=os.path.basename(img_path))
		message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
	
		message.attach(image)
	else:
		mail_msg = """
		<p>親愛的學員 """ + student_name + """ 您好：</p>
		<p><b>""" + sign_time + """</b></p>
		"""
		message = MIMEMultipart()
		message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
	# Add subject to email
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
	send_email('Input time here!', '1')