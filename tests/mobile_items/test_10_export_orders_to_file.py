from utilities.execution_status import ExecutionStatus
from pages.mobile_items.export_orders_to_file_page import ExportOrdersToFile
import unittest
import pytest

# # Verify user is able to reorder/change placed order
# 1. precondition: User account must have a placed order in status Pending.
# Account "abc11@hotmail.com", "newpass11" has such an order 100012396


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ExportOrdersToFileTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.etf = ExportOrdersToFile(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_1_verifySuccessfullExport(self):
        result = self.etf.validFileExport("user01", "guru99com", "CSV")
        self.es.markFinal("test_1_verifySuccessfullExport", result, "Verification of File Export")


#py.test -s -v tests\mobile_items\test_10_export_orders_to_file.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html