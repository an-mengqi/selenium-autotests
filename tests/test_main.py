import time
import pytest

from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_search(browser):
    """Check that a title 'Search' appears after clicking to the search button"""
    browser.find_element(By.XPATH,
                         "//div[@class='container']/div[@class='row']/div[@class='col-sm-5']/div[@id='search']/\n"
                         "span[@class='input-group-btn']/button[@class='btn btn-default btn-lg']").click()
    text_search = browser.find_element(By.XPATH, "//div[@id='product-search']/div[@class='row']/div[@id='content']/h1")
    assert text_search.get_attribute("innerHTML") == "Search"

@pytest.mark.skip
def test_cart_empty(browser):
    """Check that the shopping cart is empty"""
    browser.find_element(By.XPATH,
                         "//div[@class='container']/div[@class='row']/div[@class='col-sm-3']/div[@id='cart']/\n"
                         "button[@type='button']").click()
    dropdown_menu = browser.find_element(By.XPATH,
                         "//div[@class='container']/div[@class='row']/div[@class='col-sm-3']/div[@id='cart']/\n"
                         "ul[@class='dropdown-menu pull-right']/li/p[@class='text-center']")
    assert dropdown_menu.get_attribute("innerHTML") == "Your shopping cart is empty!"

@pytest.mark.skip
def test_add_to_wishlist(browser):
    """Check that the alert appears after adding an item to wishist"""
    browser.find_element(By.XPATH,
                         "//div[@id='common-home']/div[@class='row']/div[@id='content']/div[@class='row']/\n"
                         "div[@class='product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12']/\n"
                         "div[@class='product-thumb transition']/div[@class='button-group']/\n"
                         "button[@type='button']").click()
    time.sleep(0.3)
    assert browser.find_element(By.XPATH,
                                "//div[@id='common-home']/div[@class='alert alert-success alert-dismissible']")

def test_my_account_dropdown_menu(browser):
    """Check that dropdown menu with buttons 'Register' and 'Login' appears"""
    browser.find_element(By.XPATH, "//a[contains(@href,'route=account/account')]").click()
    assert browser.find_element(By.LINK_TEXT, "Register")
    assert browser.find_element(By.LINK_TEXT, "Login")

def test_move_to_register_account_page(browser):
    """Move to a registration page"""
    browser.find_element(By.XPATH, "//a[contains(@href,'route=account/account')]").click()
    browser.find_element(By.LINK_TEXT, "Register").click()
    text_register_account = browser.find_element(By.XPATH, "//div[@id='account-register']/div[@class='row']/div[@id='content']/h1")
    assert text_register_account.get_attribute("innerHTML") == "Register Account"
