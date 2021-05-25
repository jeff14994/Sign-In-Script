# Sign-in Script

## [資策會]自動化簽到系統
- 定時早上 0900 與 下午 0130 會去戳上課簽到系統的 API 
- 戳完後，會寄 Email 提醒你已簽到打卡

## 使用教學
- Step1: 更改 .env.example 的內容 
    - QRCODE = XXX -> XXX 改成資策會提供的連結
    - NAME = XXX -> XXX 改成你的姓名
    - GMAIL_SENDER_EMAIL = XXX -> XXX 改成你的寄信 Email
    - GMAIL_RECEIVER_EMAIL = XXX -> XXX 改成改成你的收信 Email
    - GMAIL_PASSWORD = XXX -> XXX 改成下面教學拿到的密碼
         - 因為會使用到 Google 的 Gmail 所以要去申請自己 Gmail 權限的密碼
        - [教學 - 下半部](https://lininu.blogspot.com/2017/09/NodeJSSendMailService.html)  
- Step2: 記得安裝 dotenv, requests, bs4(BeautifulSoup) 套件
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
- 純方便打卡使用，要自己確定有打到卡。
- 沒打到卡與我無關XD
- 建議可以在收信時是否是正確的時間，是的話才真正有打到卡！
- 確認如下：
    ![](https://i.imgur.com/0iHsw5c.png)