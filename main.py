import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime, calendar
import page
from Meet import *

# CHROME OPTIONS
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

# LOGIN TOOLS
email_info = 'sirbu.andrei@info.tm.edu.ro'
password_info = 'Q2PStzkaPcms'
gmail = 'https://mail.google.com'
meet = 'https://meet.google.com/'


class GoogleMeet(unittest.TestCase):

    def setUp(self):
        # INITIALIZE DRIVER
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
        self.driver.get(gmail)

    def test_connect(self):
        # TYPE EMAIL AND HIT NEXT
        loginEmailPage = page.LoginEmailPage(self.driver)
        loginEmailPage.email = email_info
        loginEmailPage.click_next_button()

        # TYPE PASSWORD AND LOGIN
        loginPasswordPage = page.LoginPasswordPage(self.driver)
        loginPasswordPage.password = password_info
        loginPasswordPage.click_login_button()

        # WAIT TO CONNECT (wait until the inbox is shown)
        inboxGmailPage = page.GmailPage(self.driver)
        inboxGmailPage.inbox = 'wait'

        # GET THE DAY OF THE WEEK
        today_date = calendar.day_name[datetime.date.today().weekday()]

        # SEARCH FOR TODAY IN THE TIMETABLE
        for day in timetable:
            if day[0] == today_date:
                # ITERATE THROUGH THE CLASSES AND CONNECT
                for hour in day[1:]:
                    # CONNECT TO MEET WEBSITE OR DISCONNECT FROM PREVIOUS CLASS
                    self.driver.get(meet)

                    # GET THE EXACT TIME
                    today = datetime.datetime.now()

                    # CHECK IF YOU STILL HAVE TO CONNECT
                    if today.hour <= int(hour.finish_hour) or (today.hour == int(hour.finish_hour) and today.minute < int(hour.finish_min)):

                        # CHECK IF BREAK AND WAIT
                        while today.hour <= int(hour.start_hour) and today.minute <= int(hour.start_min):
                            today = datetime.datetime.now()

                        # ADD THE SPECIFIC MEETING CODE AND CONNECT
                        googleMeetPage = page.GoogleMeetPage(self.driver)
                        googleMeetPage.click_use_a_code_button()
                        googleMeetPage.code = hour.meet_code
                        googleMeetPage.connect_to_meet()

                        # MUTE MIC, WEBCAM AND JOIN
                        googleMeetJoiningPage = page.GoogleMeetJoiningPage(self.driver)
                        googleMeetJoiningPage.join_button = 'wait'
                        googleMeetJoiningPage.mute_mic()
                        googleMeetJoiningPage.unseen_webcam()
                        # CONNECT AFTER THE SPECIFIED AMOUNT
                        time.sleep(60*hour.connect_after)
                        googleMeetJoiningPage.join()

                        # WAIT FOR PAGE TO LOAD
                        googleMeetClassPage = page.GoogleMeetClassPage(self.driver)
                        googleMeetClassPage.show_chat = 'wait'
                        googleMeetClassPage.show()

                        disconnect = False
                        people_connected_max = 0

                        # LEAVE WHEN MOST OF THE PEOPLE LEAVE (finish_hour does not matter)
                        while not disconnect:
                            time.sleep(2.5)
                            # VALUE FORMAT IS 'x participants' (use .split(' ')[0] to get the x value)
                            people_connected_now = int(googleMeetClassPage.get_participants.split(' ')[0])
                            if people_connected_now > people_connected_max:
                                people_connected_max = people_connected_now
                            elif people_connected_now <= people_connected_max/2:
                                disconnect = True

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
