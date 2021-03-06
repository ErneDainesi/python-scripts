from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass

PATH = "/usr/local/bin"  # geckodriver path


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.__driver = webdriver.Firefox(PATH)
        # self.driver.maximize_window()

    def __wait_for_element(self, tag, value):
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((tag, value)))
        except:
            self.quit_browser()

    def __wait_for_clickable(self, tag, value):
        try:
            WebDriverWait(self.__driver,
                          10).until(EC.element_to_be_clickable(
                              (tag, value))).click()
        except:
            self.quit_browser()

    def __load_instagram(self):
        self.__driver.get("http://instagram.com")  # Opens instagram on firefox
        self.__wait_for_element(By.NAME, "username")

    def login(self):
        self.__load_instagram()
        username_element = self.__driver.find_element_by_name('username')
        password_element = self.__driver.find_element_by_name('password')
        username_element.send_keys(self.username)
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)

    def __close_pop_ups(self):
        self.__wait_for_element(By.CLASS_NAME, "cmbtv")
        self.__wait_for_clickable(
            By.XPATH, "//button[@class='sqdOP yWX7d    y3zKF     ']")
        self.__wait_for_element(By.CLASS_NAME, "mt3GC")
        self.__wait_for_clickable(By.XPATH,
                                  "//button[@class='aOOlW   HoLwm ']")

    def got_to_profile(self):
        self.__close_pop_ups()
        self.__wait_for_clickable(By.XPATH, "//span[@class='_2dbep qNELH']")
        self.__wait_for_clickable(By.XPATH, "//a[@class='-qQT3']")

    def get_followers(self):
        num_f_xpath = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"
        self.__wait_for_element(By.XPATH, num_f_xpath)
        number_of_followers = int(
            self.__driver.find_element_by_xpath(num_f_xpath).text)
        self.__wait_for_clickable(By.XPATH, "//a[@class='-nal3 ']")
        self.__wait_for_element(By.XPATH, "//div[@class='PZuss']")
        dialog = self.__driver.find_element_by_xpath("//div[@class='isgrP']")
        scrolling_times = (number_of_followers // 6)
        xpath = "/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a"
        #  coords = follower.location_once_scrolled_into_view
        for x in range(1, number_of_followers + 1):
            try:
                follower = self.__driver.find_element_by_xpath(xpath.format(x))
                print(f"{x}. {follower.text}")
            except:
                self.__driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                    dialog)
                time.sleep(1)
        #  self.__driver.execute_script("window.scrollTo(0, {})".format(
        #      coords['y']))
        #  for x in range(1, number_of_followers + 1):
        #      follower = self.__driver.find_element_by_xpath(xpath.format(x))
        #      self.followers.append(follower.text)

    def quit_browser(self):
        self.__driver.quit()


def get_user_data():
    username = input("username: ")
    password = getpass.getpass(prompt="password: ")
    return username, password


if __name__ == "__main__":
    username, password = get_user_data()
    user = User(username, password)
    user.login()
    user.got_to_profile()
    user.get_followers()
