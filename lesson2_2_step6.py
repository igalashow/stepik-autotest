import math
from selenium import webdriver
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_css_selector('span#input_value').text
	y = calc(x_element)

	answer = browser.find_element_by_xpath("//input[@id='answer']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
	browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)

	browser.find_element_by_xpath("//input[@type='checkbox']").click()
	browser.find_element_by_xpath("//input[@id='robotsRule']").click()
	time.sleep(1)
	
	# находим элемент button
	button = browser.find_element_by_tag_name("button")
	# скроллим до элемента button
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)

	browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

