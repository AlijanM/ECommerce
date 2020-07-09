import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select

class SortByName(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _home_page_text = "//h2[contains(text(),'This is demo site for')]"
    _mobile_menu = "//a[contains(text(),'Mobile')]"
    _mobile_page_title = "//h1[contains(text(),'Mobile')]"
    _list_of_items = "//a[@class='product-image']"  # or "//li[@class='item last']"
    _sorting_box = "//div[@class='toolbar-bottom']//select[@onchange='setLocation(this.value)'][@title='Sort By']"

    ############################
    ### Element Interactions ###
    ############################

    def verifyTextOnHomePage(self):
        result = self.isElementDisplayed(locator=self._home_page_text, locatorType="xpath")
        return result

    def clickMobileMenu(self):
        self.elementClick(locator=self._mobile_menu, locatorType="xpath")

    def verifyMobilePageTitle(self, txt):
        self.clickMobileMenu()
        result = self.verifyPageTitle(txt)
        return result

    def verifySortByName(self):
        dropdownBox = self.getElement(locator=self._sorting_box, locatorType="xpath")
        slc = Select(dropdownBox)
        # slc.select_by_value("http://live.demoguru99.com/index.php/mobile.html?dir=asc&order=name")
        # slc.select_by_index(1)
        slc.select_by_visible_text("Name")

        # verify items are sorted by name - by taking screenshot of items after sorting
        destinationFileName = "C:\\Users\\semc0\\Desktop\\Guru99\\Screenshot_itemsSortedByName.png"
        self.driver.save_screenshot(destinationFileName)

        # verify items are sorted by name - by comparing list of items after sorting
        items = self.getElementList(locator=self._list_of_items, locatorType="xpath")
        actualList = []
        tempList = []
        for item in items:
            mobileNames = item.get_attribute("title")
            actualList.append(mobileNames)
        # print("Actual list is:", actualList)

        for item in actualList:
            tempList.append(item)
        tempList.sort()

        return actualList == tempList
