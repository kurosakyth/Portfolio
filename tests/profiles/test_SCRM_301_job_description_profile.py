import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_301_job_description_profile(browser):
    
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

#JOB DESCRIPTION SUBPANEL

    #CREATE JOB DESCRIPTION.

    # Display the job description subpanel.
    webdriver.click_button(page_object.job_description_sub_profile)
    
    # Click on the create job description button.
    webdriver.click_button(page_object.create_job_description_view_profile)

    # Fill the name input of the create job description.
    webdriver.send_keys_to_element(page_object.name_create_job_description_view_profile, "Automation_profile")

    # Click on the Save button.
    webdriver.click_button(page_object.save_btn_create_job_description_view_profile)

    #SELECT JOB DESCRIPTION.
    
    # Click on the select job description button.
    webdriver.click_button(page_object.select_job_description_view_profile)

    # Get a list of all the open windows
    window_handles = browser.window_handles

    # Switch to the latest window (the new window)
    window = window_handles[-1]
    browser.switch_to.window(window)

    # Click option of the select window.
    webdriver.click_button(page_object.option_select_job_description_view_profile)