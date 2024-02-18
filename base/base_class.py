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

    def get_screenshot(self):
        """Metod screenshot"""
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.browser.save_screenshot("C:\\Users\\ilnazhim\\environments\\SimbirSoft\\screen\\" + name_screenshot)
        print("Screenshot")

    def return_amount():
        date_now = int(datetime.datetime.utcnow().strftime('%d')) + 1
        def fibonacci_recursive(n):
            if n <= 1:
                return n
            else:
                return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        return fibonacci_recursive(date_now)
