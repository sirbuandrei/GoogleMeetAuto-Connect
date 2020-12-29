from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GoogleMeetLoginElement(object):
    def __set__(self, instance, value):
        driver = instance.driver
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator))
        )
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)

    def __get__(self, instance, owner):
        driver = instance.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.locator)
        )
        element = driver.find_element_by_xpath(self.locator)
        return element.get_attribute("value")


class WaitForElement(object):
    def __set__(self, instance, value):
        driver = instance.driver
        if value == 'wait':
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.locator))
            )


class GetParticipantsElement(object):
    def __get__(self, instance, owner):
        driver = instance.driver
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator))
        )
        element = driver.find_element_by_xpath(self.locator)
        return element.get_attribute('aria-label')
