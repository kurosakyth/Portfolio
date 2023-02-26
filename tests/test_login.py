from pages.common import login
from pages.actions import actions

def test_login(browser):
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page.
    login(webdriver)
