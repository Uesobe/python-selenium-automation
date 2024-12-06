from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open web page
driver.get('https://www.target.com/')

# Navigate to the right page
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()


# Verification
expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert expected_result == actual_result, f'Expected text {expected_result} not same as Actual text {actual_result}'
print('Test case passed')

sleep(3)
driver.quit()

