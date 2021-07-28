import unittest
from selenium import webdriver
import time


link1 = "http://suninjuly.github.io/registration1.html"	#первая форма
link2 = "http://suninjuly.github.io/registration2.html"	#вторая форма с багом

def reg(link):
	try: 
		browser = webdriver.Chrome()
		browser.get(link)
	
		# Ваш код, который заполняет обязательные поля
		input1 = browser.find_element_by_css_selector('input.form-control.first[required]')
		input1.send_keys("Ivan")
		time.sleep(1)
	
		input2 = browser.find_element_by_css_selector('input.form-control.second[required]')
		input2.send_keys("Petrov")
		time.sleep(1)
	
		input3 = browser.find_element_by_css_selector('input.form-control.third[required]')
		input3.send_keys("Smolensk@mail.ru")
		time.sleep(1)
	
	
		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
	
		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(5)
	
		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text
		
	
	finally:
		# закрываем браузер после всех манипуляций
		browser.quit()
	return welcome_text
	
class TestReg(unittest.TestCase):
	""" Тестирование регистрационной формы """
	
	def test_reg1(self):
		self.assertEqual(reg(link1), "Congratulations! You have successfully registered!",'Ожидаемый текст не совпал с текстом на странице сайта!')
		
	def test_reg2(self):
		self.assertEqual(reg(link2), "Congratulations! You have successfully registered!",'Ожидаемый текст не совпал с текстом на странице сайта!')


if __name__ == "__main__":
	unittest.main()
