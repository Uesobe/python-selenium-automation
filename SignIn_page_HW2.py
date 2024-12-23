from mmap import ACCESS_COPY

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)

ACC_NAV_SIGNIN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
SIGN_INTO_YOUR_ACC_TEXT = (By.XPATH, "//span[text()='Sign into your Target account']")
# Open web page
driver.get('https://www.target.com/')

# Navigate to the right page
driver.find_element(By.ID, 'account-sign-in').click()
driver.wait.until(EC.element_to_be_clickable(ACC_NAV_SIGNIN)).click()

# Verification
expected_result = 'Sign into your Target account'
actual_result = driver.wait.until(EC.presence_of_element_located(SIGN_INTO_YOUR_ACC_TEXT)).text
assert expected_result == actual_result, f'Expected text {expected_result} not same as Actual text {actual_result}'
print('Test case passed')

sleep(3)
driver.quit()

