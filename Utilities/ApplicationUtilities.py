from selenium.webdriver.support.select import Select
from Utilities import configReader


class ApplicationUtilities:
    def __init__(self,driver):
        self.driver = driver

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith(("_XPATH")):
            dropdown = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator))
        elif str(locator).endswith(("_CSS")):
            dropdown = self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)

    def type(self,locator,value):
        if str(locator).endswith(("_XPATH")):
            self.driver.find_element_by_xpath(configReader.readConfig("locators",locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators",locator)).send_keys(value)

    def click(self,locator):
        if str(locator).endswith(("_XPATH")):
            self.driver.find_element_by_xpath(configReader.readConfig("locators",locator)).click()
        elif str(locator).endswith(("_CSS")):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators",locator)).click()

    def switch_default(self):
        self.driver.switch_to.default_content()

    def window_scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")