from utilities.execution_status import ExecutionStatus
from pages.mobile_items.product_prices_page import ProductPrices
import unittest
import pytest

# Verify that cost of product in list page and details page are equal

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ProductPriceTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.pp = ProductPrices(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_mobilePrices(self):
        result = self.pp.comparePrices()
        self.es.markFinal("test_mobilePrices", result, "Verification of Mobile Prices")


#py.test -s -v tests\mobile_items\product_prices_test.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html