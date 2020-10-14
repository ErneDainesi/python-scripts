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

    def wait_for_element(self, tag, value):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((tag, value)))
        except:
            self.quit_browser()

    def wait_for_clickable(self, tag, value):
        try:
            WebDriverWait(self.driver,
                          10).until(EC.element_to_be_clickable(
                              (tag, value))).click()
        except:
            self.quit_browser()

    def load_instagram(self):
        self.driver.get("http://instagram.com")  # Opens instagram on firefox
        self.wait_for_element(By.NAME, "username")

    def login(self):
        self.load_instagram()
        username_element = self.driver.find_element_by_name('username')
        password_element = self.driver.find_element_by_name('password')
        username_element.send_keys(self.username)
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)

    def close_pop_ups(self):
        self.wait_for_element(By.CLASS_NAME, "cmbtv")
        self.wait_for_clickable(
            By.XPATH, "//button[@class='sqdOP yWX7d    y3zKF     ']")
        self.wait_for_element(By.CLASS_NAME, "mt3GC")
        self.wait_for_clickable(By.XPATH, "//button[@class='aOOlW   HoLwm ']")

    def got_to_profile(self):
        self.close_pop_ups()

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
    user.got_to_profile()
