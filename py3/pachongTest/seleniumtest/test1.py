from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_1 = browser.find_element_by_id('q')
input_2 = browser.find_element_by_css_selector('#q')
input_3 = browser.find_element_by_xpath('//*[@id="q"]')
input_4 = browser.find_element(By.ID,'q')
print(input_1)
print(input_2)
print(input_3)
print(input_4)
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
lis1 = browser.find_elements_by_css_selector('.service-bd li')
lis2 = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(lis1)
print(lis2)
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
input_1.send_keys('iPhone')
time.sleep(3)
input_1.clear()
input_1.send_keys('iPad')
button_1 = browser.find_element_by_class_name('btn-search')
button_1.click()

browser.close()

browser1 = webdriver.Chrome()
url1 = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser1.get(url1)
browser1.switch_to.frame('iframeResult')
source = browser1.find_element_by_css_selector('#draggable')
target = browser1.find_element_by_css_selector('#droppable')
action = ActionChains(browser1)
action.drag_and_drop(source,target)
action.perform()