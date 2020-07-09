import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select

class CreateAccount(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _my_account_link = "//div[@class='footer']//a[contains(text(),'My Account')]"

    _create_account_button = "//a[@class='button']"

    _first_name_field = "firstname"
    _last_name_field = "lastname"
    _email_address_field = "//input[@id='email_address']"
    _password_field = "//input[@id='password']"
    _confirm_password_field = "//input[@id='confirmation']"
    _register_button = "//div[@class='buttons-set']//button[@class='button']"

    _register_confirmation = "//span[contains(text(), 'Thank you for registering with Main Website Store.')]" # Verify
    _tv_page_link = "//a[contains(text(),'TV')]"

    _wishlist_link_LG = "//li[1]//div[1]//div[3]//ul[1]//li[1]//a[1]"
    _share_wishlist_button = "//span[contains(text(),'Share Wishlist')]"
    _email_address = "email_address"
    _share_wishlist_submit_button = "//button[@title='Share Wishlist']"
    _wishlist_confirmation_msg = "//span[contains(text(),'Your Wishlist has been shared.')]"  # Verify

    ############################
    ### Element Interactions ###
    ############################

    def clickMyAccountLink(self):
        self.elementClick(locator=self._my_account_link, locatorType="xpath")

    def clickCreateAccountBtn(self):
        self.elementClick(locator=self._create_account_button, locatorType="xpath")

    def enterFirstName(self, firstName):
        self.sendKeys(firstName, locator=self._first_name_field)

    def enterLastName(self, lastName):
        self.sendKeys(lastName, locator=self._last_name_field)

    def enterEmailAddress(self, email):
        self.sendKeys(email, locator=self._email_address_field, locatorType="xpath")

    def enterEmailPaasword(self, Password):
        self.sendKeys(Password, locator=self._password_field, locatorType="xpath")

    def enterConfirmPassword(self, password):
        self.sendKeys(password, locator=self._confirm_password_field, locatorType="xpath")

    def clickRegisterButton(self):
        self.elementClick(locator=self._register_button, locatorType="xpath")

    def clickTvPageLink(self):
        self.elementClick(locator=self._tv_page_link, locatorType="xpath")

    def clickWishlistLinkLG(self):
        self.elementClick(locator=self._wishlist_link_LG, locatorType="xpath")

    def clickShareWishlistButton(self):
        self.elementClick(locator=self._share_wishlist_button, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, locator=self._email_address)

    def clickShareWishlistSubmit(self):
        self.elementClick(locator=self._share_wishlist_submit_button, locatorType="xpath")

    def createAccount(self, firstName, lastName, email, password):
        self.clickMyAccountLink()
        self.clickCreateAccountBtn()
        self.enterFirstName(firstName)
        self.enterLastName(lastName)
        self.enterEmailAddress(email)
        self.enterEmailPaasword(password)
        self.enterConfirmPassword(password)
        self.clickRegisterButton()

    def verifyRegistration(self):
        result = self.isElementDisplayed(locator=self._register_confirmation, locatorType="xpath")
        return result

    def addAndShareWishlist(self, email):
        self.clickTvPageLink()
        self.clickWishlistLinkLG()
        self.clickShareWishlistButton()
        self.enterEmail(email)
        self.clickShareWishlistButton()

    def verifyWishlistShare(self):
        result = self.isElementDisplayed(locator=self._wishlist_confirmation_msg, locatorType="xpath")
        return result






