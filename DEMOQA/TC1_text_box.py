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
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()

    wait.until(EC.visibility_of_element_located((By.ID,"userName"))).send_keys("Vikas Chaudhary")
    driver.find_element(By.ID,"userEmail").send_keys("vikas@test.com")
    driver.find_element(By.ID,"currentAddress").send_keys("Vapi, Gujarat")
    driver.find_element(By.ID,"permanentAddress").send_keys("India")

    submit = driver.find_element(By.ID,"submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)
    submit.click()

    out = wait.until(EC.visibility_of_element_located((By.ID,"output"))).text
    print("Output:", out)
    print("TC PASSED")

except Exception as e:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    name=os.path.splitext(os.path.basename(__file__))[0]
    path=os.path.join(SHOTS_DIR,f"{name}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
