import pytest

from selenium.webdriver.common.by import By


def test_check_menu_catalog_exists(browser):
    """Check that there is menu option 'Catalog'"""
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button/i").click()
    menu_catalog = browser.find_element(By.ID, "menu-catalog")
    assert menu_catalog.text == "Catalog"

def test_expand_catalog(browser):
    """Check that menu option 'Catalog' expands"""
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button/i").click()
    browser.find_element(By.ID, "menu-catalog").click()
    assert browser.find_element(By.XPATH, "//*[@id='collapse1']").get_attribute("aria-expanded") == "true"

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
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button/i").click()
    browser.find_element(By.ID, "menu-catalog").click()
    if text != "Attributes" or "Attribute Groups":
        menu_option = browser.find_element(By.XPATH, "//a[contains(@href,'route=catalog/" + link + "')]")
        assert menu_option.get_attribute("innerHTML") == text
    else:
        attributes = browser.find_element(By.XPATH, "//*[@id='collapse1']/li[5]/a").click()
        assert attributes.text == "Attributes"
        attributes_suboptions = browser.find_element(By.XPATH, "//a[contains(@href,'route=catalog/" + link + "')]")
        assert attributes_suboptions.get_attribute("innerHTML") == text
