import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select
import time
class PurchaseProducts(BasePage):

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

    _my_wishlist_link = "//*[@id='top']/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[8]/a" # "//a[contains(text(),'My Wishlist')]" # //strong[contains(text(),'My Wishlist')]
    #   //a[contains(text(),'My Wishlist')]
    _add_to_cart_button = "//button[@type='button'][@title='Add to Cart'][@class='button btn-cart']" # "//tr[@id='item_45258']//span[contains(text(),'Add to Cart')]" # //tr[@id='item_45258']//span[contains(text(),'Add to Cart')]"
    _checkout_button = "//ul[@class='checkout-types top']//span[contains(text(),'Proceed to Checkout')]"

    # shipping information
    _first_name_field = "billing:firstname"  # id
    _last_nae_field = "billing:lastname"  # id
    _address_field = "billing:street1"  # id
    _city_field = "billing:city"  # id
    _state_province_field = "billing:region_id"  # id
    _zip_field = "billing:postcode"  # id
    _telephone_field = "billing:telephone"  # id
    _continue_button1 = "//div[@id='billing-buttons-container']//span[contains(text(),'Continue')]"
    _continue_button2 = "//div[@id='shipping-method-buttons-container']//button[@class='button']//span//span[contains(text(),'Continue')]"

    _flat_rate = "//span[@class='price'][contains(text(),'$5.00')]"  # enhetspris //span[contains(text(),'$10.00')]
    _money_order_radioBtn = "//label[@for='p_method_checkmo'][contains(text(),'Check / Money order')]"
    _continue_button3 = "//div[@id='payment-buttons-container']//button[@class='button']//span//span[contains(text(),'Continue')]" # "//*[@id='payment-buttons-container']/button"

    _sub_total = "//tr[@class='first']//span[@class='price'][contains(text(),'$615.00')]"
    _grand_total = "//span[contains(text(),'$620.00')]"

    _place_order_button = "//span[contains(text(),'Place Order')]"

    _order_confirmation = "//h2[@class='sub-title']"  # getText : "Thank you for your purchase!"
    _order_id = "//a[contains(text(),'100012392')]"  # getText = 100012392, i.e. not none

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

    def clickMyWishlistLink(self):
        self.elementClick(locator=self._my_wishlist_link, locatorType="xpath")
        '''
        element = self.waitForElement(locator=self._my_wishlist_link, locatorType="xpath")
        self.elementClick(element)
        '''

    def clickAddToCartBtn(self):
        self.elementClick(locator=self._add_to_cart_button, locatorType="xpath")

    def clickCheckoutBtn(self):
        self.elementClick(locator=self._checkout_button, locatorType="xpath")

    '''
    def enterFirstName(self, fname):
        self.sendKeys(fname, locator=self._first_name_field)

    def enterLastName(self, lname):
        self.sendKeys(lname, locator=self._last_nae_field)
    '''

    def enterAddress(self, address):
        self.sendKeys(address, locator=self._address_field)

    def enterCity(self, city):
        self.sendKeys(city, locator=self._city_field)

    def enterState(self):
        state = self.getElement(locator=self._state_province_field)
        sel = Select(state)
        sel.select_by_value("43")

    def enterZip(self, zip):
        self.sendKeys(zip, locator=self._zip_field)

    def enterTelephone(self, number):
        self.sendKeys(number, locator=self._telephone_field)

    def clickContinueBtn1(self):
        self.elementClick(locator=self._continue_button1, locatorType="xpath")

    def clickContinueBtn2(self):
        self.elementClick(locator=self._continue_button2, locatorType="xpath")

    def isFlatRateDisplayed(self):
        #txt = self.getText(locator=self._flat_rate, locatorType="xpath")
        #return txt
        display = self.isElementDisplayed(locator=self._flat_rate, locatorType="xpath")
        return display

    def clickMoneyOrderRadioBtn(self):
        self.elementClick(locator=self._money_order_radioBtn, locatorType="xpath")

    def clickContinueBtn3(self):
        self.elementClick(locator=self._continue_button3, locatorType="xpath")

    def getSubTotal(self):
        txt = self.getText(locator=self._sub_total, locatorType="xpath")
        return txt

    def clickPlacrOrderBtn(self):
        self.elementClick(locator=self._place_order_button, locatorType="xpath")

    def getOrderId(self):
        self.getText(locator=self._order_id, locatorType="xpath")


    def login(self, email, password):
        self.clickMyAccountLink()
        self.enterEmailAddress(email)
        self.enterEmailPaasword(password)
        self.clickLoginButton()

    def addWishlistToCart(self):
        self.clickMyWishlistLink()
        self.clickAddToCartBtn()
        self.clickCheckoutBtn()

    def enterShippingInfo(self, address, city, zip, number):
        #self.enterFirstName(fname)
        #self.enterLastName(lname)
        self.enterAddress(address)
        self.enterCity(city)
        self.enterState()
        self.enterZip(zip)
        self.enterTelephone(number)
        self.clickContinueBtn1()

    def verifyFlatRate(self):
        self.login("abc11@hotmail.com", "newpass11")
        self.addWishlistToCart()
        self.enterShippingInfo("ABC", "New York", "542896", "12345678")
        self.clickContinueBtn2()
        result = self.isFlatRateDisplayed()

        return result

    def verifyGrandTotal(self):
        self.clickMoneyOrderRadioBtn()
        self.clickContinueBtn3()
        txt = self.getText(locator=self._grand_total, locatorType="xpath")
        return txt == '$620.00'

    def orderConfirmation(self):
        self.clickPlacrOrderBtn()
        result = self.isElementDisplayed(locator=self._order_confirmation, locatorType="xpath")
        return result














