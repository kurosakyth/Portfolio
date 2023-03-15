import pages.locators as page_object
from pages.functions import actions
from pages.common import login
import credentials.credentials as account
import time

def test_create_invoices(browser):
    
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

    # Click the create invoice or the invoice dropdown button.
    webdriver.hover_and_click_element(page_object.create_invoice)

#Create Invoices

    # Validate the Create Invoice title page.
    webdriver.compare_title(page_object.title_create_invoice)

    # Displays the project list.
    webdriver.click_button(page_object.project_dropdown_create_invoice)

    # Select academy as the dropdown option on the project dropdown.
    webdriver.click_button(page_object.academy_project_option)
    
    # Send the title to the create invoice page.
    webdriver.send_keys_to_element(page_object.title_field_create_invoice, "Mr")

    # Write the # of the project.
    webdriver.send_keys_to_element(page_object.project_number_create_invoice, "321")

    # Displays the status list.
    webdriver.click_button(page_object.status_dropdown_create_invoice)

    # Select an option of the status list.
    webdriver.click_button(page_object.status_option_create_invoice)

    # Write a purchase order number.
    webdriver.send_keys_to_element(page_object.purchase_order_number_create_invoice, "456")

    # Write the description.
    webdriver.send_keys_to_element(page_object.description_create_invoice, "Description automation test")

    # Click the save button.
    # webdriver.click_btn_new(page_object.save_btn_create_invoice)

    # time.sleep(5)