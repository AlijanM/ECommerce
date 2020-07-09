from selenium import webdriver
import unittest
import time

# Search: it works fine for competence search, e.g. "Python", "Selenium" or "Alijan Momeni", "*", ""...
# Filter: not implemented yet

class CvDataBase(unittest.TestCase):

        # setup web browser
    def browserSetUp(self):
        baseUrl = "https://starbase.hiq.se/sv/login"
        self.driver = webdriver.Chrome("C:\\drivers\\chromedriver.exe")  # Chrome browser
        # self.driver = webdriver.Ie("C:\\drivers\\IEDriverServer.exe")  # IE browser
        # self.driver = webdriver.Firefox(executable_path="C:\\drivers\\geckodriver.exe")  # Firefox browser
        self.driver.maximize_window()
        self.driver.get(baseUrl)
        self.driver.implicitly_wait(3)

        # login with user email and password
    def userLogin(self, email, password):
        # click on login link on the start page
        self.driver.find_element_by_link_text("Logga in").click()

        # enter user name and click on 'Next' button
        self.driver.find_element_by_id("i0116").send_keys(email)
        self.driver.find_element_by_id("idSIButton9").click()

        # enter password name and click on 'Sign in' button
        self.driver.find_element_by_id("passwordInput").send_keys(password)
        self.driver.find_element_by_id("submitButton").click()

        # click on checkbox
        self.driver.find_element_by_id("KmsiCheckboxField").click()

        # click on 'Yes' button
        self.driver.find_element_by_id("idSIButton9").click()

        # click on'No' button
        # driver.find_element_by_id("idBtn_Back").click()

        self.driver.find_element_by_xpath("//span[@class='oi oi-x']").click()

        # enter searchText and click on Search button
    def searchFunction(self, searchText):
        # click on Search icon
        self.driver.find_element_by_xpath("//span[contains(text(),'Sök')]").click()

        # search field
        xpath = "//div[@class='search__input']/input[@type='text']"
        self.driver.find_element_by_xpath(xpath).send_keys(searchText)
        self.driver.find_element_by_xpath("//span[@class='search'][contains(text(),'Sök')]").click()

        # click on "Load More" button until all search result, if more than one page, is downloaded
    def downloadSearchResult(self):
        loadMoreButton = "//button[@class='btn btn-primary']"
        while True:
            try:
                self.driver.execute_script("window.scrollTo(0, 1000)")
                time.sleep(2)
                self.driver.find_element_by_xpath(loadMoreButton).click()
            except:
                print("End of the competence list.")
                break

        # write competences to outFile
    def writeResultToTextFile(self):
        outFilePath = "C:\\Users\\AlijanMo\\Desktop\\TestReport\\ListOfCompetences.txt"
        outFile = open(outFilePath, "a")

        # get number of consultant(s) matching search criteria
        foundConsultants = self.driver.find_elements_by_xpath("//div[@class='card mb-4 box-shadow employee-summary']")
        outFile.write("########### Found %d consultant(s) ########## \n" % len(foundConsultants))
        for x in range(1, len(foundConsultants) + 1):
            consultantXpath = "//div[@id='employeeCard%d']//strong" % x
            consultant = self.driver.find_element_by_xpath(consultantXpath).text
            outFile.write(consultant + ":" + "\n")

            # get each consultant's competences
            consultantCompetences = "//div[@id='employeeCard%d']//span[@class='competence-name pr-2 ng-star-inserted']" % x
            competences = self.driver.find_elements_by_xpath(consultantCompetences)
            for competence in competences:
                competenceLabel = competence.text
                outFile.write(" " + competenceLabel.replace(' ', ''))

            outFile.write("\n\n")
        outFile.close()

    def filterFunction(self):
        # click Bolag field
        self.driver.find_element_by_xpath("//div[@class='ng-input']//input").click()
        # select HiqSkåne
        pass

    def searchResult(self, username, password, searchText):
        self.browserSetUp()
        self.userLogin(username, password)
        self.searchFunction(searchText)
        self.downloadSearchResult()
        self.writeResultToTextFile()

username = "alijan.momeni@hiq.se"
password = "Hiq2020?"
searchText = "*"

cdb = CvDataBase()
cdb.searchResult(username, password, searchText)

# How to Run this script in prompt terminal:
# 1. Download Python and web driver(s) for web browser(s)
# 2. Add path to Python and web driver(s) in sys environment variable
# 3. Change web driver and outFilePath, if required
# 4. provide username, password and searchText
# 5. Navigate to the testfile.py location
# 6. Enter: python testfile.py
# 7. Press Enter