import pytest

from page_objects.RegisterPage import RegisterPage
from page_objects.elements.SuccessAlert import SuccessAlert


@pytest.mark.parametrize("element_number, name", [("2", "First Name"),
                                                  ("3", "Last Name"),
                                                  ("4", "E-Mail"),
                                                  ("5", "Telephone")])
def test_reg_personal_details_required_params(browser, element_number, name):
    """Check required parameters and their names in 'Your Personal Details' section"""
    assert RegisterPage(browser)._get_element_text(RegisterPage(browser).
                                                   get_personal_details_fields_xpath(element_number)) == name


@pytest.mark.parametrize("element_number, name", [("1", "Password"),
                                                 ("2", "Password Confirm")])
def test_reg_password_params(browser, element_number, name):
    """Check required parameters and their names in 'Your Password' section"""
    assert RegisterPage(browser)._get_element_text(RegisterPage(browser).get_password_fields_xpath(element_number)) \
           == name


def test_redirect_to_login_page(browser):
    """Check the redirect to login page"""
    RegisterPage(browser)._click_element(RegisterPage.LOGIN_PAGE_LINK)
    assert RegisterPage(browser)._get_element_attribute(RegisterPage.BREADCRUMB_LOGIN_TAB, "innerHTML") == "Login"


def test_subscribe_radio_button_default_value(browser):
    """Check that 'Subscribe' radio-button default meaning is 'No'"""
    radio_button_no = RegisterPage(browser)._find_element(RegisterPage.SUBSCRIBE_RADIO_BUTTON_NO)
    assert radio_button_no.is_selected()


def test_register_negative_do_not_agree_privacy_policy(browser):
    """Check that there is no opportunity to register untill user agrees privacy policy"""
    RegisterPage(browser)._input_value(RegisterPage.FIRSTNAME_FIELD, "Alice")
    RegisterPage(browser)._input_value(RegisterPage.LASTNAME_FIELD, "Wonderland")
    RegisterPage(browser)._input_value(RegisterPage.EMAIL_FIELD, "alice@wonderland.land")
    RegisterPage(browser)._input_value(RegisterPage.TELEPHONE_FIELD, "1234567")
    RegisterPage(browser)._input_value(RegisterPage.PASSWORD_FIELD, "12345")
    RegisterPage(browser)._input_value(RegisterPage.CONFIRM_PASSWORD_FIELD, "12345")
    RegisterPage(browser)._click_element(RegisterPage.CONTINUE_BUTTON)
    assert SuccessAlert(browser)._get_element_text(SuccessAlert.REGISTER_WARNING_ALERT) ==\
           "Warning: You must agree to the Privacy Policy!"
