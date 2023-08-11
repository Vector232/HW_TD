from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import os
from dotenv import load_dotenv
import time

load_dotenv()

class TestLogin:
    def test_loginYandex(self):
        driver = webdriver.Chrome()

        
        driver.maximize_window()
        driver.get(f'https://passport.yandex.ru/auth/')

        assert driver.find_element('id', 'passp-field-login')

        email_input = driver.find_element('id', 'passp-field-login')

        email_input.clear()
        for l in 'email@mail.com':
            email_input.send_keys(l)
            time.sleep(0.1)
        driver.find_element('id', 'passp:sign-in').click()
        time.sleep(1)

        assert driver.find_element('id', 'passp-field-login')
        assert driver.find_element('id', 'field:input-login:hint').text == 'Такой логин не подойдет'

        email_input.send_keys(Keys.CONTROL + "a")
        email_input.send_keys(Keys.DELETE)
        for l in os.getenv('login'):
            email_input.send_keys(l)
            time.sleep(0.1)
        driver.find_element('id', 'passp:sign-in').click()
        time.sleep(1)

        assert driver.find_element('id', 'passp-field-passwd')
        
        password_input = driver.find_element('id', 'passp-field-passwd')
        password_input.clear()
        for l in 'password':
            password_input.send_keys(l)
            time.sleep(0.1)
        driver.find_element('id', 'passp:sign-in').click()
        time.sleep(1)
        
        assert driver.find_element('id', 'passp-field-passwd')
        assert driver.find_element('id', 'field:input-passwd:hint').text == 'Неверный пароль'

        password_input.send_keys(Keys.CONTROL + "a")
        password_input.send_keys(Keys.DELETE)
        for l in os.getenv('password'):
            password_input.send_keys(l)
            time.sleep(0.1)
        driver.find_element('id', 'passp:sign-in').click()
        time.sleep(1)
        
        driver.close()
        driver.quit()


if __name__ == '__main__':
    pytest.main(["-vv"])
