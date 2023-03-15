import pages.locators as page_object

def login(webdriver, username, password, title_of_the_page):
    
    # Open the browser with the page.
    webdriver.open_page(page_object.url)

    # Validate the Login title page.
    webdriver.compare_title(page_object.title_login)

#LOGIN

    # Search the input and send keys.
    webdriver.send_keys_to_element(page_object.username, username)
    
    # Search the input and send keys.
    webdriver.send_keys_to_element(page_object.password, password)

    # Click the log in btn.
    webdriver.click_button(page_object.login_btn)

#HOMEPAGE

    # Validate the Homepage title page.
    webdriver.compare_title(title_of_the_page)