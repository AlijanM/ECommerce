from utilities.execution_status import ExecutionStatus
from pages.mobile_items.discount_coupon_page import DiscountCoupon
import unittest
import pytest

# Verify Discount Coupon works correctly

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DiscountCouponTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.dc = DiscountCoupon(self.driver)
        self.es = ExecutionStatus(self.driver)

    # @pytest.mark.run(order=1)
    def test_verifyDiscount(self):
        result = self.dc.verifyAppliedDiscount()
        self.es.markFinal("test_verifyDiscount", result, "Verification of Applied Discount")



#py.test -s -v tests\mobile_items\test_09_discount_coupon.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html