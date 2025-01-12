from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    def search_product(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart(self):
        self.click(*self.CART_ICON)