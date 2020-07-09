import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class DiscountCoupon(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################

    _mobile_menu = "//a[contains(text(),'Mobile')]"
    _add_to_cart_iphone_button = "//html[@id='top']/body/div[@class='wrapper']/div[@class='page']//div[@class='category-products']/ul/li[2]/div[@class='product-info']//button[@title='Add to Cart']/span/span[.='Add to Cart']"  # //span[@xpath='1'][contains(text(), 'Add to Cart')]
    _grand_total = "//strong//span[@class='price'][contains(text(),'$500.00')]"
    _discount_field = "coupon_code" #"//input[@id='coupon_code']"  # id  "coupon_code"
    _apply_discount_button = "//span[contains(text(),'Apply')]"
    _discount_amount = "//td[contains(text(),'Discount (GURU50)')]"

    ############################
    ### Element Interactions ###
    ############################

    def clickMobileMenu(self):
        self.elementClick(locator=self._mobile_menu, locatorType="xpath")

    def clickAddToCartButton(self):
        self.elementClick(locator=self._add_to_cart_iphone_button, locatorType="xpath")

    def enterDiscountField(self, code):
        #self.sendKeys(code, locator=self._discount_field, locatorType="xpath")
        self.sendKeysWhenReady(code, locator=self._discount_field)

    def clickApplyDiscountButton(self):
        self.elementClick(locator=self._apply_discount_button, locatorType="xpath")

    def getTextOnDiscount(self):
        discountElem = self.getElement(locator=self._discount_amount, locatorType="xpath")
        txt = self.getText(element=discountElem)
        return txt

    def applyDiscount(self, code):
        self.clickMobileMenu()
        self.clickAddToCartButton()
        self.enterDiscountField(code)
        self.clickApplyDiscountButton()

    def verifyAppliedDiscount(self):
        self.applyDiscount("GURU50")
        txt = self.getTextOnDiscount()

        return txt == 'DISCOUNT (GURU50)'






