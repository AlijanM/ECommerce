import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class ProductPrices(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################

    _mobile_menu = "//a[contains(text(),'Mobile')]"
    _list_page_price = "//span[contains(text(),'$100.00')]"
    _detail_page_link = "//a[@title='Sony Xperia']"
    _detail_page_price = "//span[@class='price']"

    ############################
    ### Element Interactions ###
    ############################

    def clickMobileMenu(self):
        self.elementClick(locator=self._mobile_menu, locatorType="xpath")

    def clickDetailPageLink(self):
        self.elementClick(locator=self._detail_page_link, locatorType="xpath")

    def comparePrices(self):
        self.clickMobileMenu()
        listPrice = self.getText(locator=self._list_page_price, locatorType="xpath")
        self.clickDetailPageLink()
        detailPrice = self.getText(locator=self._detail_page_price, locatorType="xpath")

        return listPrice == detailPrice

