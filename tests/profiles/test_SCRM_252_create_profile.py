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

    # Click on Create Profile.
    webdriver.click_button(page_object.create_profile)

    # Validate the title of the Create Profile page.
    webdriver.compare_title(page_object.title_create_profile)

    # Click on the Save button to display the validation messages.
    webdriver.click_button(page_object.save_btn_create_profile)

    # Verify the error message of the Name.
    webdriver.verify_text(page_object.error_message_create_profile, "Missing required field: Name")
    
    # Fill the name of the profile.
    webdriver.send_keys_to_element(page_object.name_create_profile, "Automation_profile")

    #Change the time.sleep for something that wait to the form to be completed.
    time.sleep(3)
    
    # Click on the Save button to Create a Profile.
    webdriver.click_button(page_object.save_btn_create_profile)
    
    # Validate the title of the Create Profile page.
    webdriver.compare_title(page_object.automation_profile_created)