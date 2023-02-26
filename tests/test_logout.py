import pages.page_objects as page_object
from pages.actions import actions
from pages.common import login
import time

def test_logout(browser):

    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page.
    login(webdriver)

    # Mouse hover the profile icon.
    webdriver.hover_and_click_btn(page_object.profile_option)

    # Mouse hover and click all.
    webdriver.click_btn(page_object.logout_option)

    # Validate the Login title page.
    webdriver.title_compare(page_object.tittle_login)

    #time.sleep(5)