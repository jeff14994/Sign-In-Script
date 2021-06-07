from datetime import datetime
# from signIn import sign_in
from sendEmail import send_email
from openWebex import control_webex

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    print("Signing in ...")
    # sign_in()
    # send_email('omg', '0')
    control_webex()
cronjob()