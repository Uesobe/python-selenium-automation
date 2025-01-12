from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SigninPage(BasePage):
    VERIFY_SIGNIN = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_in(self):
        self.click(*self.VERIFY_SIGNIN)