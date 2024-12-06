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

# Locator and search strategy, Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Locator and search strategy, Email field
driver.find_element(By.ID, "ap_email")

# Locator and search strategy, Continue button
driver.find_element(By.ID, "continue")

# Locator and search strategy, Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of use']")

# Locator and search strategy, Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Locator and search strategy, Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Locator and search strategy, Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Locator and search strategy, Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Locator and search strategy, Create your Amazon account button
driver.find_element(By.XPATH, "//a[@class='a-button-text']")




