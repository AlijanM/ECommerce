import utilities.custom_logger as cl
from utilities.util import Util
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select
import time
import os
# Verify Sort is working correctly

class SortInvoice(BasePage):

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
    _invoices_link = "//span[contains(text(),'Invoices')]"
    _invoice_date_link = "//span[contains(text(),'Invoice Date')]"


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

    def clickInvoicesLink(self):
        self.elementClick(locator=self._invoices_link, locatorType="xpath")

    def clickInvoiceDateLink(self):
        self.elementClick(locator=self._invoice_date_link, locatorType="xpath")

    def login(self, email, password):
        self.enterUserName(email)
        self.enterPaasword(password)
        self.clickLoginButton()

    def navigateToInvoices(self):
        self.clickClosePopupWindow()
        self.clickSalesLink()
        self.clickInvoicesLink()
        #self.clickInvoiceDateLink()

    def sortByDate(self):
        dateList = []
        n = 1
        elemList = self.getElementList(locator="//table[@id='sales_invoice_grid_table']/tbody/tr", locatorType="xpath")
        # for n in range(1, len(elemList)+1):
        for n in range(1, len(elemList)-3):
            invoiceDateLocator = "//table[@id='sales_invoice_grid_table']/tbody/tr[%d]/td[3]" % n
            invoiceDate = self.getText(locator=invoiceDateLocator, locatorType="xpath")
            dateList.append(invoiceDate)
        print(dateList)
        return dateList

    def verifyInvoiceSort(self):
       #lst = ['Mar 6, 2020 5:56:50 PM', 'Jan 28, 2020 11:38:27 PM', 'Dec 12, 2019 9:20:18 AM', 'Jun 16, 2019 9:14:09 AM', 'Jun 16, 2019 7:17:25 AM', 'May 26, 2019 10:41:18 AM', 'May 4, 2017 7:41:10 AM', 'Aug 23, 2014 7:12:37 AM', 'Aug 23,2014 1:16:55 AM', 'Aug 23, 2014 1:11:57 AM', 'Aug 23, 2014 12:48:09 AM', 'Aug 23, 2014 12:25:57 AM']
        lst = ['Mar 6, 2020 5:56:50 PM', 'Jan 28, 2020 11:38:27 PM', 'Dec 12, 2019 9:20:18 AM', 'Jun 16, 2019 9:14:09 AM', 'Jun 16, 2019 7:17:25 AM', 'May 26, 2019 10:41:18 AM', 'May 4, 2017 7:41:10 AM', 'Aug 23, 2014 7:12:37 AM']
        self.login("user01", "guru99com")
        self.navigateToInvoices()
        dateList = self.sortByDate()

        # #result = Util().verifyListMatch(lst, dateList)
        # result = Util().verifyListContains(lst, dateList)
        # print(result)

        return dateList == lst