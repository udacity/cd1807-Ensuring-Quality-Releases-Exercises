# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Start the browser and navigate to https://www.saucedemo.com/
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

# Log in to the website
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

# Wait for the page to load
import time
time.sleep(2)  # Wait for 2 seconds

# Find the search input element and enter the search term "sauce"
search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
search_box.send_keys("sauce")
search_box.send_keys(Keys.RETURN)  # Simulate pressing the Enter key

# Optional: Add some wait time to see the results before the browser closes
time.sleep(5)  # Wait for 5 seconds

# Close the browser
driver.quit()
