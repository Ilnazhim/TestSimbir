from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
import allure
from base.base_class import BaseClass


class TransactionsPage(BaseClass):

    # Locators
    credit_transaction_date = "//tr[@id='anchor0'] //td[1]"
    credit_transaction_amount = "//tr[@id='anchor0'] //td[2]"
    credit_transaction_type = "//tr[@id='anchor0'] //td[3]"

    debit_transaction_date = "//tr[@id='anchor1'] //td[1]"
    debit_transaction_amount = "//tr[@id='anchor1'] //td[2]"
    debit_transaction_type = "//tr[@id='anchor1'] //td[3]"

    # Getters
    def get_credit_transaction_date(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.credit_transaction_date)))

    def get_credit_transaction_amount(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.credit_transaction_amount)))

    def get_credit_transaction_type(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.credit_transaction_type)))

    def get_debit_transaction_date(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.debit_transaction_date)))

    def get_debit_transaction_amount(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.debit_transaction_amount)))

    def get_debit_transaction_type(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.debit_transaction_type)))

    # Metods
    def do_csv(self):
        with allure.step("Check transaction and make file.csv"):
            Logger.add_start_step(method="Add file")

            filename = "file.csv"
            try:
                with open(filename, "w+") as file:
                    file.write(self.get_credit_transaction_date().text + ' ')
                    file.write(self.get_credit_transaction_amount().text + ' ')
                    file.write(self.get_credit_transaction_type().text + '\n')
                    file.write(self.get_debit_transaction_date().text + ' ')
                    file.write(self.get_debit_transaction_amount().text + ' ')
                    file.write(self.get_debit_transaction_type().text)
            except:
                self.browser.refresh()
                with open(filename, "w+") as file:
                    file.write(self.get_credit_transaction_date().text + ' ')
                    file.write(self.get_credit_transaction_amount().text + ' ')
                    file.write(self.get_credit_transaction_type().text + '\n')
                    file.write(self.get_debit_transaction_date().text + ' ')
                    file.write(self.get_debit_transaction_amount().text + ' ')
                    file.write(self.get_debit_transaction_type().text)
            allure.attach.file("C:\\Users\\ilnazhim\\environments\\SimbirSoft\\file.csv", attachment_type=allure.attachment_type.CSV)
            Logger.add_end_step(url=self.browser.current_url, method="Add file")
