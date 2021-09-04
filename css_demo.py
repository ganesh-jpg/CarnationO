# from selenium import webdriver
#
# driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.get("http://way2automation.com/way2auto_jquery/index.php")
# driver.find_element_by_css_selector("input[name=name]").send_keys("Rahul")

from selenium.webdriver import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("http://way2automation.com/way2auto_jquery/index.php")
driver.maximize_window()

wait=WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Signin")))
#once displayed,below logic
driver.find_element_by_link_text("Signin").click()

# signin = driver.find_element_by_css_selector("a[href*='Signin']")
# ActionChains(driver).move_to_element(signin).click().perform()

# #driver.find_element_by_xpath("//input[@type='submit']").click()
# button = driver.find_element_by_xpath("//input[@type='submit']")
# driver.implicitly_wait(20)
# ActionChains(driver).move_to_element(button).click().perform()

