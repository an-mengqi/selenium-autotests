import allure
import datetime
import logging
import os
import pytest
import requests
import time

from selenium import webdriver


@allure.step("Waiting for availability {url}")
def wait_url_data(url, timeout=10):
    """Wait fur url availability"""
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url:
                return response.content
            else:
                return response.text
    return None


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
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    video = request.config.getoption("--video")
    mobile = request.config.getoption("--mobile")
    logs = request.config.getoption("--logs")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": _browser,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": video
        }}

    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    if not mobile:
        driver.maximize_window()

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    def finalizer():
        log_url = f"{executor}/logs/{driver.session_id}.log"
        video_url = f"http://{executor}:8080/video/{driver.session_id}.mp4"
        driver.quit()

        if request.node.status != 'passed':
            if logs:
                allure.attach(
                    name="selenoid_log_" + driver.session_id,
                    body=wait_url_data(log_url),
                    attachment_type=allure.attachment_type.TEXT)
            if video:
                allure.attach(
                    body=wait_url_data(video_url),
                    name="video_for_" + driver.session_id,
                    attachment_type=allure.attachment_type.MP4)

        if video and wait_url_data(video_url):
            requests.delete(url=video_url)

        if logs and wait_url_data(log_url):
            requests.delete(url=log_url)

    request.addfinalizer(finalizer)
    return driver
