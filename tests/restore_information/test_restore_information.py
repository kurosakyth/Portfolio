import pages.locators as page_object
from pages.functions import actions
import pages.common as common
import credentials.credentials as account

def test_restore_information(browser):
    
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

    repeat = True

    while repeat == True:
        # Write on the search input for a candidate.
        webdriver.send_keys_to_element(page_object.search_candidate, 'Waldina')
        
        if repeat == True:
            # Click on the candidate searched.
            webdriver.click_button(page_object.result_searched_test_candidate)

            # Verify the candidate title of the page.
            webdriver.compare_title(page_object.title_waldina_candidate_view)
                
            # Click on delete button on the candidate view.
            webdriver.click_button(page_object.delete_button_view_candidate)

            # Accept the alert to delete.
            webdriver.alert_click()

            # Verify the candidate title of the page.
            webdriver.compare_title(page_object.title_candidates)           

# Delete the records correctly, but when it ends, fails.