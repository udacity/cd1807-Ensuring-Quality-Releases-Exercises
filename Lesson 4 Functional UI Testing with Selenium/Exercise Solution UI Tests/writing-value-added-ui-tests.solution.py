# #!/usr/bin/env python
from selenium import webdriver

# Start the browser and navigate to http://automationpractice.com/index.php.
driver = webdriver.Chrome()
url = 'http://automationpractice.com/index.php'
search_item = 't shirt'

print('Navigating to ' + url)
driver.get(url)

print('Searching for ' + search_item)
driver.find_element_by_css_selector("input[id='search_query_top']").send_keys(search_item)
driver.find_element_by_css_selector("button[class='btn btn-default button-search']").click()
our_search = driver.find_element_by_css_selector("div[id='center_column'] > h1 > span.lighter").text
results = driver.find_element_by_css_selector("div[id='center_column'] > h1 > span.heading-counter").text

assert "T SHIRT" in our_search
print ("We are on the search results page for " + our_search) 
if '1' in results:
    print("We found 1 result successfully.")
else:
    print('ERROR! We did not find 1 result!')

