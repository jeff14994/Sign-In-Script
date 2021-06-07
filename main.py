from datetime import datetime
import os
from selenium import webdriver
from signIn import sign_in
from sendEmail import send_email

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    # sign_in()
    send_email('omg', '0')