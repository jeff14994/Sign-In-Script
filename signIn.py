#!/Users/hungyuchuan/opt/anaconda3/bin/python
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from sendEmail import send_email
from datetime import datetime
from openWebex import control_webex

load_dotenv()
qrcode_link = os.environ.get('QRCODE_LINK')
student_name = os.environ.get('NAME')

# Start request
url = qrcode_link
# res = requests.get(url)
response = """
<style type="text/css">
bg-img {
    background: url('/qrcode/remote_attendance.png');
    background-size:     contain;
    background-repeat:   no-repeat;
    background-position: center center;     
}
.text {
    text-align: center;
    font-size: 50px;
}
body{
    font-family: "Microsoft JhengHei"!important;
}
</style>
<body>
    <div>
        <p class="text">課程名稱：AI 人工智慧創新應用就業養成班</p>
        <p class="text">學生姓名：洪裕權</p>
        <p class="text">刷卡時間：2021-05-25 07:59:04</p> 
            </div>

</body>
"""
# Response from web
soup = BeautifulSoup(response, 'html.parser')
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
    print('正在開啟 Webex')
    control_webex()
    print('正在關閉 Webex')
