from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    VERIFY_CART = (By.CSS_SELECTOR, "div[data-test='cartItem-title']")

    def verify_cart_empty(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.CART_EMPTY_MSG).text
        assert expected_result == actual_result, f"Expected '{expected_result}' but got '{actual_result}'"

    def open_cart_page(self):
        self.driver.get('https://www.target.com/cart')

    def verify_product_in_cart(self):
        self.verify_partial_text('Tea', *self.VERIFY_CART)





