from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_pack.needed_datas import Needed_datas
from selenium.webdriver.support.select import Select


class Make_appoint:

    def __init__(self, driver):
        self.driver = driver

    # for click to make an appointment page for the form filling
    def click_to_make_appoint(self):
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, Needed_datas.make_appoint_lt))).click()

    # for click login via menu bar
    def click_login_from_menubar(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.menu_line_btn_id))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, Needed_datas.login_lt_in_menu))).click()

    # for "if need 'Tokyo CURA Healthcare Center drop down' "
    def fecility_one(self):
        one= Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.facility_id))))
        one.select_by_visible_text('Tokyo CURA Healthcare Center')
        print('you selected Tokyo CURA Healthcare Center')

    # for "if need 'Hongkong CURA Healthcare Center' "
    def fecility_two(self):
        two = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.facility_id))))
        two.select_by_visible_text('Hongkong CURA Healthcare Center')
        print('you selected Hong kong CURA Healthcare Center')

    # for "if need 'Seoul CURA Healthcare Center' "
    def fecility_three(self):
        three = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.facility_id))))
        three.select_by_visible_text('Seoul CURA Healthcare Center')
        print('you selected Seoul CURA Healthcare Center')

    # for click the "Apply for hospital readmission" checkbox
    def check_box(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.apply_checkbox_id))).click()
        print('CheckBox selected')

    # for if need Medicare radio btn
    def click_Medicare(self):
        print('This is Medicare')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Needed_datas.healthcare_program_radio1_xp))).click()

    # for if need Medicaid radio btn
    def click_Medicaid(self):
        print('This is Medicaid')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Needed_datas.healthcare_program_radio2_xp))).click()

    # for if need None radio btn
    def click_None(self):
        print('This is None')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Needed_datas.healthcare_program_radio3_xp))).click()

    # enter the "Appointment or Visit Date" manually with (dd/mm/yyyy)
    def date(self,ddmmyyyy):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Needed_datas.healthcare_program_radio3_xp))).send_keys(ddmmyyyy)
        print('the date is: ', ddmmyyyy)

    # for Enter the comments for what purpose
    def comment(self,lines):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Needed_datas.comments_text_id))).send_keys(lines)
        print('the comment is: ',lines)

    #for click the btn book appointment
    def book_appoint(self):
        Needed_datas.go_to_home_page_lt.is_enabled()

    def again_appoint(self):
        main_url.is_displayed()
        return self.click_to_make_appoint()

    def go_to_home_page(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, Needed_datas.go_to_home_page_lt))).send_keys(lines)
