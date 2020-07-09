import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select
import time
import os
# Export all Orders in csv file and display these information in console and you are able to send this file to another
# email id as attachment. page link: http://live.demoguru99.com/index.php/backendlogin/
# credentials: id = "user01" pass = "guru99com"

class PrintInvoice(BasePage):

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

    _status_field = "sales_order_grid_filter_status"  # id
    _search_button = "//span[contains(text(),'Search')]"  # xpath
    _canceled_order_checkbox = "//input[@type='checkbox'][@value='12324']"  # xpath  //table[@id='sales_order_grid_table']/tbody/tr[1]/td[1]/input
    _complete_order_checkbox = "//table[@id='sales_order_grid_table']//input[@type='checkbox'][@name='order_ids'][@value='5']"  # //input[@name='order_ids']
    _actions_field = "sales_order_grid_massaction-select"  # id
    _submit_button = "//span[contains(text(),'Submit')]"  # xpath

    _error_msg = "//li[@class='error-msg']//span[contains(text(),'There are no printable documents related to selected orders.')]"

    ## problem: all elements are found but no popup is displayed when clicking on _export_button in the last steps ##

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

    def selectOrderStatus(self, index1):
        # element = self.waitForElement(locator=self._export_box, locatorType="xpath")
        element = self.getElement(locator=self._status_field)
        slct = Select(element)
        slct.select_by_index(index1)  # "Canceled"
        # slct.select_by_visible_text(visibleText)  # "Excel XML"

    def clickSearchButton(self):
        self.elementClick(locator=self._search_button, locatorType="xpath")

    def clickCanceledOrderCheckBox(self):
        # self.elementClick(locator=self._order_checkbox, locatorType="xpath")
        #elem = self.waitForElement(locator=self._order_checkbox, locatorType="xpath")
        self.elementClick(locator=self._canceled_order_checkbox, locatorType="xpath")

    def clickCompleteOrderCheckBox(self):
        # self.elementClick(locator=self._order_checkbox, locatorType="xpath")
        #elem = self.waitForElement(locator=self._order_checkbox, locatorType="xpath")
        self.elementClick(locator=self._complete_order_checkbox, locatorType="xpath")

    def selectActionType(self, index2):
        # element = self.waitForElement(locator=self._export_box, locatorType="xpath")
        element = self.getElement(locator=self._actions_field)
        slct = Select(element)
        slct.select_by_index(index2)  # "4"
        # slct.select_by_visible_text(visibleText)  # "Excel XML"

    def clickSubmitButton(self):
        self.elementClick(locator=self._submit_button, locatorType="xpath")

    def login(self, userName, password):
        self.enterUserName(userName)
        self.enterPaasword(password)
        self.clickLoginButton()

    def printCanceledInvoice(self, index1, index2):
        self.clickSalesLink()
        self.clickOdersLink()
        self.selectOrderStatus(index1)
        self.clickSearchButton()
        self.clickCanceledOrderCheckBox()
        self.selectActionType(index2)
        self.clickSubmitButton()

    def printCompletedInvoice(self, index1, index2):
        self.selectOrderStatus(index1)  # '3'
        self.clickSearchButton()
        self.clickCompleteOrderCheckBox()
        self.selectActionType(index2)
        self.clickSubmitButton()


    def verifyErrorMsg(self, userName, password, index1, index2):
        self.login(userName, password)
        self.clickClosePopupWindow()
        time.sleep(2)
        self.printCanceledInvoice(index1, index2)
        # verify if error message is shown
        result = self.isElementDisplayed(locator=self._error_msg, locatorType="xpath")

        return result

    def verifyinvoiceDownload(self, index1, index2):
        self.printCompletedInvoice(index1, index2)
        #fname = 'invoice'
        x = 0
        while x < 10:
            for fname in os.listdir('C:\\Users\\semc0\\Downloads'):
                if fname.startswith("invoice"):
                    result = True
                    break
                else:
                    time.sleep(2)
                    x += 2
            else:
                result = False

            return result


