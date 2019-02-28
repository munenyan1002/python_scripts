import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By

#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

driver = webdriver.Chrome()
driver.get('http://spcdev:83/redmine/login?back_url=http%3A%2F%2Fspcdev%3A83%2Fredmine%2Fmy%2Fpage')
print(driver.title)

id_box = driver.find_element_by_name("username")
id_box.send_keys('')
password_box = driver.find_element_by_name("password")
password_box.send_keys('')

login_box = driver.find_element_by_name("login")
login_box.click()
print ("ログイン成功")
driver.quit()
