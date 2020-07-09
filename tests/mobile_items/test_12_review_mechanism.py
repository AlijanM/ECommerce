from utilities.execution_status import ExecutionStatus
from pages.mobile_items.review_mechanism_page import ReviewMechanism
import unittest
import pytest

# Verify the product review mechanism

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ReviewMechanismTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.rm = ReviewMechanism(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_verifyReviewDisplay(self):
        result = self.rm.verifyReviewDisplay("Good Q&D2", "Good QD4", "almomash34", "user01", "guru99com")
        self.es.markFinal("test_verifyReviewDisplay", result, "Verification of Review Display")


#py.test -s -v tests\mobile_items\test_12_review_mechanism.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html