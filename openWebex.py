import os 
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

load_dotenv()
meeting_link = os.environ.get('MEETING_LINK')
name = os.environ.get('WEBEX_NAME')
email = os.environ.get('WEBEX_EMAIL')

def control_webex():
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(meeting_link)
    sleep(3)
    # Input username and email
    actions = ActionChains(driver)
    actions.send_keys(name)
    actions.send_keys(Keys.TAB)
    actions.send_keys(email)
    actions.pause(3)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    sleep(2)
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
    # Start action
    start_meeting_actions.perform()
    # Turn off the video after 15 minutes
    # sleep(900)
    sleep(5)
    driver.close()
if __name__ == '__main__':
    control_webex()