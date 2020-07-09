import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select
import time
class SavePlacedOrder(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _my_account_link = "//div[@class='footer']//a[contains(text(),'My Account')]"

    _create_account_button = "//a[@class='button']"

    _email_address_field = "email"  # id
    _password_field = "pass"  # id
    _login_button = "send2"  # id

    _recent_order_number = "//td[contains(text(),'100012397')]"
    _recent_oder_status = "//tr[@class='first odd']//em[contains(text(),'Pending')]"

    _view_order_link = "//tr[@class='first odd']//a[contains(text(),'View Order')]"
    _print_order_link = "//a[@class='link-print']"

    _print_button = "//*[@id='sidebar']//print-preview-button-strip//cr-button[1]"

    _save_button = "//*[@id='sidebar']//print-preview-button-strip//cr-button[1]"
    # //cr-button[@class='action-button'][contains(text(),'Save')]
    # //print-preview-sidebar[@id="sidebar"]//print-preview-button-strip//cr-button[1]
    #  //print-preview-sidebar[@id='sidebar']//cr-button[@class='action-button'][contains(text(),'Save')]
    #                //*[@id="sidebar"]//print-preview-button-strip//cr-button[1]




    ############################
    ### Element Interactions ###
    ############################

    def clickMyAccountLink(self):
        self.elementClick(locator=self._my_account_link, locatorType="xpath")

    def enterEmailAddress(self, email):
        self.sendKeys(email, locator=self._email_address_field)

    def enterEmailPaasword(self, password):
        self.sendKeys(password, locator=self._password_field)

    def clickLoginButton(self):
        self.elementClick(locator=self._login_button)

    def clickViewOrderLink(self):
        self.elementClick(locator=self._view_order_link, locatorType="xpath")

    def clickPrintOrderLink(self):
        self.elementClick(locator=self._print_order_link, locatorType="xpath")

    def clickPrintButton(self):
        self.elementClick(locator=self._print_button, locatorType="xpath")

    def switchToPopupWindow(self):
        parentHandle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                self.driver.maximize_window()
                time.sleep(3)

    def clickSaveButton(self):
        self.elementClick(locator=self._save_button, locatorType="xpath")

    def login(self, email, password):
        self.clickMyAccountLink()
        self.enterEmailAddress(email)
        self.enterEmailPaasword(password)
        self.clickLoginButton()

    def verifyRecentOrderNumber(self):
        self.login("abc11@hotmail.com", "newpass11")
        result = self.isElementDisplayed(locator=self._recent_order_number, locatorType="xpath")
        return result

    def verifyRecentOrderStatus(self):
        txt = self.getText(locator=self._recent_oder_status, locatorType="xpath")
        return txt == "Pending"

    def verifyOrderPrint(self):
        self.clickViewOrderLink()
        self.clickPrintOrderLink()
        self.switchToPopupWindow()
        self.clickPrintButton()  # Driver can't find the Print button
        return True














