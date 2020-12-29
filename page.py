from locators import *
from element import GoogleMeetLoginElement, WaitForElement, GetParticipantsElement


class Email(GoogleMeetLoginElement):
    locator = '//*[@id="identifierId"]'


class Password(GoogleMeetLoginElement):
    locator = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'


class Inbox(WaitForElement):
    locator = '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div'


class UseCode(GoogleMeetLoginElement):
    locator = '/html/body/div[1]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input'


class JoinButton(WaitForElement):
    locator = '/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]'


class ShowChat(WaitForElement):
    locator = '/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span'


class GetParticipants(GetParticipantsElement):
    locator = '/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginEmailPage(BasePage):
    email = Email()

    def click_next_button(self):
        element = self.driver.find_element(*LoginPageLocators.NEXT_BUTTON)
        element.click()


class LoginPasswordPage(BasePage):
    password = Password()

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()


class GmailPage(BasePage):
    inbox = Inbox()


class GoogleMeetPage(BasePage):
    code = UseCode()

    def click_use_a_code_button(self):
        element = self.driver.find_element(*GoogleMeetPageLocators.USE_CODE)
        element.click()

    def connect_to_meet(self):
        element = self.driver.find_element(*GoogleMeetPageLocators.CONNECT)
        element.click()


class GoogleMeetJoiningPage(BasePage):
    join_button = JoinButton()

    def mute_mic(self):
        element = self.driver.find_element(*GoogleMeetJoiningPageLocators.MIC)
        element.click()

    def unseen_webcam(self):
        element = self.driver.find_element(*GoogleMeetJoiningPageLocators.WEBCAM)
        element.click()

    def join(self):
        element = self.driver.find_element(*GoogleMeetJoiningPageLocators.JOIN)
        element.click()


class GoogleMeetClassPage(BasePage):

    show_chat = ShowChat()
    get_participants = GetParticipants()

    def show(self):
        element = self.driver.find_element(*GoogleMeetClassPageLocators.SHOW_CHAT)
        element.click()
