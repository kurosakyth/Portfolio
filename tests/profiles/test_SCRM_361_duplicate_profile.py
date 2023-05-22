import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_361_duplicate_profile(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#PROFILE

    # Open the browser with the page.
    webdriver.open_page(page_object.url_profile)
   
    # Validate the Login title page.
    webdriver.compare_title(page_object.title_profile)

    # Click on the first profile on the list.
    webdriver.click_button(page_object.option_on_the_table_profile)

#PROFILE OPTION

    # Verify the prfoile title of the page.
    webdriver.compare_title(page_object.title_contains_view_profile)
    
    # Click on duplicate button on the candidate view.
    webdriver.click_button(page_object.duplicate_button_view_profile)

    # Verify the create candidate title of the page.
    webdriver.compare_title(page_object.title_create_profile)

    # Click on save button on the create candidate view.
    webdriver.click_button(page_object.save_btn_create_profile)

    # Verify the candidate title of the page.
    webdriver.compare_title(page_object.title_contains_view_profile)