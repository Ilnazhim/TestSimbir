from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure
from base.base_class import BaseClass


class LoginPage(BaseClass):

    # Locators
    btn_customer_login = "//button[@ng-click='customer()']"
    harry_login = "//option[text()='Harry Potter']"
    btn_login = "//button[@class='btn btn-default']"
    assert_text = "//span[@class='fontBig ng-binding']"

    # Getters
    def get_btn_customer_login(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_customer_login)))

    def get_harry_login(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.harry_login)))

    def get_btn_login(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_login)))

    def get_assert_text(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_text)))

    # Actions
    def click_btn_customer_login(self):
        self.get_btn_customer_login().click()
        print("Click customer_login")

    def click_harry_login(self):
        self.get_harry_login().click()
        print("Click harry_login")

    def click_btn_login(self):
        self.get_btn_login().click()
        print("Click btn_login")

    # Metods
    def login_to_site(self):
        """Login to site"""
        with allure.step("Login to site"):
            Logger.add_start_step(method="Login to site by Harry Potter")

            self.click_btn_customer_login()
            self.click_harry_login()
            self.click_btn_login()
            self.assert_word(self.get_assert_text(), "Harry Potter")

            Logger.add_end_step(url=self.browser.current_url, method="Login to site by Harry Potter")
