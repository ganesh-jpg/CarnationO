from Utilities.ApplicationUtilities import ApplicationUtilities


class DemoPage(ApplicationUtilities):
    def __init__(self, driver):
        super().__init__(driver) # call to BasePage Constructor

    def demoform(self):
        print("In Demo Form --------------------------------------------------")
        self.select("countryDemo_XPATH","Iceland")