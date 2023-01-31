from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):

    CATALOG_MENU_OPTION = (By.ID, "menu-catalog")
    PRODUCTS_OPTION = (By.XPATH, "//*[@id='collapse1']/li[2]/a")
    CATALOG_MENU_AREA = (By.XPATH, "//*[@id='collapse1']")
    ATTRIBUTES_MENU_OPTION = (By.XPATH, "//*[@id='collapse1']/li[5]/a")

    def get_menu_option_xpath(self, link):
        res = (By.XPATH, "//a[contains(@href,'route=catalog/" + link + "')]")
        return res
