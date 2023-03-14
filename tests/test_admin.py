import allure
import configuration as conf

from page_objects.AdminPage import AdminPage


@allure.step("Ищу окно с формой авторизации")
def test_login_window(browser):
    """Check that there is a login window on the page"""
    AdminPage(browser).open(conf.admin_url)
    assert AdminPage(browser).find_element(AdminPage.AUTH_WINDOW)


@allure.step("Проверяю значение плейсхолдера для поля логина")
def test_username_field_placeholder(browser):
    """Check that login field placeholder is 'Username'"""
    AdminPage(browser).open(conf.admin_url)
    assert AdminPage(browser).get_element_attribute(AdminPage.USERNAME_INPUT_FIELD, "placeholder") == "Username"


@allure.step("Проверяю значение плейсхолдера для поля пароля")
def test_password_field_placeholder(browser):
    """Check that password field placeholder is 'Password'"""
    AdminPage(browser).open(conf.admin_url)
    assert AdminPage(browser).get_element_attribute(AdminPage.PASSWORD_INPUT_FIELD, "placeholder") == "Password"


@allure.step("Проверяю значение плейсхолдера для поля 'Forgot Password'")
def test_forgot_password_window(browser):
    """Check the work of the 'Forgot Password' button"""
    AdminPage(browser).open(conf.admin_url)
    AdminPage(browser).click_element(AdminPage.FORGOTTEN_PASSWORD_LINK)
    assert AdminPage(browser).get_element_text(AdminPage.FORGOT_PASSWORD_WINDOW_TITLE) == "Forgot Your Password?"


@allure.step("Вхожу в учетку")
def test_login(browser):
    """Check that the user can log in and redirect to Dashboard"""
    AdminPage(browser).open(conf.admin_url)
    AdminPage(browser).login("user", "bitnami")
    with allure.step("Проверяю редирект на страницу Dashboard"):
        assert AdminPage(browser).get_element_attribute(AdminPage.DASHBOARD_PAGE_TITLE, "innerHTML") == "Dashboard"
