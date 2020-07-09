import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

# Verify you can create an account in e-Commerce site and can share wishlist to other poeple using email.
class CompareProducts(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################

    _mobile_menu = "//a[contains(text(),'Mobile')]"
    _compare_link_sony =   "//li[1]//div[1]//div[3]//ul[1]//li[2]//a[1]" # //ul[@class='add-to-links'][@xpath='1']
    _compare_link_iphone = "//li[2]//div[1]//div[3]//ul[1]//li[2]//a[1]"
    _compare_button = "//button[@class='button']//span//span[contains(text(),'Compare')]"
    _popup_window = ""
    _sony_link = "//img[@alt='Sony Xperia']"
    _iphone_link = "//img[@alt='IPhone']"
    _close_popup_window = "//button[@title='Close Window']"


    ############################
    ### Element Interactions ###
    ############################

    def clickMobileMenu(self):
        self.elementClick(locator=self._mobile_menu, locatorType="xpath")

    def clickCompareLinkSony(self):
        self.elementClick(locator=self._compare_link_sony, locatorType="xpath")

    def clickCompareLinkIphone(self):
        self.elementClick(locator=self._compare_link_iphone, locatorType="xpath")

    def clickCompareButton(self):
        self.elementClick(locator=self._compare_button, locatorType="xpath")

    def closePopupWindow(self):
        self.elementClick(locator=self._close_popup_window, locatorType="xpath")


    def compareProducts(self):
        self.clickMobileMenu()
        parentHandle = self.driver.current_window_handle
        self.clickCompareLinkSony()
        self.clickCompareLinkIphone()
        self.clickCompareButton()

        Handles = self.driver.window_handles
        print(Handles)
        for handle in Handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                self.driver.maximize_window()
        # self.driver.switch_to.window(parentHandle)

    def verifyComparison(self):
        self.compareProducts()
        result1 = self.getElement(locator=self._sony_link, locatorType="xpath").is_displayed()
        result2 = self.getElement(locator=self._iphone_link, locatorType="xpath").is_displayed()

        return result1 and result2








