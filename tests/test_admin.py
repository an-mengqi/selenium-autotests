from selenium.webdriver.common.by import By

def test_login_window(browser):
    """Check that there is a login window on the page"""
    assert browser.find_element(By.XPATH, "//div[@class='panel panel-default']")

def test_username_field_placeholder(browser):
    """Check that login field placeholder is 'Username'"""
    username_field = browser.find_element(By.NAME, "username")
    assert username_field.get_attribute("placeholder") == "Username"

def test_password_field_placeholder(browser):
    """Check that password field placeholder is 'Password'"""
    password_field = browser.find_element(By.NAME, "password")
    assert password_field.get_attribute("placeholder") == "Password"

def test_forgot_password_window(browser):
    """Check the work of the 'Forgot Password' button"""
    browser.find_element(By.XPATH, "//a[contains(@href,'route=common/forgotten')]").click()
    forgot_password_window = browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[1]/h1")
    assert forgot_password_window.text == "Forgot Your Password?"

def test_login(browser):
    """Check that the user can log in and redirect to Dashboard"""
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button/i").click()
    title = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div/h1")
    assert title.get_attribute("innerHTML") == "Dashboard"
