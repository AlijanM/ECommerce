import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Verify the product review mechanism

class ReviewMechanism(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _mobile_menu = "//a[contains(text(),'Mobile')]"
    _xperia_image_link = "product-collection-image-1"
    _add_reviw_link = "//a[contains(text(),'Add Your Review')]"
    _review_field = "review_field"
    _summary_field = "summary_field"
    _nickname_field = "nickname_field"
    _submit_review_button = "//span[contains(text(),'Submit Review')]"

    _user_name_field = "username"  # id
    _password_field = "login"  # id
    _login_button = "//input[@class='form-button']"  # xpath
    _popup_close_link = "//div[@id='message-popup-window']//a[@title='close']"
    _catalogue_link = "//span[contains(text(),'Catalog')]"
    _review_rating_link = "//span[contains(text(),'Reviews and Ratings')]"
    _customer_review_link = "//span[contains(text(),'Customer Reviews')]"
    _pending_review_link = "//span[contains(text(),'Pending Reviews')]"

    _sort_by_id_link = "//span[contains(text(),'ID')]"
    _comment_checkbox = "//div[@class='grid']//tr[1]//td[1]//input[1]"  # first row after _sort_by_id
    _edit_link = "//tr[1]//td[10]//a[1]"
    _select_approved = "//select[@id='status_id']"  # by visible text
    _save_review_button = "//span[contains(text(),'Save Review')]"

    _tab_class = "//ul[@class='toggle-tabs']"
    _review_tab = "//li[@class='last']//span[contains(text(),'Reviews')]"
    _your_review_title = ""



    ############################
    ### Element Interactions ###
    ############################

    def clickMobileMenu(self):
        self.elementClick(locator=self._mobile_menu, locatorType="xpath")

    def clickXperiaImage(self):
        self.elementClick(locator=self._xperia_image_link)

    def clickAddReviewLink(self):
        self.elementClick(locator=self._add_reviw_link, locatorType="xpath")

    def enterReviewField(self, review):
        self.sendKeys(review, self._review_field)

    def enterSummaryField(self, summary):
        self.sendKeys(summary, self._summary_field)

    def enterNicknameField(self, nickname):
        self.sendKeys(nickname, self._nickname_field)

    def clickSubmitButton(self):
        self.elementClick(locator=self._submit_review_button, locatorType="xpath")

    ########## login to backend and approve review ##########
    def enterUserName(self, email):
        self.sendKeys(email, locator=self._user_name_field)

    def enterPaasword(self, password):
        self.sendKeys(password, locator=self._password_field)

    def clickLoginButton(self):
        self.elementClick(locator=self._login_button, locatorType="xpath")

    def clickClosePopupWindow(self):
        self.elementClick(locator=self._popup_close_link, locatorType="xpath")

    def clickCatalogueLink(self):
        self.elementClick(locator=self._catalogue_link, locatorType="xpath")

    def clickReviewRatingLink(self):
        self.elementClick(locator=self._review_rating_link, locatorType="xpath")

    def clickCustomerReviewLink(self):
        self.elementClick(locator=self._customer_review_link, locatorType="xpath")

    def selectPendingReviewMenu(self):
        self.elementClick(locator=self._pending_review_link, locatorType="xpath")


    # def clickSortById(self):
    #     self.elementClick(locator=self._sort_by_id_link, locatorType="xpath")

    def clickCommentChekbox(self):
        self.elementClick(locator=self._comment_checkbox, locatorType="xpath")

    def clickEditLink(self):
        self.elementClick(locator=self._edit_link, locatorType="xpath")

    def selectApprovedOption(self):
        elem = self.getElement(locator=self._select_approved, locatorType="xpath")
        slc = Select(elem)
        slc.select_by_value("1")

    def clickSaveReviewButton(self):
        self.elementClick(locator=self._save_review_button, locatorType="xpath")

    def clickReviewsTab(self):
        self.getElement(locator=self._tab_class, locatorType="xpath")
        self.elementClick(locator=self._review_tab, locatorType="xpath")


        # add review (frontend)
    def addReview(self, review, summary, nickname):
        self.clickMobileMenu()
        self.clickXperiaImage()
        self.clickAddReviewLink()
        time.sleep(2)
        self.enterReviewField(review)
        self.enterSummaryField(summary)
        self.enterNicknameField(nickname)
        self.clickSubmitButton()
        return True

        # login to admin (backend)
    def loginToBackend(self, userName, password):
        url = "http://live.demoguru99.com/index.php/backendlogin"
        self.driver.get(url)
        self.enterUserName(userName)
        self.enterPaasword(password)
        self.clickLoginButton()
        self.clickClosePopupWindow()

        # navigate to customer reviews (backend)
    def navigateToPendingReviews(self):
        self.clickCatalogueLink()
        self.clickReviewRatingLink()
        self.clickCustomerReviewLink()
        self.selectPendingReviewMenu()

        # approve review (backend)
    def approveReview(self):
        # self.clickSortById()
        self.clickCommentChekbox()
        self.clickEditLink()
        self.selectApprovedOption()
        self.clickSaveReviewButton()

        # verify approved review (frontend)
    def reviewDisplayInFrontend(self):
        url = "http://live.demoguru99.com/"
        self.driver.get(url)
        self.clickMobileMenu()
        self.clickXperiaImage()
        self.clickReviewsTab()
        time.sleep(3)

        # verify
    def verifyReviewDisplay(self, review, summary, nickname, userName, password):
        self.addReview(review, summary, nickname)
        self.loginToBackend(userName, password)
        self.navigateToPendingReviews()
        self.approveReview()
        self.reviewDisplayInFrontend()

        summaryLink = "//a[contains(text(),'%s')]" % summary
        return self.isElementDisplayed(locator=summaryLink, locatorType="xpath")

