from utilities.execution_status import ExecutionStatus
from pages.mobile_items.save_placed_order_page import SavePlacedOrder
import unittest
import pytest

# # Verify user is able to save an existing order as pdf
# 1. precondition: User account must have a placed order in status Pending.
# Account "abc11@hotmail.com", "newpass11" has such an order 100012397
# 2. Driver can't find _print_button on popup window

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SavePlacedOrderTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.spo = SavePlacedOrder(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_1_orderNumberVerification(self):
        result = self.spo.verifyRecentOrderNumber()
        self.es.markFinal("test_1_orderNumberVerification", result, "Verification of Order Number")

    def test_2_orderStatusVerification(self):
        result = self.spo.verifyRecentOrderStatus()
        self.es.markFinal("test_2_orderStatusVerification", result, "Verification of Order Status")

    def test_3_orderPrintVerification(self):
        result = self.spo.verifyOrderPrint()
        self.es.markFinal("test_3_orderPrintVerification", result, "Verification of Order Print")


#py.test -s -v tests\mobile_items\test_07_save_placed_order_as_pdf.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html