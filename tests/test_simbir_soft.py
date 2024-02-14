import time
import allure
from pages.cafe import CafePage



#@allure.description("Test select product 1")
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_login(browser):

    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    print("\nStart login page")
    browser.maximize_window()
    login = LoginPage(browser, link)
    login.open()
    login.login_to_site()

    deposite = MainPage(browser, link)
    deposite.add_deposite()




    print("Finish Tests")
    time.sleep(1)
