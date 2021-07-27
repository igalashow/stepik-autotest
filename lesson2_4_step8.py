from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)

# говорим Selenium проверять в течение 15 секунд
	price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
	
	browser.find_element_by_xpath("//button[@id='book']").click()

	x_element = browser.find_element_by_css_selector('#input_value')
	x = x_element.text
	y = calc(x)
	browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)

	
	browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(5)
	# закрываем браузер после всех манипуляций
	browser.quit()

