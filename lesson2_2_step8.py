import os
from selenium import webdriver
import time

try: 
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	input1 = browser.find_element_by_xpath("//input[@name='firstname']")
	input1.send_keys("Petr")

	input2 = browser.find_element_by_xpath("//input[@name='lastname']")
	input2.send_keys("Sidorov")

	input3 = browser.find_element_by_xpath("//input[@name='email']")
	input3.send_keys("sidorov@pochta.ru")


	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, '11.txt')           # добавляем к этому пути имя файла 
	element = browser.find_element_by_xpath("//input[@id='file']")
	element.send_keys(file_path)
	
	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

# def calc(x):
	# return str(math.log(abs(12*math.sin(int(x)))))

# try: 
	# link = "http://suninjuly.github.io/execute_script.html"
	# browser = webdriver.Chrome()
	# browser.get(link)

	# x_element = browser.find_element_by_css_selector('span#input_value').text
	# y = calc(x_element)

	# answer = browser.find_element_by_xpath("//input[@id='answer']")
	# browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
	# browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)

	# browser.find_element_by_xpath("//input[@type='checkbox']").click()
	# browser.find_element_by_xpath("//input[@id='robotsRule']").click()
	# time.sleep(1)
	
	# # находим элемент button
	# button = browser.find_element_by_tag_name("button")
	# # скроллим до элемента button
	# browser.execute_script("return arguments[0].scrollIntoView(true);", button)

	# browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

