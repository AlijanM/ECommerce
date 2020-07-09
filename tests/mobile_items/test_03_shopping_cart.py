from utilities.execution_status import ExecutionStatus
from pages.mobile_items.shopping_cart_page import ShoppingCart
import unittest
import pytest

# Verify that user will not be able to add more product in cart than the product available in the store

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ShoppingCartTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.sc = ShoppingCart(self.driver)
        self.es = ExecutionStatus(self.driver)

    # @pytest.mark.run(order=1)
    def test_1_invalidQuantity(self):
        result = self.sc.verifyErrorMsg()
        self.es.markFinal("test_invalidQuantity", result, "Verification of size of Shopping Cart")

    # @pytest.mark.run(order=2)
    def test_2_emptyShoppingCart(self):
        result = self.sc.verifyEmptyCart()
        self.es.markFinal("test_emptyShoppingCart", result, "Verification of empty Shopping Cart")


#py.test -s -v tests\mobile_items\shopping_cart_test.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html