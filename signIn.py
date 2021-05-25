#!/Users/hungyuchuan/opt/anaconda3/bin/python
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from sendEmail import send_email
from datetime import datetime

load_dotenv()
qrcode_link = os.environ.get('QRCODE_LINK')
student_name = os.environ.get('NAME')

# Start request
url = qrcode_link
res = requests.get(url)

# Response from web
soup = BeautifulSoup(res.text, 'html.parser')
p_tag = soup.find_all('p')
class_name = 'AI 人工智慧創新應用就業養成班'
# 資料前處理
response_class = p_tag[0].text[5:]
response_name = p_tag[1].text[5:]
response_time = p_tag[2].text
if (response_class == class_name and response_name == student_name):
    print(datetime.now())
    print('打卡成功！')
    print(response_time)
    send_email(response_time)
