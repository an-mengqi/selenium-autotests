import time

from selenium.webdriver.common.by import By


def test_search(browser):
    """Check that a title 'Search' appears after clicking to the search button"""
    browser.find_element(By.XPATH, "//*[@id='search']/span/button").click()
    text_search = browser.find_element(By.XPATH, "//*[@id='content']/h1")
    assert text_search.get_attribute("innerHTML") == "Search"

def test_cart_empty(browser):
    """Check that the shopping cart is empty"""
    browser.find_element(By.ID, "cart").click()
    dropdown_menu = browser.find_element(By.XPATH, "//*[@id='cart']/ul/li/p")
    assert dropdown_menu.get_attribute("innerHTML") == "Your shopping cart is empty!"

def test_add_to_wishlist(browser):
    """Check that the alert appears after adding an item to wishist"""
    browser.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[3]/button[2]").click()
    time.sleep(0.3)
    assert browser.find_element(By.XPATH, "//*[@id='common-home']/div[1]")

def test_my_account_dropdown_menu(browser):
    """Check that dropdown menu with buttons 'Register' and 'Login' appears"""
    browser.find_element(By.XPATH, "//a[contains(@href,'route=account/account')]").click()
    assert browser.find_element(By.LINK_TEXT, "Register")
    assert browser.find_element(By.LINK_TEXT, "Login")

def test_move_to_register_account_page(browser):
    """Move to a registration page"""
    browser.find_element(By.XPATH, "//a[contains(@href,'route=account/account')]").click()
    browser.find_element(By.LINK_TEXT, "Register").click()
    text_register_account = browser.find_element(By.XPATH, "//*[@id='content']/h1")
    assert text_register_account.get_attribute("innerHTML") == "Register Account"
