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
project_dropdown_create_invoice = (By.XPATH,'//*[@id="select2-project_list-container"]')
academy_project_option = (By.XPATH,'//li[text()="Academy Old"]')
title_field_create_invoice = (By.XPATH,'//*[@id="txt_title"]')
terms_dropdown_create_invoice = (By.XPATH,'//*[@id="slcterms"]')
freeform_radio_create_invoice = (By.XPATH,'//*[@id="pagecontent"]/div/div[2]/div[4]/div/label[1]/input')
prefilled_with_work_radio_create_invoice = (By.XPATH,'//*[@id="pagecontent"]/div/div[2]/div[4]/div/label[2]/input')
project_number_create_invoice = (By.XPATH,'//*[@id="txt_project"]')
status_dropdown_create_invoice = (By.XPATH,'//*[@id="slcstatus"]')
status_option_create_invoice = (By.XPATH, '//*[@id="slcstatus"]/option[1]')
purchase_order_number_create_invoice = (By.XPATH,'//*[@id="txt_purchase_orden"]')
description_create_invoice = (By.XPATH,'//*[@id="txt_description"]')
save_btn_create_invoice = (By.XPATH,'//*[@id="btn_create"]')