from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    SIGNIN_LINK= (By.XPATH,"//span[contains(text(),'Sign in')]")
    USERNAME = (By.ID, "identifierId")
    NEXT_BTN = (By.ID, "identifierNext")

    def select_signIn(self):
        self.do_click(self.SIGNIN_LINK)

    def enter_username(self, username):
        self.do_send_keys(self.USERNAME, username)

    def click_next(self):
        self.do_click(self.NEXT_BTN)

    