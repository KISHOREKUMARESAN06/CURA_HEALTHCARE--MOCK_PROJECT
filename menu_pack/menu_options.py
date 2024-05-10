from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_pack.needed_datas import Needed_datas
from selenium.webdriver.support.select import Select


class Menu_class:

    def __init__(self, driver):
        self.driver = driver

    # for go to home page again
    def click_home(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.menu_line_btn_id))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, Needed_datas.home_lt))).click()

    # for view the histories on the history page
    def click_history(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.menu_line_btn_id))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, Needed_datas.history_lt))).click()

    # click after view the all histories
    def history_page(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, Needed_datas.go_to_home_page_lt))).click()

    # view profiles
    def click_profile(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.menu_line_btn_id))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, Needed_datas.profile_lt))).click()

    # finally logout method
    def click_logout(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.menu_line_btn_id))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.login_btn_id))).click()

    # for scroll down when we needed
    def scroll_down(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'CURA Healthcare Service').send_keys(Keys.PAGE_DOWN)))

