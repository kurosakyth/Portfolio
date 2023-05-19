import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_278_recruitment_profile(browser):
    
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

#RECRUITMENT SUBPANEL

    #CREATE RECRUITMENT.

    # Display the recruitment request subpanel.
    webdriver.click_button(page_object.recruitment_request_sub_view_profile)
    
    # Click on the create recruitment request button.
    webdriver.click_button(page_object.create_recruit_req_view_profile)
    time.sleep(5)
    # Fill the name input of the create recruitment request.
    webdriver.send_keys_to_element(page_object.name_create_recruit_req_view_profile, "Automation_profile")

    # Click on the Save button.
    webdriver.click_button(page_object.save_btn_create_recruit_req_view_profile)

    #SELECT RECRUITMENT.
    
    # Click on the select recruitment request button.
    webdriver.click_button(page_object.select_recruit_req_view_profile)
    time.sleep(5)
    # Get a list of all the open windows
    window_handles = browser.window_handles

    # Switch to the latest window (the new window)
    window = window_handles[-1]
    browser.switch_to.window(window)

    # Click option of the select window.
    webdriver.click_button(page_object.option_select_recruit_req_view_profile)

#     # Other window.

# #In progress.


# #CREATE A JOB OFFER
#     # Switch back to the original window.
#     window = window_handles[0]
#     browser.switch_to.window(window)

#     # Click on the create button.
#     webdriver.click_button(page_object.create_job_offer_view_candidate)

#     # Send the keys to the input.
#     webdriver.send_keys_to_element(page_object.name_create_on_view_candidate, 'mobile tester')

#     # Click on the save button to create the request on the subpanel.
#     webdriver.click_button(page_object.save_button_job_offer_view_candidate)