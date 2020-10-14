from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

PATH = "/usr/local/bin"  # geckodriver path


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(PATH)
        #self.driver.maximize_window()

    def load_instagram(self):
        self.driver.get("http://instagram.com")  # Opens instagram on firefox
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username")))

    def login(self):
        self.load_instagram()
        username_element = self.driver.find_element_by_name('username')
        password_element = self.driver.find_element_by_name('password')
        username_element.send_keys(self.username)
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)

    def quit_browser(self):
        self.driver.quit()


def get_user_data():
    username = input("username: ")
    password = getpass.getpass(prompt="password: ")
    return username, password


if __name__ == "__main__":
    username, password = get_user_data()
    user = User(username, password)
    user.login()
    time.sleep(10)
    user.quit_browser()
