from Utilities.ApplicationUtilities import ApplicationUtilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class CSSDemoPage(ApplicationUtilities):
    def __init__(self, driver):
        super().__init__(driver) # call to BasePage Constructor

    def cssdemoform(self):
        print(" ******************* In css demo form ************************")
        self.type("name_css","Ganesh")

    def linktextform(self):
        print(" **************** In link text **********************")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Signin")))
        self.click("Signin")

    def switch_default_form(self):
        self.driver.switch_to.frame("packageListFrame")
        self.driver.find_element_by_link_text("org.openqa.selenium.chromium").click()
        self.switch_default()

    def window_scroll_form(self):
        self.window_scroll()

