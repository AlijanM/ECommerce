from selenium import webdriver
from fpdf import FPDF
import time

# Search: it works fine for competence search, e.g. "Python", "Selenium" or "Alijan Momeni", "*", ""...
# Filter: not implemented yet

class CvDataBase():

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
        _login_button = "Logga in"
        _email_field = "i0116"
        _email_next_button = "idSIButton9"
        _password_field = "passwordInput"
        _password_submit_button = "submitButton"
        _stay_signed_in_checkbox = "KmsiCheckboxField"
        _yes_button = "idSIButton9"
        _popup_close_button = "//span[@class='oi oi-x']"

        # click on login link on the start page
        self.driver.find_element_by_link_text(_login_button).click()

        # enter user name and click on 'Next' button
        self.driver.find_element_by_id(_email_field).send_keys(email)
        self.driver.find_element_by_id(_email_next_button).click()

        # enter password name and click on 'Sign in' button
        self.driver.find_element_by_id(_password_field).send_keys(password)
        self.driver.find_element_by_id(_password_submit_button).click()

        # click on stay signed in checkbox
        self.driver.find_element_by_id(_stay_signed_in_checkbox).click()

        # click on 'Yes' button
        self.driver.find_element_by_id(_yes_button).click()

        # click on'No' button
        # driver.find_element_by_id("idBtn_Back").click()

        if self.driver.find_element_by_xpath(_popup_close_button):
            self.driver.find_element_by_xpath(_popup_close_button).click()

        # enter searchText and click on Search button
    def searchFunction(self, searchText):
        _search_icon = "//span[contains(text(),'Sök')]"
        _search_field = "//div[@class='search__input']/input[@type='text']"
        _search_button = "//span[@class='search'][contains(text(),'Sök')]"

        # click on Search icon, enter Search field and click Search button
        self.driver.find_element_by_xpath(_search_icon).click()
        self.driver.find_element_by_xpath(_search_field).send_keys(searchText)
        self.driver.find_element_by_xpath(_search_button).click()

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

    def getLastModifiedDate(self):
        lastModified = self.driver.execute_script("return document.lastModified")
        print(lastModified)
        print(type(lastModified))
        return lastModified



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
            '''
            # get last modified date/time for web page. To get the date on output file, uncomment this code block 
            # and comment line 97 above, i.e. outFile.write(consultant + ":" + "\n")
            dateTime = self.getLastModifiedDate()
            outFile.write("%s (Last Modified: %s):" % (consultant, dateTime))
            outFile.write("\n")
            '''

            lineSize = 0  ###
            # get each consultant's competences
            consultantCompetences = "//div[@id='employeeCard%d']//span[@class='competence-name pr-2 ng-star-inserted']" % x
            competences = self.driver.find_elements_by_xpath(consultantCompetences)
            for competence in competences:
                competenceLabel = " " + competence.text

                # Determine size of each line fitting pdf page
                lineSize += len(competenceLabel)
                if lineSize > 90:
                    outFile.write("\n")
                    lineSize = len(competenceLabel)

                outFile.write(competenceLabel)

            outFile.write("\n\n")
        outFile.close()

    def convertTextFileToPdf(self):
        # create pdf object
        pdf = FPDF()
        # add a page
        pdf.add_page()
        # set style and size of font
        pdf.set_font("Arial", size=13)
        # open text file for reading
        outFilePath = "C:\\Users\\AlijanMo\\Desktop\\TestReport\\ListOfCompetences.txt"
        outFile = open(outFilePath, "r")
        # insert the texts in pdf
        for x in outFile:
            pdf.cell(200, 10, txt=x, ln=1, align='L')

        # save the pdf with name .pdf
        pdf.output("C:\\Users\\AlijanMo\\Desktop\\TestReport\\ListOfCompetences.pdf")

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
        self.convertTextFileToPdf()

username = "alijan.momeni@hiq.se"
password = "Hiq2020?"
searchText = "Alijan Momeni"

cdb = CvDataBase()
cdb.searchResult(username, password, searchText)

# How to Run this script in prompt terminal:
# 1. Download Python and web driver(s) for web browser(s)
# 2. Add path to Python and web driver(s) in sys environment variable
# 3. Change web driver, path to the output text file and pdf file, if required
# 4. provide username, password and searchText
# 5. Navigate to the testfile.py location
# 6. Enter: python testfile.py
# 7. Press Enter