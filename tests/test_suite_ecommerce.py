import unittest
from tests.mobile_items.test_01_sort_by_name import SortByNameTest
from tests.mobile_items.test_02_product_prices import ProductPriceTest
from tests.mobile_items.test_03_shopping_cart import ShoppingCartTest
from tests.mobile_items.test_04_compare_products import CompareProductsTest
from tests.mobile_items.test_05_create_account import CreateAccountTest
from tests.mobile_items.test_06_purchase_products import PurchaseProductsTest
from tests.mobile_items.test_07_save_placed_order_as_pdf import SavePlacedOrderTest
from tests.mobile_items.test_08_change_placed_order import ChangePlacedOrderTest


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(SortByNameTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ProductPriceTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(ShoppingCartTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(CompareProductsTest)
tc5 = unittest.TestLoader().loadTestsFromTestCase(CreateAccountTest)
tc6 = unittest.TestLoader().loadTestsFromTestCase(PurchaseProductsTest)
tc7 = unittest.TestLoader().loadTestsFromTestCase(SavePlacedOrderTest)
tc8 = unittest.TestLoader().loadTestsFromTestCase(ChangePlacedOrderTest)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

# command to run the this test suite: py.test tests\test_suite_ecommerce.py --browser chrome
