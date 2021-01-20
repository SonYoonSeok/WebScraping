import time
import random
from selenium import webdriver

executable_path = './chromedriver.exe'
driver = webdriver.Chrome(executable_path = executable_path)
time.sleep(random.uniform(1, 3))

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "dbstjr5517", pw = "lpko1234!!")

time.sleep(random.uniform(1, 3))
driver.execute_script(input_js)
time.sleep(random.uniform(1, 3))
driver.find_element_by_id("log.login").click()