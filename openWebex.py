import os 
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep, time, localtime
from selenium.webdriver.chrome.options import Options
from sendEmail import send_email
from callBrowser import normal_browser, headless_browser

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
    if status == '0':
        normal_browser(driver_path, snapshot_path, name, email, meeting_link)
    else: 
        headless_browser(driver_path, snapshot_path, name, email, meeting_link, chrome_options)
        
if __name__ == '__main__':
    control_webex()