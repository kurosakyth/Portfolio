from pages.common import login
from pages.actions import actions
import credentials.credentials as account
import pages.page_objects as page_object
import time

def test_login_SCRM_347(browser):
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with invalid credentials.
    login(webdriver, account.username_invalid, account.password_invalid, page_object.title_login)

    # Validate the error message.
    webdriver.validate_text(page_object.homepage_error, page_object.error_message_login)