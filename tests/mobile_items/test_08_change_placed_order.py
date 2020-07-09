from utilities.execution_status import ExecutionStatus
from pages.mobile_items.change_placed_order_page import ChangePlacedOrder
import unittest
import pytest

# # Verify user is able to reorder/change placed order
# 1. precondition: User account must have a placed order in status Pending.
# Account "abc11@hotmail.com", "newpass11" has such an order 100012396


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ChangePlacedOrderTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cpo = ChangePlacedOrder(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_1_verifyGranTotals(self):
        result = self.cpo.verifyCurrentGrandTotals()
        self.es.markFinal("test_1_verifyGranTotals", result, "Verification of Grand Totals")

    def test_2_verifyReorderConfirmation(self):
        result = self.cpo.verifyNewOrderConfirmation()
        self.es.markFinal("test_2_verifyReorderConfirmation", result, "Verification of Reorder Confirmation")

    def test_3_VerifyNewPurchaseConfirmation(self):
        result = self.cpo.verifyNewPurchaseConfirmation()
        self.es.markFinal("test_3_VerifyNewPurchaseConfirmation", result, "Verification of Purchase Confirmation")


#py.test -s -v tests\mobile_items\test_08_change_placed_order.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html