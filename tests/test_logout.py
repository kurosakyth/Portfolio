from selenium.webdriver.common.by import By
import pages.page_objects as page_object
from pages.actions import actions
import credentials.credentials as account
import time

def test_logout(browser):

    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

    # Open the browser with the page.
    webdriver.load_page(page_object.url)

    # Validate the Login title page.
    webdriver.title_compare(page_object.tittle_login)

#LOGIN

    # Search the input and send keys.
    webdriver.send_keys(page_object.username, account.username)
    
    # Search the input and send keys.
    webdriver.send_keys(page_object.password, account.password)

    # Click the log in btn.
    webdriver.click_btn(page_object.login_btn)

#HOMEPAGE

    # Validate the Homepage title page.
    webdriver.title_compare(page_object.title_crm)

    # Mouse hover the profile icon.
    webdriver.hover_and_click_btn(page_object.profile_option)

    # Mouse hover and click all.
    webdriver.click_btn(page_object.logout_option)

    # Validate the Login title page.
    webdriver.title_compare(page_object.tittle_login)

    #time.sleep(5)