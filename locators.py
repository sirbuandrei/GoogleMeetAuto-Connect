from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    NEXT_BUTTON = (
        By.XPATH,
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
    LOGIN_BUTTON = (
        By.XPATH,
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')


class GoogleMeetPageLocators(object):
    USE_CODE = (By.XPATH, '/html/body/div[1]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]')
    CONNECT = (By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span')


class GoogleMeetJoiningPageLocators(object):
    MIC = (
        By.XPATH,
        '/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div['
        '1]/div/div/div')
    WEBCAM = (
        By.XPATH,
        '/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div['
        '2]/div/div')
    JOIN = (
        By.XPATH,
        '/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]')


class GoogleMeetClassPageLocators(object):
    LEAVE_BUTTON = (
        By.XPATH,
        '')
    SHOW_CHAT = (
        By.XPATH,
        '/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span')
