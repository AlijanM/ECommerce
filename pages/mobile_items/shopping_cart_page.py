import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class ShoppingCart(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################

    _mobile_menu = "//a[contains(text(),'Mobile')]"
    _add_to_cart_button = "//li[1]//div[1]//div[3]//button[1]//span[1]//span[1]"  # //span[@xpath='1'][contains(text(), 'Add to Cart')]
    _quantity_field = "//input[@type='text'][@title='Qty']"  # xpath
    _update_button = "//button[@class='button btn-update']//span[contains(text(),'Update')]"
    _error_msg = "//p[@class='item-msg error'][contains(text(), 'The maximum quantity allowed for purchase is 500.')]"
    _empty_cart_link = "//span[contains(text(),'Empty Cart')]"
    _empty_cart_msg = "//h1[contains(text(),'Shopping Cart is Empty')]"

    ############################
    ### Element Interactions ###
    ############################

    def clickMobileMenu(self):
        self.elementClick(locator=self._mobile_menu, locatorType="xpath")

    def clickAddToCartButton(self):
        self.elementClick(locator=self._add_to_cart_button, locatorType="xpath")

    def enterQuantity(self, number):
        self.sendKeys(number, locator=self._quantity_field, locatorType="xpath")

    def clickUpdateButton(self):
        self.elementClick(locator=self._update_button, locatorType="xpath")

    def clickEmptyCartLink(self):
        self.elementClick(locator=self._empty_cart_link, locatorType="xpath")

    def generateErrorMsg(self, number):
        self.clickMobileMenu()
        self.clickAddToCartButton()
        self.enterQuantity(number)
        self.clickUpdateButton()

    def verifyErrorMsg(self):
        self.generateErrorMsg(number=1000)
        result = self.isElementDisplayed(locator=self._error_msg, locatorType="xpath")
        return result

    def verifyEmptyCart(self):
        self.clickEmptyCartLink()
        result = self.isElementDisplayed(locator=self._empty_cart_msg, locatorType="xpath")
        return result








