# # importing the modules
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time
#
# # using chrome driver
# driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#
# # web page url
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#
# # switch to 1st frame
# driver.switch_to.frame("packageListFrame")
#
# # click on 1st frame
# driver.find_element_by_link_text("org.openqa.selenium.chromium").click()
#
# # back to default web page frame
# driver.switch_to.default_content()




# ****************************************************************

from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
browser.get("https://en.wikipedia.org")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
browser.close()

# for i in range(20):  # adjust integer value for need
#     # you can change right side number for scroll convenience or destination
#     browser.execute_script("window.scrollBy(0, 250)")
#     # you can change time integer to float or remove
#     time.sleep(1)
