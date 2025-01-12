from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class SearchResultsPage(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
    SIDEBAR_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")

    def verify_search_result(self):
        actual_result = self.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
        assert 'tea' in actual_result, f'Expected text {'tea'} not in actual {actual_result}'

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def click_sidebar_add_to_cart(self):
        self.click(*self.SIDEBAR_ADD_TO_CART_BTN)
