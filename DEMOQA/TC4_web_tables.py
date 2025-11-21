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
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()

    driver.find_element(By.ID,"addNewRecordButton").click()

    wait.until(EC.visibility_of_element_located((By.ID,"firstName"))).send_keys("Vikas")
    driver.find_element(By.ID,"lastName").send_keys("Chaudhary")
    driver.find_element(By.ID,"userEmail").send_keys("vikas@demo.com")
    driver.find_element(By.ID,"age").send_keys("27")
    driver.find_element(By.ID,"salary").send_keys("50000")
    driver.find_element(By.ID,"department").send_keys("QA")

    driver.find_element(By.ID,"submit").click()

    driver.find_element(By.ID,"searchBox").send_keys("vikas")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[id^='edit-record']"))).click()
    age = driver.find_element(By.ID,"age")
    age.clear()
    age.send_keys("28")

    driver.find_element(By.ID,"submit").click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[id^='delete-record']"))).click()

    print("WebTables operations done.")
    print("TC PASSED")

except:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    name=os.path.splitext(os.path.basename(__file__))[0]
    path=os.path.join(SHOTS_DIR,f"{name}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
