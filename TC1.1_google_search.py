import os
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# ================================
# Prepare Screenshot Directory
# ================================
REPORTS_DIR = "reports"
SHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
os.makedirs(SHOTS_DIR, exist_ok=True)

# ================================
# Launch Browser
# ================================
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # ================================
    #       TEST STEPS
    # ================================
    driver.get("https://www.google.com")
    driver.maximize_window()

    print("Page Title:", driver.title)
    print("TC PASSED")   # important for logs

# ================================
#      ON FAILURE → TAKE SCREENSHOT
# ================================
except Exception as e:
    ts = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
    tc_name = os.path.splitext(os.path.basename(__file__))[0]
    shot_name = f"{tc_name}_{ts}.png"
    shot_path = os.path.join(SHOTS_DIR, shot_name)

    driver.save_screenshot(shot_path)
    print(f"Screenshot saved: {shot_path}")
    
    raise   # VERY IMPORTANT → ensures FAIL shows in report

# ================================
# Always close browser
# ================================
finally:
    driver.quit()
