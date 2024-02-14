import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.links import LinkPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser():

    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(chrome_options=options)

    yield browser
    browser.quit()
    print("\nquit browser..")
