from TestCases.BaseTest import BaseTest
from Pages.CSSDemoPage import CSSDemoPage


class Test_default_dummy(BaseTest):

    def test_switch_default(self):
        print(" ******************************* switch default test case ******************************")
        rPage = CSSDemoPage(self.driver)
        rPage.switch_default_form()