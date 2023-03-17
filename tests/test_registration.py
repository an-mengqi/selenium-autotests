import allure
import pytest

from page_objects.RegisterPage import RegisterPage
from page_objects.elements.SuccessAlert import SuccessAlert


@pytest.mark.parametrize("element_number, name", [("2", "First Name"),
                                                  ("3", "Last Name"),
                                                  ("4", "E-Mail"),
                                                  ("5", "Telephone")])
def test_reg_personal_details_required_params(browser, element_number, name):
    """Check required parameters and their names in 'Your Personal Details' section"""
    with allure.step("Открываю страницу регистрации"):
        RegisterPage(browser).open(browser.registration_url)
    with allure.step(f'Проверяю в разделе "Your Personal Details" обязательное поле ввода: {name}'):
        assert RegisterPage(browser).get_element_text(RegisterPage(browser).
                                                      get_personal_details_fields_xpath(element_number)) == name


@pytest.mark.parametrize("element_number, name", [("1", "Password"),
                                                  ("2", "Password Confirm")])
def test_reg_password_params(browser, element_number, name):
    """Check required parameters and their names in 'Your Password' section"""
    with allure.step("Открываю страницу регистрации"):
        RegisterPage(browser).open(browser.registration_url)
    with allure.step(f'Проверяю в разделе "Your Personal Details" обязательное поле ввода: {name}'):
        assert RegisterPage(browser).get_element_text(RegisterPage(browser).get_password_fields_xpath(element_number)) \
               == name


@allure.step("Проверяю редирект на страницу авторизации")
def test_redirect_to_login_page(browser):
    """Check the redirect to login page"""
    RegisterPage(browser).open(browser.registration_url)
    RegisterPage(browser).click_element(RegisterPage.LOGIN_PAGE_LINK)
    assert RegisterPage(browser).get_element_attribute(RegisterPage.BREADCRUMB_LOGIN_TAB, "innerHTML") == "Login"


@allure.step("Проверяю дефолтное значение radio-button 'Subscribe'")
def test_subscribe_radio_button_default_value(browser):
    """Check that 'Subscribe' radio-button default meaning is 'No'"""
    RegisterPage(browser).open(browser.registration_url)
    radio_button_no = RegisterPage(browser).find_element(RegisterPage.SUBSCRIBE_RADIO_BUTTON_NO)
    assert radio_button_no.is_selected()


@allure.step("Проверяю невозможность зарегистрироваться без согласия с Политикой конфиденциальности")
def test_register_negative_do_not_agree_privacy_policy(browser):
    """Check that there is no opportunity to register untill user agrees privacy policy"""
    RegisterPage(browser).open(browser.registration_url)
    RegisterPage(browser).input_value(RegisterPage.FIRSTNAME_FIELD, "Alice")
    RegisterPage(browser).input_value(RegisterPage.LASTNAME_FIELD, "Wonderland")
    RegisterPage(browser).input_value(RegisterPage.EMAIL_FIELD, "alice@wonderland.land")
    RegisterPage(browser).input_value(RegisterPage.TELEPHONE_FIELD, "1234567")
    RegisterPage(browser).input_value(RegisterPage.PASSWORD_FIELD, "12345")
    RegisterPage(browser).input_value(RegisterPage.CONFIRM_PASSWORD_FIELD, "12345")
    RegisterPage(browser).click_element(RegisterPage.CONTINUE_BUTTON)
    assert SuccessAlert(browser).get_element_text(SuccessAlert.REGISTER_WARNING_ALERT) ==\
           "Warning: You must agree to the Privacy Policy!"


@allure.step("Проверяю регистрацию нового пользователя")
def test_register_user(browser):
    """Check registration"""
    RegisterPage(browser).open(browser.registration_url)
    RegisterPage(browser).input_value(RegisterPage.FIRSTNAME_FIELD, "Alice")
    RegisterPage(browser).input_value(RegisterPage.LASTNAME_FIELD, "Wonderland")
    RegisterPage(browser).input_value(RegisterPage.EMAIL_FIELD, "alice@wonderland.land")
    RegisterPage(browser).input_value(RegisterPage.TELEPHONE_FIELD, "1234567")
    RegisterPage(browser).input_value(RegisterPage.PASSWORD_FIELD, "12345")
    RegisterPage(browser).input_value(RegisterPage.CONFIRM_PASSWORD_FIELD, "12345")
    RegisterPage(browser).click_element(RegisterPage.PRIVACY_POLICY_CHECKBOX)
    RegisterPage(browser).click_element(RegisterPage.CONTINUE_BUTTON)
    assert RegisterPage(browser).get_element_attribute(RegisterPage.REGISTER_SUCCESS_PAGE_TITLE, "innerHTML") ==\
           "Your Account Has Been Created!"
