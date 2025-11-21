import os, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

REPORTS_DIR="reports"
SHOTS_DIR=os.path.join(REPORTS_DIR,"screenshots")
os.makedirs(SHOTS_DIR, exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/select-menu")
    driver.maximize_window()

    dropdown = wait.until(EC.visibility_of_element_located((By.ID,"oldSelectMenu")))
    Select(dropdown).select_by_visible_text("Purple")

    print("Selected Purple from dropdown")
    print("TC PASSED")

except Exception:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    path=os.path.join(SHOTS_DIR, f"{os.path.basename(__file__).replace('.py','')}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
