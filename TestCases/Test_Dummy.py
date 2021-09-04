from TestCases.BaseTest import BaseTest
from Pages.DemoPage import DemoPage


class Test_Dummy(BaseTest):
    # Simple Constant Value based Test Case
    def test_dosignup(self):
        print("Test -------------------------------------------------------------------------------")
        rPage = DemoPage(self.driver)
        rPage.demoform()

    