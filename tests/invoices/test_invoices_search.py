import pages.locators as page_object
from pages.functions import actions
from pages.common import login
import credentials.credentials as account
import time

def test_invoices_search(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

    # Mouse hover and click all.
    webdriver.hover_and_click_element(page_object.all_dropdown)

    # Click the invoices option on All.
    webdriver.click_button(page_object.invoice_option)

#INVOICES

    # Validate the Invoices title page.
    webdriver.compare_title(page_object.title_invoice)

    # Search a specific word on the search input.
    webdriver.send_keys_to_element(page_object.search_invoice, "QA WORK TYPE")
    # time.sleep(5)