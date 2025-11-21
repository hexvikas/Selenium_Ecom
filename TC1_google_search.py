from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 1. Start Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Open URL
driver.get("https://www.google.com")

# 3. Maximize window
driver.maximize_window()

# 4. Print title
print("Page Title:", driver.title)

# 5. Close browser
driver.quit()
