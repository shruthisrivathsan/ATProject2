# import pytest, data and locators
import pytest
from Data import data
from Locators import locator
# common imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


class Test:
    @pytest.fixture
    def boot(self):
        """ Fixture to set up and quitting the WebDriver instance."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    @pytest.mark.html
    def testMenuOptionsVisibility(self, boot):
        """Test case to validate visibility of all menu options on admin page using the locators in the locators folder
         and print the result of the test"""
        self.driver.get(data.WebData().url)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
        locator.WebLocators().gotoAdminPage(self.driver, locator.WebLocators().adminPageLocator)
        # Assert visibility of Admin option
        try:
            locator.WebLocators().adminDisplayed(self.driver, locator.WebLocators().adminPageLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of PIM option
        try:
            locator.WebLocators().pimDisplayed(self.driver, locator.WebLocators().pimLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Leave
        try:
            locator.WebLocators().leaveDisplayed(self.driver, locator.WebLocators().leaveLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Time option
        try:
            locator.WebLocators().timeDisplayed(self.driver, locator.WebLocators().timeLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Recruitment option
        try:
            locator.WebLocators().recruitmentDisplayed(self.driver, locator.WebLocators().recruitmentLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of My Info option
        try:
            locator.WebLocators().myInfoDisplayed(self.driver, locator.WebLocators().myInfoLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Performance option
        try:
            locator.WebLocators().performanceDisplayed(self.driver, locator.WebLocators().performanceLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Dashboard option
        try:
            locator.WebLocators().dashboardDisplayed(self.driver, locator.WebLocators().dashBoardLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Directory option
        try:
            locator.WebLocators().directoryDisplayed(self.driver, locator.WebLocators().directoryLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Maintenance option
        try:
            locator.WebLocators().maintenanceDisplayed(self.driver, locator.WebLocators().maintenanceLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Claim option
        try:
            locator.WebLocators().claimDisplayed(self.driver, locator.WebLocators().claimLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Buzz Optiom
        try:
            locator.WebLocators().buzzDisplayed(self.driver, locator.WebLocators().buzzLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        print("All menu options are displayed")


if __name__ == "__main__":
    pytest.main()
