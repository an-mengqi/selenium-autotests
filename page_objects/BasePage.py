
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
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def _input_value(self, locator, value):
        """Input value in a field"""
        self.element(locator).send_keys(value)

    def _click_element(self, locator):
        """Click on the element"""
        self.element(locator).click()

    def _find_element(self, locator):
        return self.element(locator)

    def _get_element_text(self, locator):
        element = self._find_element(locator)
        return element.text

    def _get_element_attribute(self, locator, attribute):
        return self._find_element(locator).get_attribute(attribute)
