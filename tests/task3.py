from selenium import webdriver
import pytest

class TestLogin:
    def test_loginYandex(self):
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get(f'https://passport.yandex.ru/auth/')


if __name__ == '__main__':
    pytest.main(["-vv"])
