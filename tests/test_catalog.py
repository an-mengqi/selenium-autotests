import allure
import pytest
import time

from page_objects.AdminPage import AdminPage
from page_objects.CatalogPage import CatalogPage


def test_check_menu_catalog_exists(browser):
    """Check that there is menu option 'Catalog'"""
    AdminPage(browser).open(browser.admin_url)
    AdminPage(browser).login("user", "bitnami")
    with allure.step("Проверяю в боковом меню наличие раздела Catalog"):
        assert CatalogPage(browser).get_element_text(CatalogPage.CATALOG_MENU_OPTION) == "Catalog"


def test_expand_catalog(browser):
    """Check that menu option 'Catalog' expands"""
    AdminPage(browser).open(browser.admin_url)
    AdminPage(browser).login("user", "bitnami")
    with allure.step("Нажимаю в боковом меню на раздел Catalog"):
        CatalogPage(browser).click_element(CatalogPage.CATALOG_MENU_OPTION)
    with allure.step("Проверяю, что раздел Catalog раскрылся"):
        assert CatalogPage(browser).get_element_attribute(CatalogPage.CATALOG_MENU_AREA, "aria-expanded") == "true"


@pytest.mark.parametrize("link, text", [("category", "Categories"),
                                        ("product", "Products"),
                                        ("recurring", "Recurring Profiles"),
                                        ("filter", "Filters"),
                                        ("attribute", "Attributes"),
                                        ("attribute_group", "Attribute Groups"),
                                        ("option", "Options"),
                                        ("manufacturer", "Manufacturers"),
                                        ("download", "Downloads"),
                                        ("review", "Reviews"),
                                        ("information", "Information")])
def test_check_catalog_categories(browser, link, text):
    """Check Catalog categories"""
    AdminPage(browser).open(browser.admin_url)
    AdminPage(browser).login("user", "bitnami")
    with allure.step("Нажимаю в боковом меню на раздел Catalog"):
        CatalogPage(browser).click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.5)
    with allure.step("Раскрываю подраздел Attribute"):
        CatalogPage(browser).click_element(CatalogPage.ATTRIBUTES_MENU_OPTION)
    time.sleep(0.5)
    with allure.step(f'Проверяю наличие подраздела: {text}'):
        assert CatalogPage(browser).get_element_attribute(CatalogPage(browser).get_menu_option_xpath(link),
                                                          "innerHTML") == text
