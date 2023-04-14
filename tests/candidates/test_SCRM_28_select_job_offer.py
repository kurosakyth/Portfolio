import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_28_select_job_offer(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#CANDIDATE

    # Go to the Candidates page.
    common.all_option_selector(webdriver)

    # Search for a Candidate.
    webdriver.send_keys_to_element(page_object.search_candidate, 'Walden')

    # Click on the candidate searched.
    webdriver.click_button(page_object.result_searched_test_candidate)

    # Verify the candidate title of the page.
    webdriver.compare_title(page_object.title_walden_candidate_view)

#SELECT A JOB OFFER

    # Display the subpanel.
    webdriver.click_button(page_object.job_offer_view_candidate)

    # Click on the Select to open the new window.
    webdriver.click_button(page_object.select_job_offer_view_candidate)

    # Get a list of all the open windows
    window_handles = browser.window_handles

    # Switch to the latest window (the new window)
    window = window_handles[-1]
    browser.switch_to.window(window)

    # On the new window search for the role.
    webdriver.send_keys_to_element(page_object.search_input_select_accounts_view_candidate, '.NET Developer')

    # Click on the select button.
    webdriver.click_button(page_object.search_button_select_accounts_view_candidate)

    # Select the option to link on.
    webdriver.click_button(page_object.net_developer_option_table_select_accounts_view_candidate)

#CREATE A JOB OFFER
    # Switch back to the original window.
    window = window_handles[0]
    browser.switch_to.window(window)

    # Click on the create button.
    webdriver.click_button(page_object.create_job_offer_view_candidate)

    # Send the keys to the input.
    webdriver.send_keys_to_element(page_object.name_create_on_view_candidate, 'mobile tester')

    # Click on the save button to create the request on the subpanel.
    webdriver.click_button(page_object.save_button_job_offer_view_candidate)