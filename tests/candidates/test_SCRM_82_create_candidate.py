import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time

def test_SCRM_26_candidate(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#CANDIDATE

    # Go to the Candidates page.
    common.all_option_selector(webdriver)

    # Click on Create Candidate.
    webdriver.click_button(page_object.create_candidate)

    # Click on the Save button to Create a Candidate.
    webdriver.click_button(page_object.save_btn_create_candidate)

    # Parameterize the validation messages.
    fields = [
    (page_object.first_name_validation_message_candidate, 'Missing required field: First Name'),
    (page_object.document_number_validation_candidate, 'Missing required field: Document Number'),
    (page_object.mobile_validation_candidate, 'Missing required field: Mobile'),
    (page_object.country_validation_candidate, 'Missing required field: Country'),
    (page_object.state_province_validation_candidate, 'Missing required field: State/Province'),
    (page_object.last_name_validation_candidate, 'Missing required field: Last Name'),
    (page_object.email_validation_candidate, 'Missing required field: Email'),
    (page_object.city_validation_candidate, 'Missing required field: City')]
    
    # For to verify the text on the 
    for field in fields:
        webdriver.verify_text(field[0], field[1])

    # Fill the spaces to create a candidate.