from utilities.execution_status import ExecutionStatus
from pages.mobile_items.sort_by_name_page import SortByName
import unittest
import pytest

# Verify items in Mobile List page can be sorted by 'Name'

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SortByNameTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.sbn = SortByName(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_1_homePage(self):
        result1 = self.sbn.verifyTextOnHomePage()
        self.es.markFinal("test_homePage", result1, "Verification of Text On Home Page")


    #@pytest.mark.run(order=2)
    def test_2_mobilePage(self):
        result1 = self.sbn.verifyMobilePageTitle("Mobile")
        self.es.mark(result1, "Verification of Page Title")

        result2 = self.sbn.verifySortByName()
        self.es.markFinal("test_mobilePage", result2, "Verification of Product Sorting")

#py.test -s -v tests\mobile_items\sort_by_name_test.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html