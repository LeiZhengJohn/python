from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

brower = webdriver.Chrome()
try:
    brower.get('https://www.ncbi.nlm.nih.gov/')
    select1 = Select(brower.find_element_by_id('database'))
    select1.select_by_value('gene')
    input = brower.find_element_by_id('term')
    str = 'cancer'
    input.send_keys(str)
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(brower,10)
    wait.until(EC.presence_of_element_located((By.ID,'navcontent')))

    input_page = brower.find_element_by_id('pageno')
    input_page.clear()
    input_page.send_keys(20)
    input_page.send_keys(Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.ID, 'navcontent')))

    html = brower.page_source;
    print(html)
finally:
    print('ok')
    brower.close()