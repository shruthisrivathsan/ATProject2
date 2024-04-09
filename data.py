class WebData:
    """this class is used to contain all the data required to test OrangeHRM
    data is stored in the excel file"""

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.dashboardURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        self.passwordReset = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
        self.adminPage = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        self.loginPageTitle = "OrangeHRM"
        self.username = "Admin"
        self.password = "admin123"