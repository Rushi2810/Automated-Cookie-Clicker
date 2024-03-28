from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver service and initiate a Chrome session
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the Cookie Clicker game page
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Define element IDs
language_input_id = "langSelect-EN"
cookie_id = "bigCookie"
cookies_id = "cookies"
product_prefix = "product"
product_price_prefix = "productPrice"

# Wait until language selection element is present and click on English
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, language_input_id))
)
language = driver.find_element(By.ID, language_input_id)
language.click()

# Wait until the cookie element is present
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

# Find the cookie element
cookie = driver.find_element(By.ID, cookie_id)

print("Cookie found")

# Infinite loop for clicking the cookie and buying products
while True:
    # Click the cookie to increase cookie count
    cookie.click()
    
    # Get current cookie count
    cookie_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",", ""))
    print(cookie_count)

    # Loop through products to see if any can be purchased
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        # Check if product price is valid
        if not product_price.isdigit():
            continue

        product_price = int(product_price.replace(",", ""))

        # If cookie count is enough, scroll to product, then click to purchase
        if cookie_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            # Scroll product into view
            driver.execute_script("arguments[0].scrollIntoView(true);", product)
            # Wait for a brief moment after scrolling
            time.sleep(0.2)
            # Click on the product
            product.click()
            break
