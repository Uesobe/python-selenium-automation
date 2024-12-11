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

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")

# Create Account text
driver.find_element(By.CSS_SELECTOR, ".a-box-inner h1")

# Your name text field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Mobile number or email text field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Passwords must be at least 6 characters text
driver.find_element(By.CSS_SELECTOR, "#auth-password-requirement-info")

# Password text field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Continue button
driver.find_element(By.CSS_SELECTOR, "#continue")

# Condition of use button
driver.find_element(By.CSS_SELECTOR, "[href*='_notification_condition']")

# Privacy notice button
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_p']")

