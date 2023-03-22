import pages.locators as page_object
from pages.functions import actions
from pages.common import login
import credentials.credentials as account
import time

def test_SCRM_352_sort_candidate(browser):
    
    # Using the fixture configuration run the browser.
    webdriver = actions(browser)

#LOGIN & HOMEPAGE

    # Log in to the page with valid credentials.
    login(webdriver, account.username_valid, account.password_valid, page_object.title_homepage)

    # Mouse hover and click all.
    webdriver.hover_and_click_element(page_object.all_dropdown)

    # Click the candidates option on All.
    webdriver.click_button(page_object.candidate_option)

#CANDIDATES
     
    # Validate the Candidates title page.
    webdriver.compare_title(page_object.title_candidates)

    # Ascending
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.name_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.name_on_table_candidate, 'Aarón Alonso, Sibaja Méndez')

    # Descending 
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.name_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.name_on_table_candidate, 'Óscar, Cordero Fernández')

    # Ascending
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.first_name_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.first_name_on_table_candidate, 'Aarón')

    # Descending
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.first_name_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.first_name_on_table_candidate, 'Óscar')

    # Ascending
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.last_name_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.last_name_on_table_candidate, 'A')

    # Descending
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.last_name_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.last_name_on_table_candidate, 'Zúñiga Morera')

    # Ascending
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.city_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.city_on_table_candidate, 'Agua caliente')

    # Descending
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.city_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.city_on_table_candidate, 'Zona Bananera (Orihueca)')

    # Ascending
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.country_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.country_on_table_candidate, 'AFGHANISTAN') 

    # Descending
    # Click on the name's sort of the table.
    webdriver.click_button(page_object.country_sort_candidate)

    # Check the text of the column on the table.
    webdriver.verify_text(page_object.country_on_table_candidate, 'VENEZUELA')           

    # time.sleep(5)