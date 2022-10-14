import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox or edge")


def browser_setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager(path=r".\\Drivers").install()),
                                   options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager(path=r".\\Drivers").install()))
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager(path=r".\\Drivers").install()),
                                 options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.maximize_window()
    return browser


@pytest.fixture(scope="function")
def browser(request):
    browser = browser_setup(request)
    yield browser
    browser.quit()


@pytest.fixture(scope="class")
def browser_class(request):
    browser = browser_setup(request)
    yield browser
    browser.quit()
