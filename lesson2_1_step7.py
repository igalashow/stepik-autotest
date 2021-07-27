import math
from selenium import webdriver
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_css_selector('img').get_attribute('valuex')
	y = calc(x_element)
	
	browser.find_element_by_xpath("//input[@type='checkbox']").click()
	browser.find_element_by_xpath("//input[@id='robotsRule']").click()
	browser.find_element_by_xpath("//input[@id='answer']").send_keys(str(y))
	time.sleep(1)
	browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

