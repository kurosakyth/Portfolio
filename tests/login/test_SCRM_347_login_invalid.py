from pages.common import login
from pages.functions import actions
import credentials.credentials as account
import pages.locators as page_object

def test_SCRM_347_login_invalid(browser):

    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#Test 1 password invalid.
    #LOGIN & HOMEPAGE

    # Log in to the page with invalid credentials.
    login(webdriver, account.username_invalid1, account.password_invalid1, page_object.title_login)

    # Validate the error message.
    webdriver.validate_text(page_object.homepage_error, page_object.error_message_login)

#Test 2 password invalid.
    #LOGIN & HOMEPAGE

    # Log in to the page with invalid credentials.
    login(webdriver, account.username_invalid2, account.password_invalid2, page_object.title_login)

    # Validate the error message.
    webdriver.validate_text(page_object.homepage_error, page_object.error_message_login)

#Test 3 password invalid.
    #LOGIN & HOMEPAGE

    # Log in to the page with invalid credentials.
    login(webdriver, account.username_invalid3, account.password_invalid3, page_object.title_login)

    # Validate the error message.
    webdriver.validate_text(page_object.homepage_error, page_object.error_message_login)

#Test 4 password invalid.
    #LOGIN & HOMEPAGE

    # Log in to the page with invalid credentials.
    login(webdriver, account.username_invalid4, account.password_invalid4, page_object.title_login)

    # Validate the error message.
    webdriver.validate_text(page_object.homepage_error, page_object.error_message_login)

#Test 5 password invalid.
    #LOGIN & HOMEPAGE

    # Log in to the page with invalid credentials.
    login(webdriver, account.username_invalid5, account.password_invalid5, page_object.title_login)

    # Validate the error message.
    webdriver.validate_text(page_object.homepage_error, page_object.error_message_login)

#Test 6 password invalid.
    #LOGIN & HOMEPAGE

    # Log in to the page with invalid credentials.
    login(webdriver, account.username_invalid6, account.password_invalid6, page_object.title_login)

    # Validate the error message.
    webdriver.validate_text(page_object.homepage_error, page_object.error_message_login)
