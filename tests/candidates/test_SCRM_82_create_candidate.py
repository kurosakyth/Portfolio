import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time
from selenium.webdriver.common.alert import Alert

def test_SCRM_82_create_candidate(browser):
    
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

    # Validate the title of the Create Candidates page.
    webdriver.compare_title(page_object.title_create_candidate)

    # Click on the Save button to Create a Candidate to display the validation messages.
    webdriver.click_button(page_object.save_btn_create_candidate)

    # Parameterize the validation messages.
    fields_for_validations = [
    (page_object.first_name_validation_message_candidate, 'Missing required field: First Name'),
    (page_object.document_number_validation_candidate, 'Missing required field: Document Number'),
    (page_object.mobile_validation_candidate, 'Missing required field: Mobile'),
    (page_object.country_validation_candidate, 'Missing required field: Country'),
    (page_object.state_province_validation_candidate, 'Missing required field: State/Province'),
    (page_object.last_name_validation_candidate, 'Missing required field: Last Name'),
    (page_object.email_validation_candidate, 'Missing required field: Email'),
    (page_object.city_validation_candidate, 'Missing required field: City')]
    
    # For to verify the text on the required fields.
    for field in fields_for_validations:
        webdriver.verify_text(field[0], field[1])

    # Parameterize information to write on the form.
    fields_to_fill_the_information = [
    (page_object.first_name_create_candidate, 'Walden'),
    (page_object.document_create_candidate, '99557733'),
    (page_object.mobile_create_candidate, '9955112233'),
    (page_object.country_create_candidate, 'NORUEGA'),
    (page_object.state_province_create_candidate, 'Oslo'),
    (page_object.last_name_create_candidate, 'Schmidt'),
    (page_object.email_create_candidate, 'walschmidt'),
    (page_object.city_create_candidate, 'Kolbotn')]
    
    # For to verify the text on the required fields.
    for field in fields_to_fill_the_information:
        webdriver.send_keys_to_element(field[0], field[1])
    
#Change the time.sleep for something that wait to the form to be completed.
    time.sleep(3)
    # Click the Save button.
    webdriver.click_button(page_object.save_btn_create_candidate)

    # Validate the title of the Create Candidates page.
    webdriver.compare_title(page_object.title_walden_candidate_view)

    # Verify the correctly creation of the candidate.
    webdriver.verify_text(page_object.name_view_candidate, 'Walden')
#Is not part of the testcase.
    # Delete the Candidate created.
    # webdriver.click_button(page_object.delete_view_candidate)

    # # Accept the alert to delete the Candidate.
    # Alert(browser).accept()

    # time.sleep(5)