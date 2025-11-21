from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.flipkart.com")
driver.maximize_window()
time.sleep(2)

# close popup if exists
try:
    driver.find_element(By.XPATH, "//span[text()='✕']").click()
except:
    pass

search = driver.find_element(By.NAME, "q")
search.send_keys("laptop")
search.send_keys(Keys.ENTER)

time.sleep(2)

products = driver.find_elements(By.XPATH, "//div[@data-id]")[:5]

print("\nTop 5 Laptops:")
for p in products:
    name = p.find_element(By.XPATH, ".//div[contains(@class,'_4rR01T')]").text
    price = p.find_element(By.XPATH, ".//div[contains(@class,'_30jeq3')]").text
    print(name, price)

driver.quit()
