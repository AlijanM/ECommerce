from selenium import webdriver
import unittest
import time

class CvDataBase(unittest.TestCase):

    def test_Competences(self):
        baseUrl = "https://starbase.hiq.se/sv/login"
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # click on login link on the start page
        driver.find_element_by_link_text("Logga in").click()
        time.sleep(2)

        # enter user name and click on 'Next' button
        driver.find_element_by_id("i0116").send_keys("alijan.momeni@hiq.se")
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(2)

        # enter password name and click on 'Sign in' button
        driver.find_element_by_id("passwordInput").send_keys("Hiq2020?")
        driver.find_element_by_id("submitButton").click()
        time.sleep(2)

        # click on checkbox
        driver.find_element_by_id("KmsiCheckboxField").click()
        time.sleep(2)

        # # click on 'Yes' button
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(2)

        # click on'No' button
        # driver.find_element_by_id("idBtn_Back").click()

        # click on 'Översikt' tab
        # //span[@class='text'][contains(text(),'Översikt')]
        driver.find_element_by_xpath("//a[@id='navCv']/span[@class='text']").click()

        # click on'No'
        #driver.find_element_by_id("idBtn_Back").click()

        # finding 'Kompetenser' section
        listOfElements = driver.find_elements_by_xpath("//section[@id='personal']//span[@class='ng-star-inserted']")
        for element in listOfElements:
            elemText = element.text
            print(elemText)


        txt = driver.title
        print("The title of the page is:", txt)
        time.sleep(10)

        driver.close()

cdb = CvDataBase()
cdb.test_Competences()

'''
1. How to clear cache/cookies before or after each login
2. How to ignore ',' and ' ' in the competence list
3. How to print the competences to a file in different supported format

'''