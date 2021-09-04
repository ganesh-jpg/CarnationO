from TestCases.BaseTest import BaseTest
from Pages.CSSDemoPage import CSSDemoPage


class Test_css_dummy(BaseTest):

    def test_dosignup_withcss(self):
        print("Test -------------------------------------------------------------------------------")
        rPage = CSSDemoPage(self.driver)
        rPage.cssdemoform()