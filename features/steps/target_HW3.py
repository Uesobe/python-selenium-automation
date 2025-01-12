from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main_page(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


@when('CLick cart icon')
def click_cart_icon(context):
    context.app.header.click_cart()
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()


@then('Verify cart icon opens and is empty')
def verify_cart_icon_open(context):
    context.app.cart_page.verify_cart_empty()
    #expected_result = 'Your cart is empty'
    #actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']" ).text
    #assert expected_result == actual_result, f'Expected test {expected_result} does not match actual test{actual_result}'


@when('Click signIn button on the right top corner')
def click_sign_button(context):
    context.app.header.click_sign_in()
    #context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()


@when('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.app.header.click_right_nav_sign_in()
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in()
    #context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

    sleep(4)
