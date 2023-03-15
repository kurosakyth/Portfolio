import pages.locators as page_object
from pages.functions import actions
from pages.common import login
import credentials.credentials as account
import time

def test_SCRM_43_invoices(browser):
    
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

    # Validate the objects of the Invoice page.
    webdriver.verify_elements_exist([page_object.create_invoice, page_object.view_invoice, page_object.h1_invoice, page_object.list_of_invoice_text, page_object.search_invoice, page_object.num_column_invoice, page_object.title_column_invoice])
#Missing the elements to validate, check the test case.