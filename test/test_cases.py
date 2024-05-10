import pytest
from appointment_pack.appointment_page import Make_appoint
from config_pack.needed_datas import Needed_datas
from login_pack.login_page import Login
from menu_pack.menu_options import Menu_class
# from openpyxl.styles import PatternFill
# from datetime import datetime
import time


@pytest.mark.usefixtures("chrome_driver")
class CURA_Health:

    # Test_case_01_Login
    def test_login(self):
        login = Login(self.driver)
        login.login("John Doe", "ThisIsNotAPassword")
        try:
            assert self.current_url() == Needed_datas.appointment_page_url
            print('login successfully done')
        except Exception as e:
            print('login page test_case01 somthing issue', e)


    # Test_case_02_Make Appointment with "Tokyo CURA Healthcare Center" , " Medicare "
    def test_with_medicare(self):
        make_appoint = Make_appoint(self.driver)
        login = Login(self.driver)

        if self.current_url() == Needed_datas.login_page_url:
            login.login("John Doe", "ThisIsNotAPassword")
        else:
            make_appoint.click_to_make_appoint()

            make_appoint.fecility_one()

            make_appoint.check_box()

            make_appoint.click_Medicare()

            make_appoint.date("10/05/2024")

            make_appoint.comment("This is Test_case_02_Make Appointment with Tokyo CURA Healthcare Center, Medicare")

            make_appoint.book_appoint()

        try:
            assert Needed_datas.after_book_the_appoint_url == self.current_url()
            print("Appointment Confirmation")
            print("Test_case_02_Make Appointment with Tokyo CURA Healthcare Center, Medicare")
            time.sleep(2)
            make_appoint.go_to_home_page()
            make_appoint.again_appoint()
            print("another appointment")
        except Exception as e:
            print("test_case 02 is somthing issue", e)


    # Test_case_03_Make Appointment with "Hong kong CURA Healthcare Center" , " Medicaid "
    def test_with_medicaid(self):
        make_appoint = Make_appoint(self.driver)
        login = Login(self.driver)

        if self.current_url() == Needed_datas.login_page_url:
            login.login("John Doe", "ThisIsNotAPassword")
        else:
            make_appoint.click_to_make_appoint()

            make_appoint.fecility_two()

            make_appoint.check_box()

            make_appoint.click_Medicaid()

            make_appoint.date("20/05/2024")

            make_appoint.comment("Test_case_03_Make Appointment withHong kong CURA Healthcare Center, Medicaid")

            make_appoint.book_appoint()

        try:
            assert Needed_datas.after_book_the_appoint_url == self.current_url()
            print("Appointment Confirmation")
            print("Test_case_03_Make Appointment withHong kong CURA Healthcare Center, Medicaid")
            time.sleep(2)
            make_appoint.go_to_home_page()
            make_appoint.again_appoint()
            print("another appointment")
        except Exception as e:
            print("test_case 03 is somthing issue", e)


    # Test_case_04_Make Appointment with "Seoul CURA Healthcare Center", " None "
    def test_with_none(self):
        make_appoint = Make_appoint(self.driver)
        login = Login(self.driver)

        if self.current_url() == Needed_datas.login_page_url:
            login.login("John Doe", "ThisIsNotAPassword")
        else:
            make_appoint.click_to_make_appoint()

            make_appoint.fecility_three()

            make_appoint.check_box()

            make_appoint.click_None()

            make_appoint.date("30/05/2024")

            make_appoint.comment("Test_case_04_Make Appointment with Seoul CURA Healthcare Center, None ")

            make_appoint.book_appoint()

        try:
            assert Needed_datas.after_book_the_appoint_url == self.current_url()
            print("Appointment Confirmation")
            print("Test_case_04_Make Appointment with Seoul CURA Healthcare Center, None ")
            time.sleep(2)
            make_appoint.go_to_home_page()
            make_appoint.again_appoint()
            print("another appointment")
        except Exception as e:
            print("test_case 04 is somthing issue", e)


    # Test_case_05_Make Appointment without click Apply for hospital readmission with " None "
    def test_tc05(self):
        make_appoint = Make_appoint(self.driver)
        login = Login(self.driver)

        if self.current_url() == Needed_datas.login_page_url:
            login.login("John Doe", "ThisIsNotAPassword")
        else:
            make_appoint.click_to_make_appoint()

            make_appoint.fecility_three()

            make_appoint.click_None()

            make_appoint.date("24/06/2024")

            make_appoint.comment("Test_case_05_Make Appointment with Seoul CURA Healthcare Center, None ")

            make_appoint.book_appoint()

        try:
            assert Needed_datas.after_book_the_appoint_url == self.current_url()
            print("Appointment Confirmation")
            print("Test_case_05_Make Appointment with Seoul CURA Healthcare Center, None ")
            time.sleep(2)
            make_appoint.go_to_home_page()
            make_appoint.again_appoint()
            print("another appointment")
        except Exception as e:
            print("test_case 05 is somthing issue", e)


    # Test_case_06_Make Appointment without click Apply for hospital readmission with " None "
    def test_tc06(self):
        make_appoint = Make_appoint(self.driver)
        login = Login(self.driver)

        if self.current_url() == Needed_datas.login_page_url:
            login.login("John Doe", "ThisIsNotAPassword")
        else:
            make_appoint.click_to_make_appoint()

            make_appoint.fecility_three()

            make_appoint.click_None()

            make_appoint.date("14/07/2024")

            make_appoint.comment("Test_case_06_Make Appointment with Seoul CURA Healthcare Center, None ")

            make_appoint.book_appoint()

        try:
            assert Needed_datas.after_book_the_appoint_url == self.current_url()
            print("Appointment Confirmation")
            print("Test_case_06_Make Appointment with Seoul CURA Healthcare Center, None ")
            time.sleep(2)
            make_appoint.go_to_home_page()
            make_appoint.again_appoint()
            print("another appointment")
        except Exception as e:
            print("test_case 06 is somthing issue", e)


    # Test_case_07_Make Appointment without click Apply for hospital readmission with " None "
    def test_tc07(self):
        make_appoint = Make_appoint(self.driver)
        login = Login(self.driver)

        if self.current_url() == Needed_datas.login_page_url:
            login.login("John Doe", "ThisIsNotAPassword")
        else:
            make_appoint.click_to_make_appoint()

            make_appoint.fecility_three()

            make_appoint.click_None()

            make_appoint.date("06/08/2024")

            make_appoint.comment("Test_case_07_Make Appointment with Seoul CURA Healthcare Center, None ")

            make_appoint.book_appoint()

        try:
            assert Needed_datas.after_book_the_appoint_url == self.current_url()
            print("Appointment Confirmation")
            print("Test_case_07_Make Appointment with Seoul CURA Healthcare Center, None ")
            time.sleep(2)
            make_appoint.go_to_home_page()
            make_appoint.again_appoint()
            print("another appointment")
        except Exception as e:
            print("test_case 07 is somthing issue", e)


    # Test_case_08_View the History
    def test_history(self):
        menu_opt = Menu_class(self.driver)
        make_appoint = Make_appoint(self.driver)
        login = Login(self.driver)

        if self.current_url() == Needed_datas.login_page_url:
            login.login("John Doe", "ThisIsNotAPassword")

        else:
            menu_opt.click_history()

            menu_opt.scroll_down()

            time.sleep(2)
            assert Needed_datas.history_page_url == self.current_url()
            print("you views history page")

            Needed_datas.go_to_home_page_lt.is_enabled()

            make_appoint.go_to_home_page()

        if Needed_datas.main_url == self.current_url():
            menu_opt.click_logout()
            print("successfully logout")
        else:
            print("the history test case somthing went wrong")


    # Test_case_09_View the Profile page and Compare with current url
    def test_view_profile(self):
        menu_opt = Menu_class(self.driver)
        login = Login(self.driver)

        if self.current_url() == Needed_datas.login_page_url:
            login.login("John Doe", "ThisIsNotAPassword")
        else:
            menu_opt.click_profile()

            time.sleep(2)
            assert Needed_datas.profile_page_url == self.current_url
            print("you views profile page")
            return menu_opt.click_logout


    # Test_case_10_invalid_credential
    def test_invalid_cred(self):
        login = Login(self.driver)
        login.login("KISHORE", "invalidPASSWORD")
        try:
            assert self.current_url() != Needed_datas.appointment_page_url
            print('Login failed! Please ensure the username and password are valid.')
        except Exception as e:
            print("login page test_case_10 somthing issue", e)

