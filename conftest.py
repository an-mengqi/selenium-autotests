import os
import pytest

from selenium import webdriver
from webdriver_manager.opera import OperaDriver
from webdriver_manager import opera
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default = "chrome", help = "choose browser: chrome, firefox, yandex"
    )
    parser.addoption(
        "--driver_folder", default = os.path.expanduser("~/drivers")
    )

@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")
    driver = None

    if _browser == "firefox" or _browser == "ff":
        driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox", executable_path=f"{driver_folder}{os.sep}geckodriver")
    elif _browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{driver_folder}{os.sep}chromedriver")
    elif _browser == "yandex":
        driver = webdriver.Chrome(executable_path=f"{driver_folder}{os.sep}yandexdriver")

    driver.maximize_window()
    yield driver
    driver.close()
