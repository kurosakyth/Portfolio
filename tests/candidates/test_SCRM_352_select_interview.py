import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_352_select_interview(browser):
    
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

#SELECT A INTERVIEW

    # Display the subpanel.
    webdriver.click_button(page_object.interviews_view_candidate)

    # Click on the Select to open the new window.
    webdriver.click_button(page_object.select_candidate_interviews_view_candidate)

    # Get a list of all the open windows
    window_handles = browser.window_handles

    # Switch to the latest window (the new window)
    window = window_handles[-1]
    browser.switch_to.window(window)

    # Search on the input.
    webdriver.send_keys_to_element(page_object.search_input_select_accounts_view_candidate, 'Erick Interview')

    webdriver.click_button(page_object.search_button_select_view_candidate)

    # Select the option to link on.
    webdriver.click_button(page_object.interv_option_candidate_interviews_candidate)

#CREATE A INTERVIEW
    # Switch back to the original window.
    window = window_handles[0]
    browser.switch_to.window(window)

    # Click on the create button.
    webdriver.click_button(page_object.create_candidate_interviews_view_candidate)

    # Select approved dropdown.
    webdriver.click_button(page_object.approved_interviews_create_on_view_candidate)

    # Select approved option on the dropdown.
    webdriver.click_button(page_object.approved_option_interviews_create_on_view_candidate)

    # Click to display the interview date.
    webdriver.click_button(page_object.date_button_interivews_create_on_view_candidate)

    # Select the interview date option.
    webdriver.click_button(page_object.date_option_interviews_create_on_view_candidate)

    # Parameterize the validation messages.
    fields = [
        (page_object.name_create_on_view_candidate, "Diego Interview"),
        (page_object.observations_interviews_create_on_view_candidate, "Observations testing."),
        (page_object.result_interviews_create_on_view_candidate, "87.50")]

    # For to verify the text on the required fields.
    for field in fields:
        webdriver.send_keys_to_element(field[0], field[1])

    # Click on the save button to create the request on the subpanel.
    webdriver.click_button(page_object.save_button_candidate_interview_view_candidate)