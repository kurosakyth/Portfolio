import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_252_create_profile(browser):
    
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


    # Verify the candidate title of the page.
    webdriver.compare_title(page_object.title_contains_view_profile)

    # Display the Skills & Qualifications subpanel.
    webdriver.click_button(page_object.skills_quallifications_sub_view_profile)

    # Select a Skill.
    webdriver.click_button(page_object.select_a_sk_view_profile)
    
    # Select an option of the Skill dropdown.
    webdriver.click_button(page_object.options_list_sk_view_profile)