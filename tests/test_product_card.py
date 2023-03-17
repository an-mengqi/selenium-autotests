import allure
import pytest
import time

from page_objects.AdminPage import AdminPage
from page_objects.CatalogPage import CatalogPage
from page_objects.ProductPage import ProductPage
from page_objects.elements.SuccessAlert import SuccessAlert


def test_open_product_card_page(browser):
    """Check that 'Product List' page opens"""
    with allure.step("Открываю страницу /admin"):
        AdminPage(browser).open(browser.admin_url)
    AdminPage(browser).login("user", "bitnami")
    with allure.step("Нажимаю в боковом меню на раздел Catalog"):
        CatalogPage(browser).click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    with allure.step("Перехожу на страницу Product List"):
        CatalogPage(browser).click_element(CatalogPage.PRODUCTS_OPTION)
    assert ProductPage(browser).get_element_text(ProductPage.PRODUCT_LIST_TABLE_TITLE) == "Product List"


@allure.step("Проверяю работу сортировки товаров в алфавитном и обратном порядке")
def test_change_product_cards_alphabet_order(browser):
    """Check that products order changes by clicking to 'Product Name'"""
    AdminPage(browser).open(browser.admin_url)
    AdminPage(browser).login("user", "bitnami")
    CatalogPage(browser).click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    CatalogPage(browser).click_element(CatalogPage.PRODUCTS_OPTION)
    assert ProductPage(browser).get_element_text(ProductPage.FIRST_PRODUCT_NAME_IN_TABLE) == 'Apple Cinema 30"'
    ProductPage(browser).click_element(ProductPage.PRODUCT_NAME_FILTER)
    assert ProductPage(browser).get_element_text(ProductPage.FIRST_PRODUCT_NAME_IN_TABLE) == "Sony VAIO"


@allure.step("Проверяю переход на страницу редактирвания товара")
def test_edit_product_card(browser):
    """Check redirect to 'Edit Product' page"""
    AdminPage(browser).open(browser.admin_url)
    AdminPage(browser).login("user", "bitnami")
    CatalogPage(browser).click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    CatalogPage(browser).click_element(CatalogPage.PRODUCTS_OPTION)
    ProductPage(browser).click_element(ProductPage.EDIT_BUTTON)
    assert ProductPage(browser).get_element_text(ProductPage.EDIT_PRODUCT_WINDOW_TITLE) == "Edit Product"


@pytest.mark.parametrize("field_id", ["input-name", "input-model"])
def test_negative_filter(browser, field_id):
    """Check filter work when no results were found"""
    AdminPage(browser).open(browser.admin_url)
    AdminPage(browser).login("user", "bitnami")
    CatalogPage(browser).click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    CatalogPage(browser).click_element(CatalogPage.PRODUCTS_OPTION)
    field = ProductPage(browser).get_filter_field_id(field_id)
    ProductPage(browser).find_element(field).send_keys("nonsense")
    ProductPage(browser).click_element(ProductPage.FILTER_BUTTON)
    assert ProductPage(browser).get_element_text(ProductPage.FILTER_RESULT_TEXT) == "No results!"


@allure.step("Проверяю добавление нового товара в таблицу")
def test_add_product_to_list(browser):
    """Add a product to a product list"""
    AdminPage(browser).open(browser.admin_url)
    AdminPage(browser).login("user", "bitnami")
    CatalogPage(browser).click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    CatalogPage(browser).click_element(CatalogPage.PRODUCTS_OPTION)
    CatalogPage(browser).click_element(CatalogPage.ADD_PRODUCT_TO_LIST_BUTTON)
    assert CatalogPage(browser).get_element_text(CatalogPage.ADD_PRODUCT_PAGE_TITLE) == "Add Product"
    CatalogPage(browser).click_element(CatalogPage.ADD_PRODUCT_TO_LIST_BUTTON)
    try:
        CatalogPage(browser).input_value(CatalogPage.PRODUCT_NAME_FIELD, "Superphone")
    except AssertionError:
        CatalogPage(browser).click_element(CatalogPage.ADD_PRODUCT_TO_LIST_BUTTON)
        CatalogPage(browser).input_value(CatalogPage.PRODUCT_NAME_FIELD, "Superphone")
    CatalogPage(browser).input_value(CatalogPage.META_TAG_TITLE_FIELD, "super")
    CatalogPage(browser).click_element(CatalogPage.DATA_TAB)
    CatalogPage(browser).input_value(CatalogPage.PRODUCT_MODEL_FIELD, "1.0")
    CatalogPage(browser).click_element(CatalogPage.SAVE_BUTTON)
    alert_text = SuccessAlert(browser).get_element_text(SuccessAlert.PRODUCT_MODIFIED_ALERT)
    assert "Success: You have modified products!" in alert_text
    result = ProductPage(browser).get_specific_product_in_table("Superphone")
    assert result is True


@allure.step("Проверяю удаление товара из таблицы")
def test_delete_product_from_list(browser):
    """Delete a product from a product list"""
    AdminPage(browser).open(browser.admin_url)
    AdminPage(browser).login("user", "bitnami")
    CatalogPage(browser).click_element(CatalogPage.CATALOG_MENU_OPTION)
    time.sleep(0.4)
    CatalogPage(browser).click_element(CatalogPage.PRODUCTS_OPTION)
    ProductPage(browser).click_check_box("Superphone")
    CatalogPage(browser).click_element(CatalogPage.DELETE_PRODUCT_FROM_LIST_BUTTON)
    alert = browser.switch_to.alert
    time.sleep(0.5)
    alert.accept()
    alert_text = SuccessAlert(browser).get_element_text(SuccessAlert.PRODUCT_MODIFIED_ALERT)
    assert "Success: You have modified products!" in alert_text
