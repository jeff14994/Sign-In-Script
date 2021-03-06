# Sign-in Script
![GitHub top language](https://img.shields.io/github/languages/top/jeff14994/Sign-In-Script?logo=Python&logoColor=green)
![GitHub repo size](https://img.shields.io/github/repo-size/jeff14994/Sign-In-Script?logo=Github)
![GitHub last commit](https://img.shields.io/github/last-commit/jeff14994/Sign-In-Script?logo=Github)

## [資策會]自動化簽到系統
- 基本上，會幫你做到兩件事
    - 自動打卡
        - 定時早上 0900 與 下午 0130 會去戳上課簽到系統的 API 
        - 戳完後，會寄 Email 提醒你已簽到打卡
    - 自動登入 Webex
       - 定時早上 0900 與 下午 0130 上線 Webex
       - 登入 15 分鐘後自動登出（點名完跳掉 Webex，比較不會佔資源）
       
      ![v3](https://user-images.githubusercontent.com/30124826/119886965-213ac080-bf66-11eb-88fb-fa4a73984bb9.gif)

## 使用教學
- Step1: 更改 .env.example 成 .env，並且修改內部內容
    - QRCODE_LINK = XXX -> XXX 改成資策會提供的連結
    - NAME = XXX -> XXX 改成你的姓名
    - GMAIL_SENDER_EMAIL = XXX -> XXX 改成你的寄信 Email
    - GMAIL_RECEIVER_EMAIL = XXX -> XXX 改成改成你的收信 Email
    - GMAIL_PASSWORD = XXX -> XXX 改成下面教學拿到的密碼
         - 因為會使用到 Google 的 Gmail ，所以要去申請自己 Gmail 權限的密碼
        - [教學 - 下半部](https://lininu.blogspot.com/2017/09/NodeJSSendMailService.html) 
    - Webex
        - WEBEX_NAME = XXX -> XXX 改成你的姓名
        - WEBEX_EMAIL = XXX -> XXX 改成你的信箱
- Step2: 
    - 記得安裝 dotenv, requests, bs4(BeautifulSoup), webdriver套件
    - 下載 [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)，並放在根目錄
- Step3: [使用 crontab](https://serverfault.com/questions/94351/how-to-disable-everything-in-crontab-l)
    - Usage:
        ```bash=
        # Create my_cron.txt and put the following text in my_cron.txt
        vim my_cron.txt 
        0 9 * * 1-5 /usr/bin/python ~/sign/signIn.py >> ~/sign/cron.log 2>&1
        30 13 * * 1-5 /usr/bin/python ~/sign/signIn.py >> ~/sign/cron.log 2>&1

        # Apply crontab
        crontab my_cron.txt

        # To make sure it works
        crontab -l
        ```
    - crontab 確認
        - crontab test by [crontab-0900](https://crontab.guru/#0_9_*_*_1-5)
        - crontab test by [crontab-1330](https://crontab.guru/#30_13_*_*_1-5) 
    - [Mac 使用 crontab 排錯](https://willy2016.pixnet.net/blog/post/218458338-mac-linux-crontab-%E7%84%A1%E6%B3%95%E5%9C%A8-shell-%E4%B8%AD%E5%9F%B7%E8%A1%8C-python%EF%BC%8C%E5%87%BA%E7%8F%BE) 
## Disclaimer
- 先說：沒打到卡與我無關XD
- 純方便打卡使用，要自己確定有打到卡。
- 建議可以在收信時確認是否收到正確的時間，是的話才真正有打到卡！
- 確認如下：(紅色匡起來是打卡時間)
<img src="https://i.imgur.com/0iHsw5c.png" width="500">
