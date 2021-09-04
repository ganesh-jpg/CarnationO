import pytest
from TestCases.BaseTest import BaseTest
from Pages.RegistrationPage import RegistrationPage
from Utilities import DataProvider
import logging
from Utilities.LogUtil import Logger

Log=Logger(__name__,logging.INFO)

class Test_SignUp(BaseTest):

    # Simple Constant Value based Test Case
    def test_dosignup(self):
        Log.logger.info("--- Test dosignup 1 Started ---")
        regPage = RegistrationPage(self.driver)
        regPage.fillform("KV","123456789","email@gmail.com","India","Pune","KV@123","selenium")
        Log.logger.info("--- Test dosignup 1 Ended ---")


    # Wrokbook set of Values based Test Case
    @pytest.mark.parametrize("Name,Phone,Email,Country,City,Username,Password",DataProvider.get_data("Register"))
    def test_signup_submit(self,Name,Phone,Email,Country,City,Username,Password):
        Log.logger.info("--- Test signup submit Started ---")
        regPageSubmit = RegistrationPage(self.driver)
        regPageSubmit.fillform(Name,Phone,Email,Country,City,Username,Password)
        regPageSubmit.submitform()
        Log.logger.info("--- Test signup submit Ended ---")



