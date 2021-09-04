from TestCases.BaseTest import BaseTest
from Pages.CSSDemoPage import CSSDemoPage


class Test_scroll(BaseTest):

    def test_dosignup_withscroll(self):
        print(" *************************** Test ******************************** ")
        rPage = CSSDemoPage(self.driver)
        rPage.window_scroll_form()