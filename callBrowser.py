from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep, time, localtime
from selenium.webdriver.chrome.options import Options
from sendEmail import send_email

def normal_browser(driver_path, snapshot_path, name, email, meeting_link):
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
    sleep(900)
    # Stop for 7.5 hours
    # sleep(27000)
    driver.close()

def headless_browser(driver_path, snapshot_path, name, email, meeting_link, chrome_options):
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
    driver.get_screenshot_as_file(snapshot_path + file_name)
    # Send email
    send_email('已開啟 Webex', '1')
    # Turn off the video after 15 minutes
    # sleep(900)
    # Stop for 7.5 hours
    sleep(900)
    driver.close()