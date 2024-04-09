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
    def testForgotPassword(self, boot):
        """Test case to verify forgot password link and print the result of the test"""
        self.driver.get(data.WebData().url)
        locator.WebLocators().forgotPassword(self.driver, locator.WebLocators().forgotPasswordLinkLocator)
        locator.WebLocators().enterUsername(self.driver, locator.WebLocators().usernameInputLocator, "Admin")
        locator.WebLocators().clickReset(self.driver, locator.WebLocators().resetButtonLocator)
        assert self.driver.current_url == data.WebData().passwordReset
        print("Reset password link sent successfully!")



if __name__ == "__main__":
    pytest.main()
