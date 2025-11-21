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
    driver.get("https://demoqa.com/browser-windows")
    driver.maximize_window()

    main = driver.current_window_handle
    wait.until(EC.element_to_be_clickable((By.ID,"tabButton"))).click()

    wait.until(lambda d: len(d.window_handles) > 1)

    for h in driver.window_handles:
        if h != main:
            driver.switch_to.window(h)
            break

    print("Child Text:", driver.find_element(By.ID,"sampleHeading").text)

    driver.close()
    driver.switch_to.window(main)

    print("TC PASSED")

except Exception:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    path=os.path.join(SHOTS_DIR, f"{os.path.basename(__file__).replace('.py','')}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
