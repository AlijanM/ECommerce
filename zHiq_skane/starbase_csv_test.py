import unittest, pytest
from selenium import webdriver
from ddt import ddt, data, unpack
from zHiq_skane.read_data import getCSVData
import time

@ddt
class TestStarbase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://starbase.hiq.se/sv/login")
        self.driver.implicitly_wait(3)

    @data(*getCSVData("C:\\Users\\semc0\\Desktop\\Selenium\\POM\\zHiq_skane\\test_data.csv"))
    @unpack
    def test_starBaseLogin(self, userName, password):
        driver = self.driver
        # click on login link on the start page
        driver.find_element_by_link_text("Logga in").click()
        time.sleep(2)

        # enter user name and click on 'Next' button
        driver.find_element_by_id("i0116").send_keys(userName)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(2)

        # enter password name and click on 'Sign in' button
        driver.find_element_by_id("passwordInput").send_keys(password)
        driver.find_element_by_id("submitButton").click()
        time.sleep(2)

        # click in checkbox
        driver.find_element_by_id("KmsiCheckboxField").click()
        time.sleep(2)

        # # click on 'Yes' button
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(2)

        # click on'No' button
        # driver.find_element_by_id("idBtn_Back").click()

        # finding consultant'same
        consultantName = driver.find_element_by_xpath("//h4[contains(text(),'Alijan Momeni')]").text
        note = "Lis of " + consultantName + "'s competences:"

        # click on 'Översikt' tab
        driver.find_element_by_xpath("//span[@class='text'][contains(text(),'Översikt')]").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)

        path = "C:\\Users\\semc0\\Desktop\\TestReport\\ListOfCompetences.txt"
        outFile = open(path, "a")
        outFile.write(note + "\n")

        # finding 'Kompetenser' section
        competences = driver.find_elements_by_xpath("//section[@id='personal']//span[@class='ng-star-inserted']")
        for competence in competences:
            competenceLabel = competence.text
            # print(elemText.replace(' ', ''))
            outFile.write(" " + competenceLabel.replace(' ', ''))
            # outFile.write("\n")
        outFile.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)