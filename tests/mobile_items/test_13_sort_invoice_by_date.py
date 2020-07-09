from utilities.execution_status import ExecutionStatus
from pages.mobile_items.sort_invoice_by_date_page import SortInvoice
import unittest
import pytest

# Verify Sort is working correctly


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SortInvoiceTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.si = SortInvoice(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_verifyInvoiceSort(self):
        result = self.si.verifyInvoiceSort()
        self.es.markFinal("test_verifyInvoiceSort", result, "Verification of Invoice Sort")


#py.test -s -v tests\mobile_items\test_13_sort_invoice_by_date.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html