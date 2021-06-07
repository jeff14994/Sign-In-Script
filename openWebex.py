import os 
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep, time, localtime
from selenium.webdriver.chrome.options import Options
from sendEmail import send_email

load_dotenv()
meeting_link = os.environ.get('MEETING_LINK')
name = os.environ.get('WEBEX_NAME')
email = os.environ.get('WEBEX_EMAIL')
def control_webex():
    # 0 open the browser, 1 for headless
    status = '0'
    # Configure headless settings
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options() 
    chrome_options.add_argument('--headless')  
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument("--start-maximized")
    # Change to sigin directory
    working_directory = "/Users/hungyuchuan/Desktop/近期代辦/資策會課程/sign"
    os.chdir(working_directory)
    driver_path = os.getcwd() + '/chromedriver'
    print("Chromedrive working directory:", driver_path)
    snapshot_path = './drive_snapshot/'
    # Use try to make outter dir
    try:
        os.makedirs('drive_snapshot')
    # If file exists, show below
    except FileExistsError:
        # print("dir exists")
        pass
    # Use try to make inner dir (Rule: By date)
    date = localtime(time())
    file_name = str(date.tm_mon) + '.' + str(date.tm_mday) + '/'
    # Create directory daily
    snapshot_path += file_name
    try:
        os.makedirs('drive_snapshot/' + file_name)
    # If file exists, show below
    except FileExistsError:
        # print("dir exists")
        pass
    # 0 open the browser, 1 for headless
    if status == '1':
        # Load driver
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.implicitly_wait(10)
        driver.maximize_window()
        # Make requests
        driver.get(meeting_link)
        sleep(3)
        # Screenshot
        date = localtime(time())
        file_name = 'daily_' + str(date.tm_mon) + '.' + str(date.tm_mday) + '_' + '1_登入前_' + str(date.tm_hour)  + ':' + str(date.tm_min) + ':' + str(date.tm_sec) + '.png'
        print('Screenshot...1...Before_login')
        driver.get_screenshot_as_file(snapshot_path + file_name)
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
        date = localtime(time())
        file_name = 'daily_' + str(date.tm_mon) + '.' + str(date.tm_mday) + '_' + '2_輸入名字_' + str(date.tm_hour)  + ':' + str(date.tm_min) + ':' + str(date.tm_sec) + '.png'
        print('Screenshot...2...Enter_credentials')
        driver.get_screenshot_as_file(snapshot_path + file_name)
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
        date = localtime(time())
        file_name = 'daily_' + str(date.tm_mon) + '.' + str(date.tm_mday) + '_' + '3_登入後_' + str(date.tm_hour)  + ':' + str(date.tm_min) + ':' + str(date.tm_sec) + '.png'
        print('Screenshot...3...Enter_the_meeting')
        driver.get_screenshot_as_file(snapshot_path + file_name)
        # === See all participants ===
        see_participants_actions = ActionChains(driver)
        see_participants_actions.send_keys(Keys.ENTER)
        see_participants_actions.send_keys(Keys.TAB * 23)
        see_participants_actions.send_keys(Keys.ENTER)
        # === See all participants - Start action ===
        see_participants_actions.perform()
        # Snapshot
        date = localtime(time())
        file_name = 'daily_' + str(date.tm_mon) + '.' + str(date.tm_mday) + '_' + '4_所有登入者_' + str(date.tm_hour)  + ':' + str(date.tm_min) + ':' + str(date.tm_sec) + '.png'
        print('Screenshot...4...See_all_participants')
        snapshot_path = snapshot_path + file_name
        driver.get_screenshot_as_file(snapshot_path + file_name)
        # Send email
        send_email('已開啟 Webex', '1')
        # Turn off the video after 15 minutes
        # sleep(900)
        # Stop for 7.5 hours
        sleep(9000)
        driver.close()
    else: 
        # TODO: Fix the headless browser
        # Load driver
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        # Make requests
        driver.get(meeting_link)
        sleep(3)
        # Screenshot
        date = localtime(time())
        file_name = 'daily_' + str(date.tm_mon) + '.' + str(date.tm_mday) + '_' + '1_登入前_' + str(date.tm_hour)  + ':' + str(date.tm_min) + ':' + str(date.tm_sec) + '.png'
        print('Screenshot...1...Before_login')
        driver.get_screenshot_as_file(snapshot_path + file_name)
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
        date = localtime(time())
        file_name = 'daily_' + str(date.tm_mon) + '.' + str(date.tm_mday) + '_' + '2_輸入名字_' + str(date.tm_hour)  + ':' + str(date.tm_min) + ':' + str(date.tm_sec) + '.png'
        print('Screenshot...2...Enter_credentials')
        driver.get_screenshot_as_file(snapshot_path + file_name) #截圖格式和存放地址
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
        date = localtime(time())
        file_name = 'daily_' + str(date.tm_mon) + '.' + str(date.tm_mday) + '_' + '3_登入後_' + str(date.tm_hour)  + ':' + str(date.tm_min) + ':' + str(date.tm_sec) + '.png'
        print('Screenshot...3...Enter_the_meeting')
        driver.get_screenshot_as_file(snapshot_path + file_name)
        # === See all participants ===
        see_participants_actions = ActionChains(driver)
        see_participants_actions.send_keys(Keys.ENTER)
        see_participants_actions.send_keys(Keys.TAB * 34)
        see_participants_actions.send_keys(Keys.ENTER)
        # === See all participants - Start action ===
        see_participants_actions.perform()
        # Snapshot
        date = localtime(time())
        file_name = 'daily_' + str(date.tm_mon) + '.' + str(date.tm_mday) + '_' + '4_所有登入者_' + str(date.tm_hour)  + ':' + str(date.tm_min) + ':' + str(date.tm_sec) + '.png'
        print('Screenshot...4...See_all_participants')
        snapshot_path = snapshot_path + file_name
        driver.get_screenshot_as_file(snapshot_path + file_name)
        # Send email
        send_email('已開啟 Webex', '1')
        # Turn off the video after 15 minutes
        # sleep(900)
        # Stop for 7.5 hours
        sleep(900)
        driver.close()
        
if __name__ == '__main__':
    control_webex()