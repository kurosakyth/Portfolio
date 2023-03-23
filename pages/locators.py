from selenium.webdriver.common.by import By

#URL
url = "http://develop.devcrm.site/"

#LOGIN
title_login = "CecropiaCRM"
homepage_error = (By.XPATH, '//span[text() = "You must specify a valid username and password."]')
error_message_login = "You must specify a valid username and password."
username = (By.ID, 'user_name')
password = (By.ID, 'username_password')
login_btn = (By.ID, 'bigbutton')

#HOMEPAGE
title_homepage = "Home » CecropiaCRM"
all_dropdown = (By.ID, 'grouptab_7')
invoice_option = (By.XPATH, '//*[@id="toolbar"]/ul/li[8]/span[2]/ul/li[32]/a')
profile_option = (By.ID, 'with-label')
logout_option = (By.XPATH, '//div[@class="desktop-bar"]/ul/li/ul/li/a[@id="logout_link"]')
candidate_option = (By.XPATH, '//*[@id="toolbar"]/ul/li[9]/span[2]/ul/li[13]/a')

#INVOICES
title_invoice = "Invoices » CecropiaCRM"
h1_invoice = (By.XPATH, '//*[@id="pagecontent"]/h1')
list_of_invoice_text = (By.XPATH, '//*[@id="mainSkillsDiv"]/div/div[1]/h3')
create_invoice = (By.XPATH, '//*[@id="actionMenuSidebar"]/ul/li[1]/a/div[2]')
view_invoice = (By.XPATH, '//*[@id="actionMenuSidebar"]/ul/li[2]/a/div[2]')
search_invoice = (By.XPATH, '//*[@id="dataTableInvoicesInformation_filter"]/label/input')
num_column_invoice = (By.XPATH, '//*[@id="dataTableInvoicesInformation"]/thead/tr/th[2]')
title_column_invoice = (By.XPATH, '//*[@id="dataTableInvoicesInformation"]/thead/tr/th[3]')

#CREATE INVOICES
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

#CANDIDATE
title_candidates = "Candidate » CecropiaCRM"
create_candidate = (By.XPATH,'//*[@id="actionMenuSidebar"]/ul/li[1]/a/div[2]')
view_candidate = (By.XPATH,'//*[@id="actionMenuSidebar"]/ul/li[2]/a/div[2]')
import_candidate = (By.XPATH,'//*[@id="actionMenuSidebar"]/ul/li[3]/a/div[2]')
recently_viewed_candidate = (By.XPATH,'//*[@id="recentlyViewedSidebar"]/h2')
h1_title_candidate = (By.XPATH,'//*[@id="pagecontent"]/h1')
excel_candidate = (By.XPATH,'//*[@id="dataTableCandidates_wrapper"]/div[1]/button/span')
search_candidate = (By.XPATH,'//*[@id="dataTableCandidates_filter"]/label/input')
security_groups_candidate = (By.XPATH,'//*[@id="massassign_form"]/table[1]/tbody/tr/td[1]/h3/span')
assign_button_candidate = (By.XPATH,'//*[@id="massassign_form"]/table[2]/tbody/tr/td/input[1]')
remove_button_candidate = (By.XPATH,'//*[@id="massassign_form"]/table[2]/tbody/tr/td/input[2]')
name_on_table_candidate = (By.ID, 'txt_name')
first_name_on_table_candidate = (By.ID, 'txt_first_name')
last_name_on_table_candidate = (By.ID, 'txt_last_name')
city_on_table_candidate = (By.ID, 'txt_city')
country_on_table_candidate = (By.ID, 'txt_country')
name_sort_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[2]')
first_name_sort_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[3]')
last_name_sort_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[4]')
city_sort_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[5]')
country_sort_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[6]')
    #CANDIDATE - Columns of table
name_column_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[2]')
first_name_column_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[3]')
last_name_column_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[4]')
city_column_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[5]')
country_column_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/thead/tr/th[6]')
    #CANDIDATE - Entries Dropdown
entries_dropdown_candidate = (By.ID, 'dataTableCandidates_length')
entrie_1_option_candidate = (By.XPATH, '//*[@id="dataTableCandidates_length"]/label/select/option[1]')
entrie_2_option_candidate = (By.XPATH, '//*[@id="dataTableCandidates_length"]/label/select/option[2]')
entrie_3_option_candidate = (By.XPATH, '//*[@id="dataTableCandidates_length"]/label/select/option[3]')
entrie_4_option_candidate = (By.XPATH, '//*[@id="dataTableCandidates_length"]/label/select/option[4]')
    #CANDIDATE - Toogle Column Options
toogle_column_candidate = (By.XPATH,'//*[@id="mainSkillsDiv"]/div/div[1]/span')
name_toogle_option_candidate = (By.XPATH, '//*[@id="mainSkillsDiv"]/div/div[1]/a[1]')
last_name_toogle_option_candidate = (By.XPATH, '//*[@id="mainSkillsDiv"]/div/div[1]/a[2]')
country_toogle_option_candidate = (By.XPATH, '//*[@id="mainSkillsDiv"]/div/div[1]/a[3]')
city_toogle_option_candidate = (By.XPATH, '//*[@id="mainSkillsDiv"]/div/div[1]/a[4]')
    #CANDIDATE - Group Dropdown
group_dropdown_candidate = (By.ID, 'massassign_group')
none_group_option_candidate = (By.XPATH, '//*[@id="massassign_group"]/option[1]')
hr_group_option_candidate = (By.XPATH, '//*[@id="massassign_group"]/option[2]')
private_group_option_candidate = (By.XPATH, '//*[@id="massassign_group"]/option[3]')
qa_security_group_option_candidate = (By.XPATH, '//*[@id="massassign_group"]/option[4]')
qa_test_group_option_candidate = (By.XPATH, '//*[@id="massassign_group"]/option[5]')

#CREATE CANDIDATE
save_btn_create_candidate = (By.ID, 'SAVE')
first_name_validation_message_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[1]/div[2]/div')
document_number_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[5]/div[2]/div')
mobile_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[9]/div[2]/div')
country_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[21]/div[2]/div')
state_province_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[25]/div[2]/div')
last_name_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[2]/div[2]/div')
email_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[6]/div[2]/div')
city_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[22]/div[2]/div')
#'//li[text()="Academy Old"]'