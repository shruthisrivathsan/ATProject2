#import pytest, data and locators
import pytest
from Data import data
from Locators import locator
#common imports
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
    def testTitle(self, boot):
        """Test case to validate the title of the page"""
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        assert self.driver.title == data.WebData().loginPageTitle
        print("Success: Web Title is verified!")

    @pytest.mark.html
    def testAdminPageOptionsVisibility(self, boot):
        """Test case to validate visibility of all options on admin page using the locators in the locators folder
        and print the result of the test"""
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
        locator.WebLocators().gotoAdminPage(self.driver, locator.WebLocators().adminPageLocator)
        # Assert visibility of User Management
        try:
            locator.WebLocators().userManagementDisplayed(self.driver, locator.WebLocators().userManagementLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Job
        try:
            locator.WebLocators().jobDisplayed(self.driver, locator.WebLocators().jobLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Organization
        try:
            locator.WebLocators().organizationDisplayed(self.driver, locator.WebLocators().organizationLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Qualification
        try:
            locator.WebLocators().qualificationsDisplayed(self.driver, locator.WebLocators().qualificationsLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Nationality
        try:
            locator.WebLocators().nationalityDisplayed(self.driver, locator.WebLocators().nationalitiesLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Corporate Branding
        try:
            locator.WebLocators().corporateBrandingDisplayed(self.driver, locator.WebLocators().corporateBrandingLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        # Assert visibility of Configuration
        try:
            locator.WebLocators().configurationDisplayed(self.driver, locator.WebLocators().configurationLocator)
        except NoSuchElementException as e:
            print(f"Error:{e}")
        print("All options are visible")


if __name__ == "__main__":
    pytest.main()
