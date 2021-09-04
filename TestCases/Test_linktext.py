from TestCases.BaseTest import BaseTest
from Pages.CSSDemoPage import CSSDemoPage


class Test_Dummy(BaseTest):
    # Simple Constant Value based Test Case
    def test_dosignup(self):
        print("****************** Test  **************************************")
        rPage = CSSDemoPage(self.driver)
        rPage.linktextform()