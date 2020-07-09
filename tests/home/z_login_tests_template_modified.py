from pages.home.login_page import LoginPage
from utilities.execution_status import ExecutionStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.es = ExecutionStatus(self.driver)


    @pytest.mark.run(order=1)
    def test_validLogin(self):
        #self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.es.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.es.markFinal("test_validLogin", result2, "Login Verification")
        self.lp.logout()

    @pytest.mark.run(order=2)
    def test_invalidLogin(self):
        #self.lp.logout()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True
