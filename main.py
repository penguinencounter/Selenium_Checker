from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
import time, os

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://contacts.google.com/directory")
ActionChains(driver).send_keys("milesl16519@stu.powayusd.com"+Keys.ENTER).perform()
print("Ready for capcha. Press enter when you get to MyPlan.")
input('> ')
ActionChains(driver).send_keys(os.environ['username']+Keys.TAB+os.environ['password']+Keys.ENTER).perform()
while True:
    try:
        input("> enter when ready")
        zoom = ActionChains(driver)
        zoom.key_down(Keys.CONTROL)
        zoom.send_keys('----------')
        zoom.key_up(Keys.CONTROL)
        zoom.perform()
        currentPosition = 0
        for x in range(100):
            checkboxes = driver.find_elements(By.CSS_SELECTOR, '.lpAxT.v2jl3d')
            # print(f"There are {len(checkboxes)} checkboxes")
            for checkbox in checkboxes:
                match = checkbox.find_elements(By.CSS_SELECTOR, '.XF89yf.KNwGSe.zYQnTe > .mfjUMc.psZcEd.E6Tb7b > .lpAxT.v2jl3d > .wBLdZd.RTiFqe.cdByRd.NSy2Hd')
                if len(match) > 0:
                    # print(len(match))
                    currentPosition += 40
                    continue
                driver.execute_script('arguments[0].click();', checkbox)
                currentPosition += 30
                pass
            box = driver.find_element(By.CSS_SELECTOR,'.eejsDc.SSPGKf.zQTmif')
            driver.execute_script('arguments[0].scroll(0, arguments[1])', box, currentPosition)
            print('Scrolling')
            time.sleep(0.5)
        
    except Exception as e:
        input(f'(error) : {e}');
