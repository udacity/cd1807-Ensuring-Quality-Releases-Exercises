# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start the browser and navigate to https://www.saucedemo.com/
# Initialize the Chrome browser using `webdriver.Chrome()`.
driver = webdriver.Chrome()

# Navigate to the specified URL using `driver.get()`.
driver.get('https://www.saucedemo.com/')

# Log in to the website

# Enter the username

# Enter the password

# Click the login button

# Wait for the page to load


# Find the search input element and enter the search term "sauce"
# Note: Saucedemo website does not have a search box; use the first available button as an example
# Writing a CSS Selector for the "Add to cart" button for the first product displayed

# Validate the CSS selector in the web browser console. 


# Locate the "Add to cart" button using `By.CSS_SELECTOR` and click it.

# Locate the cart icon using `By.CSS_SELECTOR`.
# Validate that the product is added to the cart by checking the cart icon


# Print the number of items in the cart

# Optional: Add some wait time to see the results before the browser closes

# Close the browser
