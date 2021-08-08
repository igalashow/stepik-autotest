import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


# def answer():
	# """ Правильный ответ """
	# return math.log(int(time.time()))
	
answer = []

links = ['https://stepik.org/lesson/236895/step/1',
		'https://stepik.org/lesson/236896/step/1',
		'https://stepik.org/lesson/236897/step/1',
		'https://stepik.org/lesson/236898/step/1',
		'https://stepik.org/lesson/236899/step/1',
		'https://stepik.org/lesson/236903/step/1',
		'https://stepik.org/lesson/236904/step/1',
		'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="function")
def browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome()
	yield browser
	print("\nquit browser..")
	browser.quit()

@pytest.mark.parametrize('link', links)
def test_verify_answer(browser, link):
	linka = f"{link}"
	browser.get(linka)
	WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))).send_keys(str(math.log(int(time.time()))))
	WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))).click()

	message = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint")))
	message_text = message.text
	if message_text != "Correct!":
		answer.append(message_text)
		print(answer)
	assert "Correct!" in message.text
print(''.join(answer))



