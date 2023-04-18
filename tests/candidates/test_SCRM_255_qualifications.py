import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time
def test_SCRM_255_qualifications(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#CANDIDATE

    # Open the browser with the page.
    webdriver.open_page(page_object.url_candidate)

    # Validate the Login title page.
    webdriver.compare_title(page_object.title_candidates)

    # Search for a Candidate.
    webdriver.send_keys_to_element(page_object.search_candidate, 'Walden')

    # Click on the candidate searched.
    webdriver.click_button(page_object.result_searched_test_candidate)

    # Verify the candidate title of the page.
    webdriver.compare_title(page_object.title_walden_candidate_view)

#SELECT A PERSONALITY TEST

    # Display the subpanel.
    webdriver.click_button(page_object.qualifications_view_candidate)

    # Click on the Select to open the new window.
    webdriver.click_button(page_object.select_qualifications_view_candidate)

    # Get a list of all the open windows
    window_handles = browser.window_handles

    # Switch to the latest window (the new window)
    window = window_handles[-1]
    browser.switch_to.window(window)

    # Click on the checkbox.
    webdriver.click_button(page_object.option_select_qualifications_view_candidate)

    # Click on the select button.

#CREATE A PERSONALITY TEST
    # Switch back to the original window.
    window = window_handles[0]
    browser.switch_to.window(window)

    # Click on the create button.
    webdriver.click_button(page_object.create_qualifications_view_candidate)
    
    # Send keys to the name input.
    webdriver.send_keys_to_element(page_object.name_create_on_view_candidate, 'Scrum Foundations')

    # Click on the save button to create the request on the subpanel.
    webdriver.click_button(page_object.save_button_qualifications_view_candidate)