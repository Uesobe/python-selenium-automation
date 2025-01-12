from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class SearchResultsPage(BasePage):
    def verify_search_result(self):
        actual_result = self.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
        assert 'tea' in actual_result, f'Expected text {'tea'} not in actual {actual_result}'