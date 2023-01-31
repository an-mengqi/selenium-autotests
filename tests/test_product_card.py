import pytest
import time

from page_objects.AdminPage import AdminPage
from page_objects.CatalogPage import CatalogPage
from page_objects.ProductPage import ProductPage


def test_open_product_card_page(browser):
    """Check that 'Product List' page opens"""
    AdminPage(browser).login("user", "bitnami")
    CatalogPage(browser)._click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    CatalogPage(browser)._click_element(CatalogPage.PRODUCTS_OPTION)
    assert ProductPage(browser)._get_element_text(ProductPage.PRODUCT_LIST_TABLE_TITLE) == "Product List"


def test_change_product_cards_alphabet_order(browser):
    """Check that products order changes by clicking to 'Product Name'"""
    AdminPage(browser).login("user", "bitnami")
    CatalogPage(browser)._click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    CatalogPage(browser)._click_element(CatalogPage.PRODUCTS_OPTION)
    assert ProductPage(browser)._get_element_text(ProductPage.FIRST_PRODUCT_NAME_IN_TABLE) == 'Apple Cinema 30"'
    ProductPage(browser)._click_element(ProductPage.PRODUCT_NAME_FILTER)
    assert ProductPage(browser)._get_element_text(ProductPage.FIRST_PRODUCT_NAME_IN_TABLE) == "Sony VAIO"


def test_edit_product_card(browser):
    """Check redirect to 'Edit Product' page"""
    AdminPage(browser).login("user", "bitnami")
    CatalogPage(browser)._click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    CatalogPage(browser)._click_element(CatalogPage.PRODUCTS_OPTION)
    ProductPage(browser)._click_element(ProductPage.EDIT_BUTTON)
    assert ProductPage(browser)._get_element_text(ProductPage.EDIT_PRODUCT_WINDOW_TITLE) == "Edit Product"


@pytest.mark.parametrize("field_id", ["input-name", "input-model"])
def test_negative_filter(browser, field_id):
    """Check filter work when no results were found"""
    AdminPage(browser).login("user", "bitnami")
    CatalogPage(browser)._click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    CatalogPage(browser)._click_element(CatalogPage.PRODUCTS_OPTION)
    field = ProductPage(browser).get_filter_field_id(field_id)
    ProductPage(browser)._find_element(field).send_keys("nonsense")
    ProductPage(browser)._click_element(ProductPage.FILTER_BUTTON)
    assert ProductPage(browser)._get_element_text(ProductPage.FILTER_RESULT_TEXT) == "No results!"
