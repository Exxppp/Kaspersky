import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def browser_setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager(path=r".\\Drivers").install()), options=options)
    browser.maximize_window()
    return browser


@pytest.fixture(scope="function")
def browser():
    browser = browser_setup()
    yield browser
    browser.quit()


@pytest.fixture(scope="class")
def browser_class():
    browser = browser_setup()
    yield browser
    browser.quit()
