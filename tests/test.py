import traceback
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

baseURL = "http://live.demoguru99.com/"
# Set chrome driver
driver = webdriver.Chrome("C:\\drivers\\chromedriver.exe")
# Set firefox driver
# driver = webdriver.Firefox()
# Setting Driver Implicit Time out for An Element
driver.implicitly_wait(3)
# Maximize the window
driver.maximize_window()
# Loading browser with App URL
driver.get(baseURL)

# click on My Account and login
driver.find_element_by_xpath("//a[contains(text(),'Mobile')]").click()
driver.find_element_by_xpath("//h2[@class='product-name']//a[contains(text(),'Sony Xperia')]").click()
driver.find_element_by_xpath("//li[@class='last']//span[contains(text(),'Reviews')]").click()
#
# driver.find_element_by_id("review_field").send_keys("Good Xperia Phone")
# driver.find_element_by_id("summary_field").send_keys("Good Q")
# driver.find_element_by_id("nickname_field").send_keys("almomash")
# driver.find_element_by_xpath("//span[contains(text(),'Submit Review')]").click()

# # view_order_link
# # driver.find_element_by_xpath("//tr[@class='first odd']//a[contains(text(),'View Order')]").click()
# # reorder_link
# driver.find_element_by_xpath("//tr[@class='last odd']//a[@class='link-reorder'][contains(text(),'Reorder')]").click()
#
# # _qty_field
# driver.find_element_by_xpath("//*[@id='shopping-cart-table']/tbody/tr/td[4]/input").clear()
# driver.find_element_by_xpath("//*[@id='shopping-cart-table']/tbody/tr/td[4]/input").send_keys("10")
# # _qty_update_button
# driver.find_element_by_xpath("//button[@type='submit'][@name='update_cart_action'][@title='Update']").click()
#
# # _state_selection
# element = driver.find_element_by_id("region_id")
# slct = Select(element)
# slct.select_by_value("43")
#
# # _zip_field
# driver.find_element_by_id("postcode").clear()
# driver.find_element_by_id("postcode").send_keys("542896")
#
# # _estimate_link
# driver.find_element_by_xpath("//span[contains(text(),'Estimate')]").click()
#
# # _flat_rate_radio_btn
# driver.find_element_by_xpath("//label[contains(text(),'Fixed')]").click()
#
# # _update_total_link
# driver.find_element_by_xpath("//strong//span[@class='price']").click()
#
# # _checkout_button
# driver.find_element_by_xpath("//ul[@class='checkout-types top']//span[contains(text(),'Proceed to Checkout')]").click()
#


# driver.quit()

