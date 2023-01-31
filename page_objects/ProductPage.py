from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    PRODUCT_LIST_TABLE_TITLE = (By.XPATH, "//*[@id='content']/div[2]/div/div[2]/div/div[1]/h3")
    FIRST_PRODUCT_NAME_IN_TABLE = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr[1]/td[3]")
    PRODUCT_NAME_FILTER = (By.XPATH, "//*[@id='form-product']/div/table/thead/tr/td[3]/a")
    EDIT_BUTTON = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr[1]/td[8]/a")
    EDIT_PRODUCT_WINDOW_TITLE = (By.XPATH, "//*[@id='content']/div[2]/div/div[1]/h3")
    FILTER_BUTTON = (By.ID, "button-filter")
    FILTER_RESULT_TEXT = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td")

    def get_filter_field_id(self, test_parameter):
        res = (By.ID, test_parameter)
        return res
