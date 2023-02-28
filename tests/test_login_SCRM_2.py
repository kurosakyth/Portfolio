from pages.common import login
from pages.actions import actions

def test_login_SCRM_2(browser):
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page.
    login(webdriver)
