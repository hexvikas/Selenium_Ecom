import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Screenshot setup
REPORTS_DIR = "reports"
SHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
os.makedirs(SHOTS_DIR, exist_ok=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.google.com")
    driver.maximize_window()

    search = driver.find_element(By.NAME, "q")
    search.send_keys("Selenium Python")
    search.send_keys(Keys.ENTER)

    results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]

    print("\nTop 5 Results:")
    for r in results:
        print(r.text)

    print("TC PASSED")

except Exception as e:
    ts = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
    tc_name = os.path.splitext(os.path.basename(__file__))[0]
    shot_name = f"{tc_name}_{ts}.png"
    shot_path = os.path.join(SHOTS_DIR, shot_name)

    driver.save_screenshot(shot_path)
    print(f"Screenshot saved: {shot_path}")

    raise

finally:
    driver.quit()
