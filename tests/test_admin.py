from page_objects.AdminPage import AdminPage


def test_login_window(browser):
    """Check that there is a login window on the page"""
    assert AdminPage(browser).find_element(AdminPage.AUTH_WINDOW)


def test_username_field_placeholder(browser):
    """Check that login field placeholder is 'Username'"""
    assert AdminPage(browser).get_element_attribute(AdminPage.USERNAME_INPUT_FIELD, "placeholder") == "Username"


def test_password_field_placeholder(browser):
    """Check that password field placeholder is 'Password'"""
    assert AdminPage(browser).get_element_attribute(AdminPage.PASSWORD_INPUT_FIELD, "placeholder") == "Password"


def test_forgot_password_window(browser):
    """Check the work of the 'Forgot Password' button"""
    AdminPage(browser).click_element(AdminPage.FORGOTTEN_PASSWORD_LINK)
    assert AdminPage(browser).get_element_text(AdminPage.FORGOT_PASSWORD_WINDOW_TITLE) == "Forgot Your Password?"


def test_login(browser):
    """Check that the user can log in and redirect to Dashboard"""
    AdminPage(browser).login("user", "bitnami")
    assert AdminPage(browser).get_element_attribute(AdminPage.DASHBOARD_PAGE_TITLE, "innerHTML") == "Dashboard"
