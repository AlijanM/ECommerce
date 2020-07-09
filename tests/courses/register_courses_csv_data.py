from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.execution_status import ExecutionStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = ExecutionStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        #self.driver.find_element_by_link_text("All Courses").click()
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']//img").click()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\semc0\\Desktop\\letskodeit_200607\\testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(courseName)
        time.sleep(1)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(1)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")