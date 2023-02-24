from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

# Set browser options to make it headless.
option = Options()
# option.add_argument("--headless")
# option.add_argument('--disable-gpu')

# fixture where is set the chrome driver as default, implicit wait to 10, to return the driver and quit.
@pytest.fixture
def browser():
    driver = webdriver.Chrome(options= option)
    driver.implicitly_wait(5)
    driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    yield driver
    driver.quit()