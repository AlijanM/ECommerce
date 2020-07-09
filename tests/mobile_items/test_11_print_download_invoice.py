from utilities.execution_status import ExecutionStatus
from pages.mobile_items.print_download_invoice_page import PrintInvoice
import unittest
import pytest

# Export all Orders in csv file and display these information in console and
# you are able to send this file to another email id as attachment


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ExportOrdersToFileTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.pi = PrintInvoice(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_1_verifyErrorMsg(self):
        result = self.pi.verifyErrorMsg("user01", "guru99com", "1", "4")
        self.es.markFinal("test_1_verifyErrorMsg", result, "Verification of Error  Message")

    def test_2_verifyInvoiceDownload(self):
        result = self.pi.verifyinvoiceDownload("3", "4")
        self.es.markFinal("test_2_verifyInvoiceDownload", result, "Verification of Invoice Download")


#py.test -s -v tests\mobile_items\test_11_print_download_invoice.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html