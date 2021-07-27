from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(num1, num2):
	return str(int(num1)+int(num2))

try: 
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	num1_element = browser.find_element_by_css_selector('span#num1')
	num1 = num1_element.text
	num2_element = browser.find_element_by_css_selector('span#num2')
	num2 = num2_element.text

	summ = calc(num1, num2)
	
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(summ)
	
	time.sleep(1)
	browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

