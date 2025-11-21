import os, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
    driver.get("https://demoqa.com/buttons")
    driver.maximize_window()

    actions = ActionChains(driver)

    dbl = driver.find_element(By.ID,"doubleClickBtn")
    actions.double_click(dbl).perform()

    rclick = driver.find_element(By.ID,"rightClickBtn")
    actions.context_click(rclick).perform()

    driver.find_element(By.XPATH,"//button[text()='Click Me']").click()

    print(driver.find_element(By.ID,"doubleClickMessage").text)
    print(driver.find_element(By.ID,"rightClickMessage").text)
    print(driver.find_element(By.ID,"dynamicClickMessage").text)

    print("TC PASSED")

except:
    ts=datetime.datetime.now().strftime("%H%M%S_%d%m%y")
    name=os.path.splitext(os.path.basename(__file__))[0]
    path=os.path.join(SHOTS_DIR,f"{name}_{ts}.png")
    driver.save_screenshot(path)
    raise
finally:
    driver.quit()
