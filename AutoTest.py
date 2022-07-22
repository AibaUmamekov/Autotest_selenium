from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import requests


class TestCaseAttractor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_form_auth(self):
        # находим форму регистрации и нажимаем на нее
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        form_auth = driver.find_element(By.LINK_TEXT, 'Form Authentication')
        form_auth.click()

        # вводим имя и пароль
        username = driver.find_element(By.ID, 'username')
        username.send_keys('tomsmith')

        password = driver.find_element(By.ID, 'password')
        password.send_keys('SuperSecretPassword!')

        # нажимаем кнопку логин
        login = driver.find_element(By.CLASS_NAME, 'radius')
        login.click()

        # выходим из логина
        logout = driver.find_element(By.LINK_TEXT, 'Logout')
        logout.click()
        print("Test Form Authentication is complete")

    def test_dropdown(self):
        # находим ссылку на выпадающий список
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        dropdown = driver.find_element(By.LINK_TEXT, 'Dropdown')
        dropdown.click()

        # выбираем option 1
        select1 = driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[2]')
        select1.click()
        print("Test Dropdown is complete")

    def test_key_presser(self):
        # находим ссылку кликера и нажимаем на нее
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        key_presses = driver.find_element(By.LINK_TEXT, 'Key Presses')
        key_presses.click()

        # находим поле ввода и нажимаем на любой символ в верхнем регистре
        input_form = driver.find_element(By.ID, 'target')
        test_keys = str(input('Press any key: '))
        input_form.send_keys(test_keys)
        # извлекаем текст из элемента и сравниваем его с введенным ранее символом
        entered = driver.find_element(By.XPATH, '//*[@id="result"]')
        entered_element = entered.get_attribute('innerHTML')
        e = entered_element.split()
        if e[-1] == test_keys:
            print('Entered keys is equal with result')
        else:
            print('failed')

    def test_file_download(self):
        # находим ссылку cкачать файл и нажимаем на нее
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        file_downloader = driver.find_element(By.LINK_TEXT, 'File Download')
        file_downloader.click()
        # находим ссылку на файл test1.txt и берем из него ссылку
        file_link = driver.find_element(By.LINK_TEXT, 'test1.txt').get_attribute('href')
        # извлекаем название файла из ссылки
        file_name = file_link.split('/')[-1]
        # с помощью библиотеки request берем ссылку для скачивания файла и сохраняем его в корневую папку программы
        r = requests.get(file_link, allow_redirects=True)
        open(file_name, 'wb').write(r.content)
        # считываем файл и сравниваем его с проверяемым словом
        f = open("test1.txt", 'r')
        a = f.read()
        if a == 'Wikivoyage':
            print('Word in test1.txt same')
        else:
            print('No find word')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

