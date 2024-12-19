from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(9)

@when('Click target circle icon')
def click_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "#utilityNav-circle").click()


@when('Click on Add to cart')
def click_target_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()


@when('Click on the Add to Cart on the side bar')
def click_target_cart_side_bar(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']").click()


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify atleast 10 benefit cells shown')
def verify_atleast_10_benefit(context):
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
    print(cells)
    assert len(cells) >= 10, f'len(cells) not equal to 10'


@then('Verify search result is shown for {expected_product}')
def verify_search_result(context, expected_product):
    actual_result = context.driver.find_element(By. CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert expected_product in actual_result, f'Expected text {expected_product} not in actual {actual_result}'


@then('Verify {expected_product} is in cart')
def verify_tea(context, expected_product):
    actual_product = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='cartItem-title']").text
    assert expected_product in actual_product, f'Expected text {expected_product} not in actual {actual_product}'






