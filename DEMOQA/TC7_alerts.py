import os, datetime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    driver.get("https://demoqa.com/alerts")
    driver.maximize_window()

    # 1️⃣ simple alert
    wait.until(EC.element_to_be_clickable((By.ID, "alertButton"))).click()
    driver.switch_to.alert.accept()

    # 2️⃣ confirm alert
    wait.until(EC.element_to_be_clickable((By.ID, "confirmButton"))).click()
    driver.switch_to.alert.dismiss()

    # 3️⃣ prompt alert
    wait.until(EC.element_to_be_clickable((By.ID, "promtButton"))).click()
    alert = driver.switch_to.alert
    alert.send_keys("Vikas")
    alert.accept()

    print(wait.until(EC.visibility_of_element_located((By.ID,"promptResult"))).text)
    print("TC PASSED")

except Exception:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    path=os.path.join(SHOTS_DIR, f"{os.path.basename(__file__).replace('.py','')}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
