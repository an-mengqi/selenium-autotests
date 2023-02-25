import allure
import pytest
import time

from page_objects.elements.SuccessAlert import SuccessAlert
from page_objects.MainPage import MainPage


def test_search(browser):
    """Check that a title 'Search' appears after clicking to the search button"""
    with allure.step("Нажимаю на кнопку поиска"):
        MainPage(browser).click_element(MainPage.SEARCH_BUTTON)
    with allure.step("Проверяю название подзаголовка - Search"):
        assert MainPage(browser).get_element_attribute(MainPage.SEARCH_TITLE, "innerHTML") == "Search"


@allure.step("Проверяю, что корзина пуста")
def test_cart_empty(browser):
    """Check that the shopping cart is empty"""
    MainPage(browser).click_element(MainPage.CART_BUTTON)
    assert MainPage(browser).get_element_attribute(MainPage.EMTY_CART_DROPDOWN_ITEM, "innerHTML") ==\
           "Your shopping cart is empty!"


@allure.step("Проверяю алерт после добавления товара в wishlist")
def test_add_to_wishlist(browser):
    """Check that the alert appears after adding an item to wishist"""
    MainPage(browser).click_element(MainPage.ADD_TO_WISHLIST_BUTTON)
    time.sleep(0.3)
    assert MainPage(browser).find_element(SuccessAlert.SUCCESS_ALERT)


def test_my_account_dropdown_menu(browser):
    """Check that dropdown menu with buttons 'Register' and 'Login' appears"""
    with allure.step("На главной странице нажимаю на Account"):
        MainPage(browser).click_element(MainPage.ACCOUNT_DROPDOWN_MENU)
    with allure.step("Проверяю, что в раскрывшемся списке есть кнопка Register"):
        assert MainPage(browser).find_element(MainPage.REGISTER_DROPDOWN_ITEM)
    with allure.step("Проверяю, что в раскрывшемся списке есть кнопка Login"):
        assert MainPage(browser).find_element(MainPage.LOGIN_DROPDOWN_ITEM)


@allure.step("Проверяю редирект на страницу регистрации аккаунта")
def test_move_to_register_account_page(browser):
    """Move to a registration page"""
    MainPage(browser).click_element(MainPage.ACCOUNT_DROPDOWN_MENU)
    MainPage(browser).click_element(MainPage.REGISTER_DROPDOWN_ITEM)
    assert MainPage(browser).get_element_attribute(MainPage.REGISTER_ACCOUNT_TITLE, "innerHTML") == "Register Account"


@pytest.mark.parametrize("dropdown_item, currency_value", [(MainPage.CURRENCY_DROPDOWN_ITEM_EURO, "€"),
                                                           (MainPage.CURRENCY_DROPDOWN_ITEM_POUND, "£"),
                                                           (MainPage.CURRENCY_DROPDOWN_ITEM_DOLLAR, "$")])
def test_check_currency(browser, dropdown_item, currency_value):
    """Check currency change"""
    with allure.step("Нажимаю на выпадающий список валют"):
        MainPage(browser).click_element(MainPage.CURRENCY_DROPDOWN_MENU_BUTTON)
    with allure.step(f'Выбираю валюту: {currency_value}'):
        MainPage(browser).click_element(dropdown_item)
    assert MainPage(browser).get_element_text(MainPage.CHOSEN_CURRENCY) == currency_value
