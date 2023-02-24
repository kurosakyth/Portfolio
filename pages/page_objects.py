from selenium.webdriver.common.by import By

#URL
url = "http://develop.devcrm.site/"
tittle_login = "CecropiaCRM"

#Login
title_crm = "Home » CecropiaCRM"
username = (By.XPATH, '//input[@id="user_name"]')
password = (By.XPATH,'//input[@id="username_password"]')
login_btn = (By.XPATH, '//*[@id="bigbutton"]')

#Homepage
all_dropdown = (By.XPATH, '//a[@id="grouptab_6"]')
invoice_option = (By.XPATH, '//*[@id="toolbar"]/ul/li[8]/span[2]/ul/li[31]/a')
profile_option = (By.XPATH, '//*[@id="with-label"]')
logout_option = (By.XPATH, '//div[@class="desktop-bar"]/ul/li/ul/li/a[@id="logout_link"]')

#Invoices
title_invoice = "Invoices » CecropiaCRM"
create_invoice = (By.XPATH, '//*[@id="actionMenuSidebar"]/ul/li[1]/a/div[2]')

#Create Invoices
title_create_invoice = "CREATE » Invoices » CecropiaCRM"
project_dropdown = ''