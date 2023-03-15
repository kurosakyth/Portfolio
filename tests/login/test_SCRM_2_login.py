from pages.common import login
from pages.functions import actions
import credentials.credentials as account
import pages.locators as page_object

def test_SCRM_2_login(browser):
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)