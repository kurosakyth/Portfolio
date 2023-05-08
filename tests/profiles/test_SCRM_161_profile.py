import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_161_profiles(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#PROFILES

    # Go to the Candidates page.
    common.all_option_profile(webdriver)

    # 