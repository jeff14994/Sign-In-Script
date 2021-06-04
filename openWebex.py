import os 
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep, time, ctime
from selenium.webdriver.chrome.options import Options

load_dotenv()
meeting_link = os.environ.get('MEETING_LINK')
name = os.environ.get('WEBEX_NAME')
email = os.environ.get('WEBEX_EMAIL')
snapshot_path = '/Users/hungyuchuan/Desktop/近期代辦/資策會課程/sign/drive_snapshot/'
def control_webex():
    # 0 open the browser, 1 for headless
    status = '0'
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options() 
    # Start headless
    chrome_options.add_argument('--headless')  
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument("--start-maximized")
    # Load driver
    path = '/Users/hungyuchuan/Desktop/近期代辦/資策會課程/sign/chromedriver'
    if status == '0':
        driver = webdriver.Chrome(executable_path=path)
        driver.implicitly_wait(10)
        driver.maximize_window()
        # Make requests
        driver.get(meeting_link)
        sleep(3)
        # Screenshot
        local_time = ctime(time())
        print('Screenshot...1...Before_login')
        driver.get_screenshot_as_file(snapshot_path + 'daily-1-登入前-' + local_time + '-.png') #截圖格式和存放地址
        #  === Input username and email ===
        actions = ActionChains(driver)
        actions.send_keys(name)
        actions.send_keys(Keys.TAB)
        actions.send_keys(email)
        actions.pause(3)
        actions.send_keys(Keys.ENTER)
        # === Input username and email - Start action ===
        actions.perform()
        # Screenshot
        # 從 1970/1/1 00:00:00 至今的秒數
        seconds = time()
        # 將秒數轉為本地時間
        local_time = ctime(seconds)
        print('Screenshot...2...Enter_credentials')
        driver.get_screenshot_as_file(snapshot_path + 'daily-2-輸入名字-' + local_time + '-.png') #截圖格式和存放地址
        sleep(3)
        # === Configure setting before entering meeting ===
        start_meeting_actions = ActionChains(driver)
        # Mute the sound
        start_meeting_actions.send_keys(Keys.TAB * 4)
        start_meeting_actions.send_keys(Keys.ENTER)
        # Turn off the video
        start_meeting_actions.send_keys(Keys.TAB * 2)
        start_meeting_actions.send_keys(Keys.ENTER)
        # Join Meeting
        start_meeting_actions.send_keys(Keys.TAB * 8)
        start_meeting_actions.send_keys(Keys.ENTER)
        # === Configure setting before entering meeting - Start action ===
        start_meeting_actions.perform()
        # Screenshot
        sleep(5)
        # 從 1970/1/1 00:00:00 至今的秒數
        seconds = time()
        # 將秒數轉為本地時間
        local_time = ctime(seconds)
        print('Screenshot...3...Enter_the_meeting')
        driver.get_screenshot_as_file(snapshot_path + 'daily-3-登入後-' + local_time + '-.png') #截圖格式和存放地址
        # Turn off the video after 15 minutes
        # sleep(900)
        # Stop for 7.5 hours
        sleep(10)
        driver.close()
    else: 
        driver = webdriver.Chrome(executable_path=path, options=chrome_options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        # Make requests
        driver.get(meeting_link)
        sleep(3)
        # Screenshot
        print('Screenshot...1...Before_login')
        driver.get_screenshot_as_file('/Users/hungyuchuan/Desktop/近期代辦/資策會課程/sign/daily1-登入前.png') #截圖格式和存放地址
        #  === Input username and email ===
        actions = ActionChains(driver)
        actions.send_keys(name)
        actions.send_keys(Keys.TAB)
        actions.send_keys(email)
        actions.pause(3)
        actions.send_keys(Keys.ENTER)
        # === Input username and email - Start action ===
        actions.perform()
        # Screenshot
        # sleep(3)
        print('Screenshot...2...Enter_credentials')
        driver.get_screenshot_as_file('/Users/hungyuchuan/Desktop/近期代辦/資策會課程/sign/daily2-輸入名字.png') #截圖格式和存放地址
        sleep(3)
        # === Configure setting before entering meeting ===
        start_meeting_actions = ActionChains(driver)
        # Get directly to the meeting
        start_meeting_actions.send_keys(Keys.TAB * 12)
        start_meeting_actions.send_keys(Keys.ENTER)
        # === Configure setting before entering meeting - Start action ===
        start_meeting_actions.perform()

        # Screenshot
        sleep(5)
        print('Screenshot...3...Enter_the_meeting')
        driver.get_screenshot_as_file('/Users/hungyuchuan/Desktop/近期代辦/資策會課程/sign/daily3-登入後.png') #截圖格式和存放地址
        # Turn off the video after 15 minutes
        sleep(900)
        # Stop for 7.5 hours
        # sleep(27000)
        sleep(10)
        driver.close()
if __name__ == '__main__':
    control_webex()