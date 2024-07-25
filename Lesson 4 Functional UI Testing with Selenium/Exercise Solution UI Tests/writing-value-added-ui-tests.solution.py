# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the browser and navigate to https://www.saucedemo.com/
driver = webdriver.Chrome()

# 1. Add print statements that tell us which site we are going to
site_url = 'https://www.saucedemo.com/'
print(f"Navigating to site: {site_url}")
driver.get(site_url)

# Log in to the website
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

# Wait for the page to load
time.sleep(2)  # Wait for 2 seconds

# Add print statement for the action being performed
print("Adding the first item to the cart")

# 2. Add the CSS Selectors for the required elements
# CSS Selector for the title of the first item displayed
our_item_css_selector = ".inventory_item_name"
# CSS Selector for the cart badge that shows the number of items in the cart
results_css_selector = ".shopping_cart_badge"

# 3. Store the elements in variables
our_item = driver.find_element(By.CSS_SELECTOR, our_item_css_selector).text
results = driver.find_element(By.CSS_SELECTOR, results_css_selector).text

# Print the values of our_item and results
print(f"Our item: {our_item}")
print(f"Results: {results}")

# Add the first item to the cart
driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()

# Wait for the cart to update
time.sleep(2)  # Wait for 2 seconds

# 4. Make an assertion for the item title being contained in our_item
assert "Sauce Labs" in our_item, "Item name does not contain 'Sauce Labs'"

# 5. Make an if/else conditional that checks if "1" is in results
if "1" in results:
    print("1 item was added to the cart successfully.")
else:
    print("Error: The item was not added to the cart.")

# Optional: Add some wait time to see the results before the browser closes
time.sleep(5)  # Wait for 5 seconds

# Close the browser
driver.quit()
