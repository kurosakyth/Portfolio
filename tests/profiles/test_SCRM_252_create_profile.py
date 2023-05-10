import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account
import time
from selenium.webdriver.common.alert import Alert

def test_SCRM_252_create_profile(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    common.login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

#CANDIDATE

    # Open the browser with the page.
    webdriver.open_page(page_object.url_profile)

    # Validate the Login title page.
    webdriver.compare_title(page_object.title_profile)

    # Click on Create Profile.
    webdriver.click_button(page_object.create_profile)

    # Validate the title of the Create Profile page.
    webdriver.compare_title(page_object.title_create_profile)

    # Click on the Save button to Create a Profile to display the validation messages.
    webdriver.click_button(page_object.save_btn_create_profile)

    # Verify the error message of the Name.
    webdriver.verify_text(page_object.error_message_creating_profile, "Missing required field: Name")

#     # Parameterize information to write on the form.
#     fields_to_fill_the_information = [
#     (page_object.first_name_create_candidate, 'Walden'),
#     (page_object.document_create_candidate, '99557733'),
#     (page_object.mobile_create_candidate, '9955112233'),
#     (page_object.country_create_candidate, 'NORUEGA'),
#     (page_object.state_province_create_candidate, 'Oslo'),
#     (page_object.last_name_create_candidate, 'Schmidt'),
#     (page_object.email_create_candidate, 'walschmidt'),
#     (page_object.city_create_candidate, 'Kolbotn')]
    
#     # For to verify the text on the required fields.
#     for field in fields_to_fill_the_information:
#         webdriver.send_keys_to_element(field[0], field[1])
    
# #Change the time.sleep for something that wait to the form to be completed.
#     time.sleep(3)
#     # Click the Save button.
#     webdriver.click_button(page_object.save_btn_create_candidate)

#     # Validate the title of the Create Candidates page.
#     webdriver.compare_title(page_object.title_walden_candidate_view)

#     # Verify the correctly creation of the candidate.
#     webdriver.verify_text(page_object.name_view_candidate, 'Walden')