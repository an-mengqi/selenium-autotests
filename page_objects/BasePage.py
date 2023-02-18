
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Did not wait for the element to be visible: {locator}")

    def input_value(self, locator, value):
        """Input value in a field"""
        self.element(locator).send_keys(value)

    def click_element(self, locator):
        """Click on the element"""
        self.element(locator).click()

    def find_element(self, locator):
        return self.element(locator)

    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def get_element_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def find_all_elements(self, locator):
        return
