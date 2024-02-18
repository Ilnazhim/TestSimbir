import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure
from base.base_class import BaseClass


class MainPage(BaseClass):

    # Locators
    btn_deposit = "//button[@ng-click='deposit()']"
    btn_withdrawl = "//button[@ng-click='withdrawl()']"
    btn_transactions = "//button[@ng-click='transactions()']"
    input_amount = "//input[@ng-model='amount']"
    btn_submit = "//button[@type='submit']"
    success_text = "//span[@ng-show='message']"
    balance_text = "//div[@ng-hide='noAccount']/strong[2]"

    # Getters
    def get_btn_deposit(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_deposit)))

    def get_btn_withdrawl(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_withdrawl)))

    def get_btn_transactions(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_transactions)))

    def get_input_amount(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_amount)))

    def get_btn_submit(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_submit)))

    def get_success_text(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.success_text)))

    def get_balance_text(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.balance_text)))

    # Actions
    def click_btn_deposit(self):
        self.get_btn_deposit().click()
        print("Click btn_deposit")

    def click_btn_withdrawl(self):
        self.get_btn_withdrawl().click()
        print("Click btn_withdrawl")

    def click_btn_transactions(self):
        self.get_btn_transactions().click()
        print("Click btn_transactions")

    def input_input_amount(self):
        self.get_input_amount().send_keys(BaseClass.return_amount())
        print("input_amount")

    def click_btn_submit(self):
        self.get_btn_submit().click()
        print("Click btn_submit_deposit")

    # Metods
    def add_deposite(self):
        with allure.step("Add deposite"):
            Logger.add_start_step(method="Add deposite")
            self.click_btn_deposit()
            self.input_input_amount()
            self.click_btn_submit()
            self.assert_word(self.get_success_text(), "Deposit Successful")
            Logger.add_end_step(url=self.browser.current_url, method="Add deposite")

    def withdraw(self):
        with allure.step("Add withdraw"):
            Logger.add_start_step(method="withdraw")
            self.click_btn_withdrawl()
            time.sleep(1)
            self.input_input_amount()
            self.click_btn_submit()
            self.assert_word(self.get_balance_text(), "0")
            Logger.add_end_step(url=self.browser.current_url, method="withdraw")
