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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/frames")
    driver.maximize_window()

    driver.switch_to.frame("frame1")
    f1_text = wait.until(EC.visibility_of_element_located((By.ID,"sampleHeading"))).text
    driver.switch_to.default_content()

    driver.switch_to.frame("frame2")
    f2_text = driver.find_element(By.ID,"sampleHeading").text
    driver.switch_to.default_content()

    print("Frame 1 text:", f1_text)
    print("Frame 2 text:", f2_text)
    print("TC PASSED")

except Exception:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    path=os.path.join(SHOTS_DIR, f"{os.path.basename(__file__).replace('.py','')}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
