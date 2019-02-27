import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

driver.get('https://www.google.com/')
print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
print(driver.title)

driver.save_screenshot('search_results.png')

for g_h3 in driver.find_elements_by_css_selector(".g h3"):
    print(g_h3.text)
    
    # print(g_h3.text.encode('cp932', 'ignore').decode('cp932'))  # Windowsのコマンドプロンプトを使う場合

#elements のように複数形にするとリストを取得できます
stats = driver.find_elements_by_id("resultStats")[0].text
print(stats)

driver.quit()
