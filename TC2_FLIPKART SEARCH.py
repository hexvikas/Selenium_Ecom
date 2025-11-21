from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()

# Find search box
search = driver.find_element(By.NAME, "q")

# Type text
search.send_keys("Selenium Python")

# Press Enter
search.send_keys(Keys.ENTER)

# Extract 5 results
results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]

print("\nTop 5 Results:")
for r in results:
    print(r.text)

driver.quit()
