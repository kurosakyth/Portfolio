from selenium.webdriver.common.by import By

#URL
url = "http://develop.devcrm.site/"

#Login
title_login = "CecropiaCRM"
homepage_error = (By.XPATH, '//span[text() = "You must specify a valid username and password."]')
error_message_login = "You must specify a valid username and password."
username = (By.ID, 'user_name')
password = (By.ID, 'username_password')
login_btn = (By.ID, 'bigbutton')

#Homepage
title_homepage = "Home » CecropiaCRM"
all_dropdown = (By.ID, 'grouptab_6')
invoice_option = (By.XPATH, '//*[@id="toolbar"]/ul/li[8]/span[2]/ul/li[32]/a')
profile_option = (By.ID, 'with-label')
logout_option = (By.XPATH, '//div[@class="desktop-bar"]/ul/li/ul/li/a[@id="logout_link"]')

#Invoices
title_invoice = "Invoices » CecropiaCRM"
h1_invoice = (By.XPATH, '//*[@id="pagecontent"]/h1')
list_of_invoice_text = (By.XPATH, '//*[@id="mainSkillsDiv"]/div/div[1]/h3')
create_invoice = (By.XPATH, '//*[@id="actionMenuSidebar"]/ul/li[1]/a/div[2]')
view_invoice = (By.XPATH, '//*[@id="actionMenuSidebar"]/ul/li[2]/a/div[2]')
search_invoice = (By.XPATH, '//*[@id="dataTableInvoicesInformation_filter"]/label/input')
num_column_invoice = (By.XPATH, '//*[@id="dataTableInvoicesInformation"]/thead/tr/th[2]')
title_column_invoice = (By.XPATH, '//*[@id="dataTableInvoicesInformation"]/thead/tr/th[3]')


#Create Invoices
title_create_invoice = "CREATE » Invoices » CecropiaCRM"
project_dropdown_create_invoice = (By.ID,'select2-project_list-container')
academy_project_option = (By.XPATH,'//li[text()="Academy Old"]')
title_field_create_invoice = (By.ID,'txt_title')
terms_dropdown_create_invoice = (By.ID,'slcterms')
freeform_radio_create_invoice = (By.XPATH,'//*[@id="pagecontent"]/div/div[2]/div[4]/div/label[1]/input')
prefilled_with_work_radio_create_invoice = (By.XPATH,'//*[@id="pagecontent"]/div/div[2]/div[4]/div/label[2]/input')
project_number_create_invoice = (By.ID,'txt_project')
status_dropdown_create_invoice = (By.ID,'slcstatus')
status_option_create_invoice = (By.XPATH, '//*[@id="slcstatus"]/option[1]')
purchase_order_number_create_invoice = (By.ID,'txt_purchase_orden')
description_create_invoice = (By.ID,'txt_description')
save_btn_create_invoice = (By.ID,'btn_create')