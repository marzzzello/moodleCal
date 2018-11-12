import requests
import time
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler


def get_cal(loginURL, calURL, username, password):
    ses = requests.Session()
    logindata = [('username', username), ('password', password)]
    siteLogin = ses.post(loginURL, data=logindata)
    soupLogin = BeautifulSoup(siteLogin.text, "html5lib")  # Parse the HTML as a string
    loginError = soupLogin.findAll("div", {"class": "alert-box alert"})
    if (len(loginError) > 0):
        print("Login failed")
        return

    cal = ses.get(calURL)
    with open('out/moodle.ical', 'wb') as f:
        f.write(cal.content)
    print("cal is in ./out/moodle.ical")
    del cal


def main():
    loginURL = 'Your Moodle Login Url' #e.g.: 'https://moodle.ruhr-uni-bochum.de/m/login/index.php'
    calURL = 'Your calendar URL' #e.g.: 'https://moodle.ruhr-uni-bochum.de/m/calendar/export_execute.php?userid=42&authtoken=deadbeefcafebabe&preset_what=all&preset_time=recentupcoming'
    username = 'Your Moodle username'
    password = 'Your Moodle password'

    sched = BlockingScheduler()

    @sched.scheduled_job('interval', id='cron', hours=2)
    def cron():
        print(time.strftime("%FT%TZ"), "Trying to get calendar...")
        get_cal(loginURL, calURL, username, password)
        print(time.strftime("%FT%TZ"), "Finished")
    cron()
    sched.start()
main()
