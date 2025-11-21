import os, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

REPORTS_DIR="reports"
SHOTS_DIR=os.path.join(REPORTS_DIR,"screenshots")
os.makedirs(SHOTS_DIR, exist_ok=True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait=WebDriverWait(driver,10)

try:
    driver.get("https://demoqa.com/radio-button")
    driver.maximize_window()

    wait.until(EC.element_to_be_clickable((By.XPATH,"//label[@for='impressiveRadio']"))).click()
    text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"text-success"))).text

    print("Selected:", text)
    print("TC PASSED")

except:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    name=os.path.splitext(os.path.basename(__file__))[0]
    path=os.path.join(SHOTS_DIR,f"{name}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
