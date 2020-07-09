import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select
import time

# Export all Orders in csv file and display these information in console and
# you are able to send this file to another email id as attachment


class ExportOrdersToFile(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################

    _user_name_field = "username"  # id
    _password_field = "login"  # id
    _login_button = "//input[@class='form-button']"  # xpath

    _popup_close_link = "//div[@id='message-popup-window']//a[@title='close']"

    _sales_link = "//span[contains(text(),'Sales')]"
    _order_link = "//span[contains(text(),'Orders')]"

    _export_box = "//select[@id='sales_order_grid_export']"
    _csv_displayed_text = "CSV"
    _export_button = "//span[contains(text(),'Export')]"


    ############################
    ### Element Interactions ###
    ############################

    def enterUserName(self, email):
        self.sendKeys(email, locator=self._user_name_field)

    def enterPaasword(self, password):
        self.sendKeys(password, locator=self._password_field)

    def clickLoginButton(self):
        self.elementClick(locator=self._login_button, locatorType="xpath")

    def clickClosePopupWindow(self):
        self.elementClick(locator=self._popup_close_link, locatorType="xpath")

    def clickSalesLink(self):
        self.elementClick(locator=self._sales_link, locatorType="xpath")

    def clickOdersLink(self):
        self.elementClick(locator=self._order_link, locatorType="xpath")

    def selectFileType(self, visibleText):
        # element = self.waitForElement(locator=self._export_box, locatorType="xpath")
        element = self.getElement(locator=self._export_box, locatorType="xpath")
        slct = Select(element)
        slct.select_by_visible_text(visibleText)  # "CSV"
        # slct.select_by_visible_text(visibleText)  # "Excel XML"


    def clickExportButton(self):
        self.elementClick(locator=self._export_button, locatorType="xpath")

    def login(self, userName, password):
        self.enterUserName(userName)
        self.enterPaasword(password)
        self.clickLoginButton()

    def exportToFile(self, visibleText):
        self.clickSalesLink()
        self.clickOdersLink()
        time.sleep(3)
        self.selectFileType(visibleText)
        self.clickExportButton()


    def validFileExport(self, userName, password, visibleText):
        self.login(userName, password)
        self.clickClosePopupWindow()
        time.sleep(2)
        self.exportToFile(visibleText)
        # click Export button
        exportElement = self.waitForElement(locator=self._export_button, locatorType="xpath")
        self.elementClick(element=exportElement)
        if exportElement is None:
            result = False
        else:
            result = True
        return result


