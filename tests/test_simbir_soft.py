import time
import allure
from pages.links import LinkPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.transaction_page import TransactionsPage


class TestTransaction:
    @allure.description("Test get file transactions")
    def test_get_transactions_csv_success(self, browser):

        link = LinkPage().link
        print("\nStart login page")
        browser.maximize_window()
        login = LoginPage(browser, link)
        login.open()
        login.login_to_site()

        deposite_withdraw = MainPage(browser, link)
        deposite_withdraw.add_deposite()
        deposite_withdraw.withdraw()
        deposite_withdraw.click_btn_transactions()

        transaction = TransactionsPage(browser, link)
        transaction.do_csv()

    print("Finish Tests")
    time.sleep(1)
