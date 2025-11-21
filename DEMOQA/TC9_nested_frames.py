import os, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

REPORTS_DIR="reports"
SHOTS_DIR=os.path.join(REPORTS_DIR,"screenshots")
os.makedirs(SHOTS_DIR, exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://demoqa.com/nestedframes")
    driver.maximize_window()

    driver.switch_to.frame("frame1")
    parent = driver.find_element(By.TAG_NAME, "body").text

    child_iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(child_iframe)
    child = driver.find_element(By.TAG_NAME, "p").text

    driver.switch_to.default_content()

    print("Parent Frame Text:", parent)
    print("Child Frame Text:", child)
    print("TC PASSED")

except Exception:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    path=os.path.join(SHOTS_DIR, f"{os.path.basename(__file__).replace('.py','')}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
