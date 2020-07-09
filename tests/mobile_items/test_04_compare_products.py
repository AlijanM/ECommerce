from utilities.execution_status import ExecutionStatus
from pages.mobile_items.compare_products_page import CompareProducts
import unittest
import pytest
import time
# Verify that user is able to compare two products

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CompareProductsTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cp = CompareProducts(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_productsComparison(self):
        result = self.cp.verifyComparison()
        self.es.markFinal("test_productsComparison", result, "Verification of Products Comparison")
        self.cp.closePopupWindow()


# py.test tests\mobile_items\compare_products_test.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html