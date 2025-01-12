from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SIGNIN_BTN = (By.CSS_SELECTOR, "#account-sign-in")
    SIDE_SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def search_product(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_sign_in(self):
        self.click(*self.SIGNIN_BTN)

    def click_right_nav_sign_in(self):
        self.click(*self.SIDE_SIGNIN_BTN)
