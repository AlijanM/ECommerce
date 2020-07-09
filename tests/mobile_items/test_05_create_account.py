from utilities.execution_status import ExecutionStatus
from pages.mobile_items.create_account_page import CreateAccount
import unittest
import pytest

# Verify user can create an account in e-Commerce site and can share wish-list to other people using email.
# Change "abc20@hotmail.com"/"newpass20" (in test_1_confirmRegistration() below) to "abc21@hotmail.com"/"newpass21"

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CreateAccountTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ca = CreateAccount(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_1_confirmRegistration(self):
        self.ca.createAccount("fname15", "lname15", "abc20@hotmail.com", "newpass20")
        result = self.ca.verifyRegistration()
        self.es.markFinal("test_confirmRegistration", result, "Verification of Registration")

    #@pytest.mark.run(order=2)
    def test_2_confirmWishlistShare(self):
        self.ca.addAndShareWishlist("new03@email.com")
        result = self.ca.verifyWishlistShare()
        self.es.markFinal("test_confirmWishlistShare", result, "Verification of Wishlist Share")


#py.test -s -v tests\mobile_items\create_account_test.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html