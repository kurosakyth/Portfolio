import pages.page_objects as page_object
import credentials.credentials as account

def login(webdriver):
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
