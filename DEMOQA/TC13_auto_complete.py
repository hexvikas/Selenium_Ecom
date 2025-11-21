import os, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

REPORTS_DIR="reports"
SHOTS_DIR=os.path.join(REPORTS_DIR,"screenshots")
os.makedirs(SHOTS_DIR, exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/auto-complete")
    driver.maximize_window()

    box = wait.until(EC.visibility_of_element_located((By.ID,"autoCompleteMultipleInput")))
    box.send_keys("Red")
    box.send_keys(Keys.ENTER)
    box.send_keys("Blue")
    box.send_keys(Keys.ENTER)

    chips = driver.find_elements(By.CSS_SELECTOR,".auto-complete__multi-value__label")
    print("Selected:", [c.text for c in chips])
    print("TC PASSED")

except Exception:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    path=os.path.join(SHOTS_DIR, f"{os.path.basename(__file__).replace('.py','')}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
