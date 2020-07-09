import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select
import time

# Verify you are able to change or reorder previously added product
# preconditions:
# 1. Update locator _reorder_link with an existing order in status pending, create such an order otherwise
# 2. Modify, if needed, number of reorder item in self.changingQuantity("20"), which is now '20'
#
class ChangePlacedOrder(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _my_account_link = "//div[@class='footer']//a[contains(text(),'My Account')]"

    _email_address_field = "email"  # id
    _password_field = "pass"  # id
    _login_button = "send2"  # id

    _grand_total_current = "//strong/span[@class='price']"  # verify '$620.00'

    _reorder_link = "//tr[@class='last odd']//a[@class='link-reorder'][contains(text(),'Reorder')]"  # current order 100012396
                #   "//tr[@class='first odd']//a[@class='link-reorder'][contains(text(),'Reorder')]"

    _qty_field =  "//*[@id='shopping-cart-table']/tbody/tr/td[4]/input"  # "cart[135209][qty]"  # "//*[@id='shopping-cart-table']/tbody/tr/td[4]/input" # send '5'
    _qty_update_button = "//button[@type='submit'][@name='update_cart_action'][@title='Update']" # click
                    # "//*[@id='shopping-cart-table']/tbody/tr/td[4]/input"

    _state_selection = "region_id"  # id  # select
    _select_state_by_name = "New York"  # select
    _zip_field = "postcode"  # id send , send 542896

    _estimate_link = "//span[contains(text(),'Estimate')]"
    _flat_rate_radio_btn = "//label[contains(text(),'Fixed')]" # select
    _update_total_link = "//span[contains(text(),'Update Total')]" # click

    _grand_total_new = "//strong/span[@class='price']" # verify amount

    _checkout_button = "//ul[@class='checkout-types bottom']//button[@type='button']//span[contains(text(),'Proceed to Checkout')]" # click
                     # "//ul[@class='checkout-types bottom']//button[@type='button']//span[contains(text(),'Proceed to Checkout')]"
                     # "//*[@id="top"]/body/div/div/div[2]/div/div/div/div[3]/div/ul/li[1]/button/span/span"
                    # //*[@id="top"]/body/div/div/div[2]/div/div/div/div[3]/div/ul/li[1]/button/span/span

    _continue_shipping_info = "//div[@id='billing-buttons-container']//button[@class='button']//span//span[contains(text(),'Continue')]" # click
    _continue_shipping_method = "//html[@id='top']//div[@id='shipping-method-buttons-container']/button/span/span[.='Continue']"
    #                           "/html/body/div/div/div[2]/div/div[1]/ol/li[3]/div[2]/form/div[3]/button/span/span"

    _money_order = "//label[contains(text(),'Check')]" # select
    _continue_payment_info = "//div[@id='payment-buttons-container']//button[@class='button']//span//span[contains(text(),'Continue')]" # click
                            # "//*[@id="payment-buttons-container"]/button/span/span"
                            # //div[@id='payment-buttons-container']//button[@class='button']//span//span[contains(text(),'Continue')]

    _place_order_button = "//span[contains(text(),'Place Order')]"

    _new_order_confirmation = "//h1[contains(text(),'Your order has been received.')]"
    _new_purchase_confirmation = "//h2[@class='sub-title']"  # Verify "Thank you for your purchase!"
    _new_order_number = "//a[contains(text(),'100012404')]" # verify


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

    def getCurrentGrandTotal(self):
        cgt = self.getText(locator=self._grand_total_current, locatorType="xpath")
        return cgt

    def clickReorderLink(self):
        self.elementClick(locator=self._reorder_link, locatorType="xpath")

    def enterQuantityField(self, quantity):
        self.getElement(locator=self._qty_field, locatorType="xpath").clear()
        self.sendKeys(quantity, locator=self._qty_field, locatorType="xpath")

    def clickUpdateQuntityBtn(self):
        self.elementClick(locator=self._qty_update_button, locatorType="xpath")

    def selectState(self, value):
        element = self.getElement(locator=self._state_selection)
        slct = Select(element)
        slct.select_by_value(value)

    def enterZipField(self, zip):
        self.getElement(locator=self._zip_field).clear()
        self.sendKeys(zip, locator=self._zip_field)

    def clickEstimateLink(self):
        self.elementClick(locator=self._estimate_link, locatorType="xpath")

    def clickFaltRateRadio(self):
        self.elementClick(locator=self._flat_rate_radio_btn, locatorType="xpath")

    def clickUpdateTotalLink(self):
        self.elementClick(locator=self._update_total_link, locatorType="xpath")

    def getNewGrandTotal(self):
        ngt = self.getText(locator=self._grand_total_new, locatorType="xpath")
        return ngt

    def clickCheckoutBtn(self):
        self.elementClick(locator=self._checkout_button, locatorType="xpath")

    def clickContinueShippingInfo(self):
        self.elementClick(locator=self._continue_shipping_info, locatorType="xpath")

    def clickContinueShippingMethod(self):
        self.elementClick(locator=self._continue_shipping_method, locatorType="xpath")

    def clickPaymentMethod(self):
        self.elementClick(locator=self._money_order, locatorType="xpath")

    def clickContinuePaymentInfo(self):
        self.elementClick(locator=self._continue_payment_info, locatorType="xpath")

    def clickPalceOrderBtn(self):
        self.elementClick(locator=self._place_order_button, locatorType="xpath")

    def getNewOrderConfirmation(self):
        txt = self.getText(locator=self._new_order_confirmation, locatorType="xpath")
        return txt

    def getPurchaseConfirmation(self):
        txt = self.getText(locator=self._new_purchase_confirmation, locatorType="xpath")
        return txt

    '''
    def isReOrderNumberDisplayed(self):
        result = self.isElementDisplayed(locator=self._new_order_number, locatorType="xpath")
        return result
    '''


    def login(self, email, password):
        self.clickMyAccountLink()
        self.enterEmailAddress(email)
        self.enterEmailPaasword(password)
        self.clickLoginButton()

    def changingQuantity(self, number):
        self.enterQuantityField(number)
        self.clickUpdateQuntityBtn()

    def estimatingNewGrandTotal(self, value, zip):  # "Now Yourk"  , 542896
        self.clickReorderLink()
        self.changingQuantity()
        # self.selectState(value)
        # self.enterZipField(zip)
        # self.clickEstimateLink()
        # self.clickFaltRateRadio()
        # self.clickUpdateTotalLink()

    def shippingInformation(self):
        self.clickContinueShippingInfo()
        time.sleep(2)
        self.clickContinueShippingMethod()
        time.sleep(2)
        self.clickPaymentMethod()
        time.sleep(2)
        self.clickContinuePaymentInfo()
        time.sleep(2)
        self.clickPalceOrderBtn()

    def verifyCurrentGrandTotals(self):
        self.login("abc11@hotmail.com", "newpass11")
        self.clickReorderLink()
        time.sleep(3)
        cgt = self.getCurrentGrandTotal()
        self.changingQuantity("20")
        #self.estimatingNewGrandTotal("43", "542896")
        ngt = self.getNewGrandTotal()
        self.clickCheckoutBtn()
        return cgt != ngt

    def verifyNewOrderConfirmation(self):
        # time.sleep(3)
        # self.clickCheckoutBtn()
        self.shippingInformation()
        result = self.getNewOrderConfirmation()
        return result == "YOUR ORDER HAS BEEN RECEIVED."

    def verifyNewPurchaseConfirmation(self):
        result = self.getPurchaseConfirmation()
        return result == "THANK YOU FOR YOUR PURCHASE!"

















