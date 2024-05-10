from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_pack.needed_datas import Needed_datas


class Login:

    def __init__(self, driver):
        self.driver = driver

    # for login method
    def login(self, u_name, p_word):

        username = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, Needed_datas.user_name_id)))
        username.send_keys(u_name)
        password = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, Needed_datas.password_id)))
        password.send_keys(p_word)
        press_login_btn = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, Needed_datas.login_btn_id)))
        press_login_btn.click()

        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert.accept()  # Accept the alert
        except:
            pass

        driver.implicitly_wait(20)
