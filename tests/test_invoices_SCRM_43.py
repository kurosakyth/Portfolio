import pages.page_objects as page_object
from pages.actions import actions
from pages.common import login
import credentials.credentials as account
import time

def test_invoices_SCRM_43(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

    # Mouse hover and click all.
    webdriver.hover_and_click_btn(page_object.all_dropdown)

    # Click the invoices option on All.
    webdriver.click_btn(page_object.invoice_option)

#INVOICES

    # Validate the Invoices title page.
    webdriver.title_compare(page_object.title_invoice)

    # Validate the objects of the Invoice page.
    webdriver.validate_elements_exist_on_page([page_object.create_invoice, page_object.view_invoice, page_object.h1_invoice, page_object.list_of_invoice_text, page_object.search_invoice, page_object.num_column_invoice, page_object.title_column_invoice])
#Missing the elements to validate, check the test case.