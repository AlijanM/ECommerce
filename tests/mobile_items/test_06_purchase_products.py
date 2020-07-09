from utilities.execution_status import ExecutionStatus
from pages.mobile_items.purchase_products_page import PurchaseProducts
import unittest
import pytest

# Verify user is able to purchase products using registered email (use chrome browser)
# The user account must have a product in wish-list

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PurchaseProductsTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.pp = PurchaseProducts(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_1_flatrateVerification(self):
        result = self.pp.verifyFlatRate()
        self.es.markFinal("test_1_flatrateVerification", result, "Verification of Flatrate")

    def test_2_grandTotalVerification(self):
        result = self.pp.verifyGrandTotal()
        self.es.markFinal("verifyGrandTotal", result, "Verification of Grand Total")

    def test_3_orderConfirmation(self):
        result = self.pp.orderConfirmation()
        self.es.markFinal("test_3_orderConfirmation", result, "Verification of Order Confirmation")


#py.test -s -v tests\mobile_items\purchase_products_test.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html