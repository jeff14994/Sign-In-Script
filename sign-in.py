import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
qrcode = os.environ.get('QRCODE')
student_name = os.environ.get('NAME')
# print(qrcode)
# print(student_name)
# Start request
url = 'https://manage.iiiedu.org.tw/api/class/remoteAttendance?qrcode=' + qrcode
# res = requests.get(url)

# print(res.text)
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
soup = BeautifulSoup(res, 'html.parser')
p_tag = soup.find_all('p')
class_name = 'AI 人工智慧創新應用就業養成班'
# 資料前處理
response_class = p_tag[0].text[5:]
response_name = p_tag[1].text[5:]
response_time = p_tag[2].text
if (response_class == class_name and response_name == student_name):
    print('打卡成功！')
    print(response_time)

# for i in p_tag:
#     print(i.text) 
# print(soup.find_all('p').text)