from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"	#первая форма
    # link = "http://suninjuly.github.io/registration2.html"	#вторая форма с багом
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

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
