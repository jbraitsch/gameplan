from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import TestCase
from selenium.webdriver.chrome.options import Options
import time
import os.path
from selenium.webdriver.chrome.service import Service


class UserTestSuccess(TestCase):
    def test_user_registration(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("127.0.0.1:8000/accounts/register")

        driver.implicitly_wait(0.5)

        name_box = driver.find_element(by=By.NAME, value="username")
        email_box = driver.find_element(by=By.NAME, value="email")
        pswd1_box = driver.find_element(by=By.NAME, value="password1")
        pswd2_box = driver.find_element(by=By.NAME, value="password2")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="input")

        name_box.send_keys("test")
        email_box.send_keys("jbraitsc@uccs.edu")
        pswd1_box.send_keys("3edcxsw2")
        pswd2_box.send_keys("3edcxsw2")
        submit_button.click()

        success = driver.find_element_by_xpath("//p [contains( text(), 'Account was created for')]")
        assert success == "Account was created for"

        driver.quit()

class UserTestFail(TestCase):
    def test_password_match(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
        homedir = os.path.expanduser("~")
        webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        driver.get("127.0.0.1:8000/accounts/register")

        driver.implicitly_wait(0.5)

        name_box = driver.find_element(by=By.NAME, value="username")
        email_box = driver.find_element(by=By.NAME, value="email")
        pswd1_box = driver.find_element(by=By.NAME, value="password1")
        pswd2_box = driver.find_element(by=By.NAME, value="password2")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="input")

        name_box.send_keys("test")
        email_box.send_keys("jbraitsc@uccs.edu")
        pswd1_box.send_keys("3edcxsw2")
        pswd2_box.send_keys("3edcvfr4")
        submit_button.click()


        err_msg = driver.find_element_by_xpath("//li [contains( text(), 'The two password fields didn’t match.')]")
        assert err_msg == "The two password fields didn’t match."

        driver.quit()