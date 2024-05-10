import pytest
from selenium import webdriver
from config_pack.needed_datas import Needed_datas
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


driver = None
driver_path = ("C:\z.selenium drivers\chromedriver-win64\chromedriver.exe")
main_url = "https://katalon-demo-cura.herokuapp.com/"

@pytest.fixture(scope="class")
def chrome_driver(request):

    # Setup Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(main_url)
    request.cls.driver = main_url

    yield driver
    # Teardown Chrome driver
    driver.quit()

