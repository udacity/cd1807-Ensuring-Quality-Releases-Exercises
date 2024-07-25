# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start the browser and navigate to https://www.saucedemo.com/
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

# Log in to the website
# Enter the username
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
# Enter the password
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
# Click the login button
driver.find_element(By.ID, 'login-button').click()

# Wait for the page to load
time.sleep(2)  # Wait for 2 seconds

# Find the search input element and enter the search term "sauce"
# Note: Saucedemo website does not have a search box; we'll use the first available button as an example
# Writing a CSS Selector for the "Add to cart" button for the first product displayed
add_to_cart_css_selector = "button.btn_inventory"

# Validate this CSS by using the console in the web browser
# You can do this by opening the console in the web browser and running the command:
# document.querySelector("button.btn_inventory")

# Use this CSS selector in the Selenium test to click the "Add to cart" button
driver.find_element(By.CSS_SELECTOR, add_to_cart_css_selector).click()

# Validate that the product is added to the cart by checking the cart icon
cart_icon = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
cart_item_count = cart_icon.text

# Print the number of items in the cart
print(f"Number of items in the cart: {cart_item_count}")

# Optional: Add some wait time to see the results before the browser closes
time.sleep(5)  # Wait for 5 seconds

# Close the browser
driver.quit()
