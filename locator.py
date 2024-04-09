from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebLocators:

    def __init__(self):
        """this method is to locate the forgot password link, reset password    """
        self.usernameLocator = "username"
        self.passwordLocator = "password"
        self.buttonLocator = "button"
        self.forgotPasswordLinkLocator = "//*[@class='orangehrm-login-forgot']"
        self.usernameInputLocator = "username"
        self.resetButtonLocator = "//button[contains(@class, 'oxd-button--large') and contains(@class, 'oxd-button--secondary') and contains(@class, 'orangehrm-forgot-password-button') and contains(@class, 'orangehrm-forgot-password-button--reset')]"
        self.adminPageLocator = "Admin"
        self.userManagementLocator = "//span[contains(text(), 'User Management ')]"
        self.jobLocator = "//span[contains(text(), 'Job')]"
        self.organizationLocator = "//span[contains(text(), 'Organization')]"
        self.qualificationsLocator = "//span[contains(text(), 'Qualifications')]"
        self.nationalitiesLocator = "Nationalities"
        self.corporateBrandingLocator = "Corporate Branding"
        self.configurationLocator = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span"
        self.pimLocator = "PIM"
        self.leaveLocator = "Leave"
        self.timeLocator = "Time"
        self.recruitmentLocator = "Recruitment"
        self.myInfoLocator = "My Info"
        self.performanceLocator = "Performance"
        self.dashBoardLocator = "Dashboard"
        self.directoryLocator = "Directory"
        self.maintenanceLocator = "Maintenance"
        self.claimLocator = "Claim"
        self.buzzLocator = "Buzz"
    def enterText(self, driver, locator, textValue):
        """ this method is to locate the element using NAME, wait until it is located and enter the text """
        WebDriverWait(driver, 10). until(EC.presence_of_element_located((By.NAME, locator)))
        element = driver.find_element(by=By.NAME, value=locator)
        element.clear()
        element.send_keys(textValue)

    def clickButton(self, driver, locator):
        """ this method is to locate the element using TAG NAME, wait until its located and enter the text """
        driver.find_element(by=By.TAG_NAME, value=locator).click()

    def forgotPassword(self, driver, locator):
        """ this method is to locate the element using XPATH and click on it """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def enterUsername(self,driver, locator, textValue):
        """ this method is to locate the element using NAME and enter the username"""
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, locator)))
        driver.find_element(by=By.NAME, value=locator).send_keys(textValue)

    def clickReset(self,driver, locator):
        """This method is to find the element by XPATH and click on it"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def gotoAdminPage(self, driver, locator):
        """This method is to find the element by XPATH and click on it"""
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).click()

    def userManagementDisplayed(self, driver, locator):
        """This method is to find the element by XPATH and to check if its displayed"""
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).is_displayed()

    def jobDisplayed(self, driver, locator):
        """This method is to find the element by XPATH and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).is_displayed()

    def organizationDisplayed(self, driver, locator):
        """This method is to find the element by XPATH and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).is_displayed()

    def qualificationsDisplayed(self, driver, locator):
        """This method is to find the element by XPATH and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).is_displayed()

    def moreDropDown(self, driver, locator):
        """This method is to find the element by XPATH and to click it"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def nationalityDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def corporateBrandingDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def configurationDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).is_displayed()

    def adminDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def pimDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def leaveDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def timeDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def recruitmentDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def myInfoDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def performanceDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def dashboardDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def directoryDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def maintenanceDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def claimDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()

    def buzzDisplayed(self, driver, locator):
        """This method is to find the element by LINKTEXT and to check if its displayed"""
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).is_displayed()