import allure
import datetime
import logging
import os
import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="choose browser: chrome, firefox, yandex")
    parser.addoption("--driver_folder", default=os.path.expanduser("~/otus/drivers"))
    parser.addoption("--url", action="store", default="http://192.168.0.15:8081")
    parser.addoption("--log_level", action="store", default="DEBUG")

    parser.addoption("--executor", action="store", default="192.168.0.15")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--logs", action="store_true")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    mobile = request.config.getoption("--mobile")
    logs = request.config.getoption("--logs")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    # file_handler = logging.FileHandler(f"selenium-autotests/logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": _browser
    }

    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    if not mobile:
        driver.maximize_window()

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    driver.local_url = url
    driver.admin_url = driver.local_url + "/admin"
    driver.registration_url = driver.local_url + "/index.php?route=account/register"

    def finalizer():
        driver.quit()

    request.addfinalizer(finalizer)
    return driver
