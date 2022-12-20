import pytest
import time

from selenium.webdriver.common.by import By


def test_open_product_card_page(browser):
    """Check that 'Product List' page opens"""
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button/i").click()
    browser.find_element(By.ID, "menu-catalog").click()
    time.sleep(0.4)
    browser.find_element(By.XPATH, "//*[@id='collapse1']/li[2]/a").click()
    assert browser.find_element(By.XPATH, "//*[@id='content']/div[2]/div/div[2]/div/div[1]/h3").text == "Product List"

def test_change_product_cards_alphabet_order(browser):
    """Check that products order changes by clicking to 'Product Name'"""
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button/i").click()
    browser.find_element(By.ID, "menu-catalog").click()
    time.sleep(0.4)
    browser.find_element(By.XPATH, "//*[@id='collapse1']/li[2]/a").click()
    first_product = browser.find_element(By.XPATH, "//*[@id='form-product']/div/table/tbody/tr[1]/td[3]")
    assert first_product.text == 'Apple Cinema 30"'
    browser.find_element(By.XPATH, "//*[@id='form-product']/div/table/thead/tr/td[3]/a").click()
    first_product = browser.find_element(By.XPATH, "//*[@id='form-product']/div/table/tbody/tr[1]/td[3]")
    assert first_product.text == "Sony VAIO"

def test_edit_product_card(browser):
    """Check redirect to 'Edit Product' page"""
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button/i").click()
    browser.find_element(By.ID, "menu-catalog").click()
    time.sleep(0.4)
    browser.find_element(By.XPATH, "//*[@id='collapse1']/li[2]/a").click()
    browser.find_element(By.XPATH, "//*[@id='form-product']/div/table/tbody/tr[1]/td[8]/a").click()
    edit_product_title = browser.find_element(By.XPATH, "//*[@id='content']/div[2]/div/div[1]/h3")
    assert edit_product_title.text == "Edit Product"

@pytest.mark.parametrize("field_id", ["input-name", "input-model"])
def test_negative_filter(browser, field_id):
    """Check filter work when no results were found"""
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button/i").click()
    browser.find_element(By.ID, "menu-catalog").click()
    time.sleep(0.4)
    browser.find_element(By.XPATH, "//*[@id='collapse1']/li[2]/a").click()
    browser.find_element(By.ID, f"{field_id}").send_keys("nonsense")
    browser.find_element(By.ID, "button-filter").click()
    result_text = browser.find_element(By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td")
    assert result_text.text == "No results!"
