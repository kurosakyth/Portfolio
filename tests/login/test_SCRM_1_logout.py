import pages.locators as page_object
from pages.functions import actions
from pages.common import login
import credentials.credentials as account

def test_SCRM_1_logout(browser):

    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

    # Mouse hover the profile icon.
    webdriver.hover_and_click_btn(page_object.profile_option)

    # Mouse hover and click all.
    webdriver.click_btn(page_object.logout_option)

    # Validate the Login title page.
    webdriver.title_compare(page_object.title_login)