import time

from selenium.webdriver.common.by import By


def test_search(browser):
    browser.find_element(By.XPATH,
                         "//div[@class='container']/div[@class='row']/div[@class='col-sm-5']/div[@id='search']/\n"
                         "span[@class='input-group-btn']/button[@class='btn btn-default btn-lg']").click()
    text_search = browser.find_element(By.XPATH, "//div[@id='product-search']/div[@class='row']/div[@id='content']/h1")
    assert text_search.get_attribute("innerHTML") == "Search"

def test_cart_empty(browser):
    browser.find_element(By.XPATH,
                         "//div[@class='container']/div[@class='row']/div[@class='col-sm-3']/div[@id='cart']/\n"
                         "button[@type='button']").click()
    dropdown_menu = browser.find_element(By.XPATH,
                         "//div[@class='container']/div[@class='row']/div[@class='col-sm-3']/div[@id='cart']/\n"
                         "ul[@class='dropdown-menu pull-right']/li/p[@class='text-center']")
    assert dropdown_menu.get_attribute("innerHTML") == "Your shopping cart is empty!"

def test_add_to_wishlist(browser):
    browser.find_element(By.XPATH,
                         "//div[@id='common-home']/div[@class='row']/div[@id='content']/div[@class='row']/\n"
                         "div[@class='product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12']/\n"
                         "div[@class='product-thumb transition']/div[@class='button-group']/\n"
                         "button[@type='button']").click()
    time.sleep(0.3)
    assert browser.find_element(By.XPATH,
                                "//div[@id='common-home']/div[@class='alert alert-success alert-dismissible']")
