import pytest

from selenium.webdriver.common.by import By

@pytest.mark.parametrize("element_number, name", [("2", "First Name"),
                                                  ("3", "Last Name"),
                                                  ("4", "E-Mail"),
                                                  ("5", "Telephone")])
def test_reg_personal_details_required_params(browser, element_number, name):
    """Check required parameters and their names in 'Your Personal Details' section"""
    element = browser.find_element(By.XPATH, "//*[@id='account']/div[" + element_number + "]/label")
    assert element.text == name

@pytest.mark.parametrize("element_number, name", [("1", "Password"),
                                                 ("2", "Password Confirm")])
def test_reg_password_params(browser, element_number, name):
    """Check required parameters and their names in 'Your Password' section"""
    element = browser.find_element(By.XPATH, "//*[@id='content']/form/fieldset[2]/div[" +  element_number + "]/label")
    assert element.text == name

def test_redirect_to_login_page(browser):
    """Check the redirect to login page"""
    browser.find_element(By.XPATH, "//*[@id='content']/p/a").click()
    breadcrumb_login = browser.find_element(By.XPATH, "//*[@id='account-login']/ul/li[3]/a")
    assert breadcrumb_login.get_attribute("innerHTML") == "Login"

def test_subscribe_radio_button_default_value(browser):
    """Check that 'Subscribe' radio-button default meaning is 'No'"""
    radio_button_no = browser.find_element(By.XPATH, "//*[@id='content']/form/fieldset[3]/div/div/label[2]/input")
    assert radio_button_no.is_selected()

def test_register_negative_do_not_agree_privacy_policy(browser):
    """Check that there is no opportunity to register untill user agrees privacy policy"""
    browser.find_element(By.NAME, "firstname").send_keys("Alice")
    browser.find_element(By.NAME, "lastname").send_keys("Wonderland")
    browser.find_element(By.NAME, "email").send_keys("alice@wonderland.land")
    browser.find_element(By.NAME, "telephone").send_keys("1234567")
    browser.find_element(By.NAME, "password").send_keys("12345")
    browser.find_element(By.NAME, "confirm").send_keys("12345")
    browser.find_element(By.XPATH, "//*[@id='content']/form/div/div/input[2]").click()
    account_created_text = browser.find_element(By.XPATH, "//*[@id='account-register']/div[1]")
    assert account_created_text.text == "Warning: You must agree to the Privacy Policy!"
