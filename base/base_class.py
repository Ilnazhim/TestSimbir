import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException


class BaseClass:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Metod open browser"""
        self.browser.get(self.url)

    def get_current_url(self):
        """Metod get current url"""
        get_url = self.browser.current_url
        print(get_url)

    def assert_word(self, word, result):
        """Metod assert word"""
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def is_element_present(self, how, what):
        """Metod is element present"""
        try:
            WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((how, what)))
            print("Assert element is present")
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


    def get_screenshot(self):
        """Metod screenshot"""
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.browser.save_screenshot("C:\\Users\\ilnazhim\\environments\\StepikAlexFinishProject\\screen\\" + name_screenshot)
        print("Screenshot")


    def assert_url(self, result):
        """Metod assert url"""
        get_url = self.browser.current_url
        assert get_url == result
        print("Good value url")

    def return_amount():
        date_now = int(datetime.datetime.utcnow().strftime('%d')) + 1
        def fibonacci_recursive(n):
            if n <= 1:
                return n
            else:
                return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        return fibonacci_recursive(date_now)

    print(return_amount())
