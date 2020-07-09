from selenium import webdriver
import unittest
import time

# due to click on "Load more ..." button
# it works fine for competence search, e.g. "Python", "Selenium" but not "Alijan Momeni"

class CvDataBase(unittest.TestCase):

    def browserSetUp(self):
        baseUrl = "https://starbase.hiq.se/sv/login"
        self.driver = webdriver.Chrome("C:\\drivers\\chromedriver.exe")
        # self.driver = webdriver.Ie("C:\\drivers\\IEDriverServer.exe")
        # self.driver = webdriver.Firefox(executable_path="C:\\drivers\\geckodriver.exe")
        self.driver.maximize_window()
        self.driver.get(baseUrl)
        self.driver.implicitly_wait(3)

    def test_userLogin(self, email, password):
        # click on login link on the start page
        self.driver.find_element_by_link_text("Logga in").click()
        time.sleep(2)

        # enter user name and click on 'Next' button
        self.driver.find_element_by_id("i0116").send_keys(email)
        self.driver.find_element_by_id("idSIButton9").click()
        time.sleep(2)

        # enter password name and click on 'Sign in' button
        self.driver.find_element_by_id("passwordInput").send_keys(password)
        self.driver.find_element_by_id("submitButton").click()
        time.sleep(2)

        # click on checkbox
        self.driver.find_element_by_id("KmsiCheckboxField").click()
        time.sleep(2)

        # click on 'Yes' button
        self.driver.find_element_by_id("idSIButton9").click()
        time.sleep(2)

        # click on'No' button
        # driver.find_element_by_id("idBtn_Back").click()

        self.driver.find_element_by_xpath("//span[@class='oi oi-x']").click()

    def test_searchCompetences(self, textToSearch=""):
        # click on Search icon tab
        self.driver.find_element_by_xpath("//span[contains(text(),'Sök')]").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)

        # search field
        xpath = "//div[@class='search__input']/input[@type='text']"
        self.driver.find_element_by_xpath(xpath).send_keys(textToSearch)
        self.driver.find_element_by_xpath("//span[@class='search'][contains(text(),'Sök')]").click()

        # moreButton = self.driver.find_element_by_xpath("//button[@class='btn btn-primary']")
        # visible = True
        while True:
            self.driver.execute_script("window.scrollTo(0, 1000)")
            loadMoreButton = self.driver.find_element_by_xpath("//button[@class='btn btn-primary']")
            try:
                time.sleep(1)
                loadMoreButton.click()
            except:
                print("Element not found")
                break

        # write competences to file
        path = "C:\\Users\\AlijanMo\\Desktop\\TestReport\\ListOfCompetences.txt"
        outFile = open(path, "a")
        # outFile.write(note+"\n")
        competences = self.driver.find_elements_by_xpath("//span[@class='competence-name pr-2 ng-star-inserted']")

        # find numberOfFoundConsultants by driver.find_elements_by_xpath("//div[@class='card mb-4 box-shadow employee-summary']")

        foundConsultants = self.driver.find_elements_by_xpath("//div[@class='card mb-4 box-shadow employee-summary']")
        for x in range(1, len(foundConsultants) + 1):
            consultantXpath = "//div[@id='employeeCard%s']//strong" % int(x)
            consultant = self.driver.find_element_by_xpath(consultantXpath).text
            outFile.write(consultant + ":" + "\n")

            # find competences by driver.find_elements_by_xpath("//div[@id='employeeCard%s']//span[@class='competence-name pr-2 ng-star-inserted']")
            consultantCompetences = "//div[@id='employeeCard%s']//span[@class='competence-name pr-2 ng-star-inserted']" % int(x)
            competences = self.driver.find_elements_by_xpath(consultantCompetences)
            for competence in competences:
                competenceLabel = competence.text
                # print(elemText.replace(' ', ''))
                outFile.write(" " + competenceLabel.replace(' ', ''))

            outFile.write("\n\n")
        outFile.close()

    def test_filterCompetences(self):
        # click Bolag field
        self.driver.find_element_by_xpath("//div[@class='ng-input']//input").click()
        # select HiqSkåne

        pass

    def test_listOfCompetences(self):
        self.browserSetUp()
        self.test_userLogin("alijan.momeni@hiq.se", "Hiq2020?")  # "alijan.momeni@hiq.se", "Hiq2020?"
        self.test_searchCompetences("Python")  # "Alijan Momeni"

cdb = CvDataBase()
cdb.test_listOfCompetences()

'''
1. How to clear cache/cookies before or after each login
2. How to ignore ',' and ' ' in the competence list
3. How to print the competences to a file in different supported format
4. Scroll down arfter finding "Översikt" page

'''