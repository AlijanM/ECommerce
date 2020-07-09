import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _user_id_field = "uid"  # id
    _password_field = "//input[@name='password']"  # xpath
    _login_button = "btnLogin"  # name
    _successful_login_msg = "//td[contains(text(),'Manger Id : mngr263185')]"
    _logou_linElement = "//a[contains(text(),'Log out')]"

    def enterEmail(self, email):
        self.getElement(self._user_id_field, locatorType="name").clear()
        self.sendKeys(email, self._user_id_field, locatorType="name")

    def enterPassword(self, password):
        self.getElement(self._password_field, locatorType="xpath").clear()
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._successful_login_msg, locatorType="xpath")
        return result


    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(self._logou_linElement,
                          locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)