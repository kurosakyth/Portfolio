from selenium.webdriver.common.by import By

#URL
url = "http://develop.devcrm.site/"
url_candidate = "https://develop.devcrm.site/index.php?module=CC_Candidate&action=index&parentTab=All"

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
candidate_option = (By.XPATH, '//div[@id="toolbar"]/ul/li[@class="topnav all"]/span[@class="notCurrentTab"]/ul/li/a[text()="Candidate"]')

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
result_searched_test_candidate = (By.XPATH, '//*[@id="dataTableCandidates"]/tbody/tr[1]/td[2]/div/a')#Para seleccionar el elemento de la tabla.
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
title_create_candidate = 'CREATE » Candidate » CecropiaCRM'
first_name_create_candidate = (By.ID, 'first_name')
first_name_validation_message_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[1]/div[2]/div')
document_create_candidate = (By.ID, 'document_number')
document_number_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[5]/div[2]/div')
mobile_create_candidate = (By.ID, 'mobile')
mobile_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[9]/div[2]/div')
country_create_candidate = (By.ID, 'country')
country_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[21]/div[2]/div')
state_province_create_candidate = (By.ID, 'state_province')
state_province_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[25]/div[2]/div')
last_name_create_candidate = (By.ID, 'last_name')
last_name_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[2]/div[2]/div')
email_create_candidate = (By.ID, 'email')
email_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[6]/div[2]/div')
city_create_candidate = (By.ID, 'city')
city_validation_candidate = (By.XPATH, '//*[@id="detailpanel_-1"]/div/div/div[22]/div[2]/div')
save_btn_create_candidate = (By.XPATH, '//div/input[@title="Save"]')

#VIEW CANDIDATE
title_walden_candidate_view = ('Walden, Schmidt » Candidate » CecropiaCRM')
edit_view_candidate = (By.ID, 'edit_button')
duplicate_view_candidate = (By.ID, 'duplicate_button')
delete_view_candidate = (By.ID, 'delete_button')
find_duplicate_view_candidate = (By.ID, 'merge_duplicate_button')
view_change_log_view_candidate = (By.ID, 'btn_view_change_log')

    #SUBPANEL BASIC
basic_subp_view_candidate = (By.XPATH, '//*[@id="pagecontent"]/div[2]/div[4]/div[2]/div[1]/a/div')
name_view_candidate = (By.XPATH, '//*[@id="top-panel--1"]/div/div[1]/div[1]/div[2]')

    #SUBPANEL EXPERIENCE & EDUCATION
exp_educ_sub_view_candidate = (By.XPATH, '//*[@id="pagecontent"]/div[2]/div[4]/div[3]/div[1]/a/div')

    #SUBPANEL PROFILE MATCHER
profile_match_sub_view_candidate = (By.XPATH, '//*[@id="pagecontent"]/div[3]/div[1]/div/a/div')
all_match_sub_view_candidate = (By.XPATH, '//*[@id="All_sp_tab"]/a')
activities_match_sub_view_candidate = (By.XPATH, '//*[@id="Activities_sp_tab"]/a')
invoices_match_sub_view_candidate = (By.XPATH, '//*[@id="Invoices_sp_tab"]/a')
recruitment_match_sub_view_candidate = (By.XPATH, '//*[@id="Recruitment_sp_tab"]/a')
other_match_sub_view_candidate = (By.XPATH, '//*[@id="Other_sp_tab"]/a')
    #SUBPANEL GENERAL INPUTS
            #CREATE FROM THE MAIN PAGE
name_create_on_view_candidate = (By.ID, 'name')
phone_create_on_view_candidate = (By.ID, 'phone_office')
save_create_on_view_candidate = (By.ID, 'Accounts_subpanel_save_button')
description_create_on_view_candidate = (By.ID, 'description')
score_index__create_on_view_candidate = (By.ID, 'score_index')
            #SELECT FROM THE SECOND WINDOW
search_input_select_accounts_view_candidate = (By.XPATH, '//*[@id="name_advanced"]')
search_button_select_view_candidate = (By.XPATH, '//*[@id="search_form_submit"]')
    #SUBPANEL CANDIDATE ACCOUNTS
candidate_accounts_view_candidate = (By.ID, 'subpanel_title_cc_candidate_accounts')
create_accounts_view_candidate = (By.ID, 'cc_candidate_accounts_create_button')
select_accounts_view_candidate = (By.ID, 'cc_candidate_accounts_select_button')
qa_option_table_select_accounts_view_candidate = (By.XPATH, '//a[text()="qa ACCCOUNT"]')
    #SUBPANEL JOB OFFER
job_offer_view_candidate = (By.ID, 'subpanel_title_cc_candidate_cc_job_offer')
create_job_offer_view_candidate = (By.ID, 'cc_candidate_cc_job_offer_create_button')
select_job_offer_view_candidate = (By.ID, 'cc_candidate_cc_job_offer_select_button')
save_button_job_offer_view_candidate = (By.ID, 'CC_Job_Offer_subpanel_save_button')
net_developer_option_table_select_accounts_view_candidate = (By.XPATH, '//a[text()=".NET Developer"]')
    #SUBPANEL CANDIDATE NOTE
candidate_note_view_candidate = (By.ID, 'subpanel_title_cc_candidate_cc_candidate_note')
create_candidate_note_view_candidate = (By.ID , 'cc_candidate_cc_candidate_note_create_button')
select_candidate_note_view_candidate = (By.ID, 'cc_candidate_cc_candidate_note_select_button')
save_button_candidate_note_view_candidate = (By.ID, 'CC_Candidate_Note_subpanel_save_button')
javascript_option_candidate_note = (By.XPATH, '//a[text()="Javascript"]')
    #SUBPANEL INTERVIEWS
interviews_view_candidate = (By.ID, 'subpanel_title_cc_interviews_cc_candidate')
create_candidate_interviews_view_candidate = (By.ID, 'cc_interviews_cc_candidate_create_button')
observations_interviews_create_on_view_candidate = (By.ID, 'observation')
result_interviews_create_on_view_candidate = (By.ID, 'result')
approved_interviews_create_on_view_candidate = (By.XPATH, '//select[@id = "approved"]')
approved_option_interviews_create_on_view_candidate = (By.XPATH, '//option[@value="Yes"]')
date_button_interivews_create_on_view_candidate = (By.ID, 'interview_date_trigger')
date_option_interviews_create_on_view_candidate = (By.XPATH, '//td[contains(@class, "today")]')
select_candidate_interviews_view_candidate = (By.ID, 'cc_interviews_cc_candidate_select_button')
save_button_candidate_interview_view_candidate = (By.ID, 'CC_Interviews_subpanel_save_button')
interv_option_candidate_interviews_candidate = (By.XPATH, '//a[text()="Erick Interview"]')
    #SUBPANEL AVAILABILITY RELATED
availab_related_view_candidate = (By.ID, 'subpanel_title_cc_candidate_availability_cc_candidate')
create_availab_related_view_candidate = (By.ID, 'cc_candidate_availability_cc_candidate_create_button')
hour_start_time_create_related_view_candidate = (By.ID, 'time_1_hours')
minutes_start_time_create_related_view_candidate = (By.ID, 'time_1_minutes')
hour_end_time_create_related_view_candidate = (By.ID, 'time_2_hours')
minutes_end_time_create_related_view_candidate = (By.ID, 'time_2_minutes')
time_option_create_related_view_candidate = (By.XPATH, '//a[text()="11"]')
select_availab_related_view_candidate = (By.ID, 'cc_candidate_availability_cc_candidate_select_button')
save_button_availab_related_view_candidate = (By.ID, 'CC_Candidate_Availability_subpanel_save_button')
option_select_availab_related_view_candidate = (By.XPATH, '//a[text()="Fabricio Arce"]')
    #SUBPANEL TRACK LOG RELATED
track_log_related_view_candidate = (By.ID, 'subpanel_title_cc_candidate_track_log_cc_candidate')
create_track_log_view_candidate = (By.ID, 'formformcc_candidate_track_log_cc_candidate')
select_track_log_view_candidate = (By.ID, 'cc_candidate_track_log_cc_candidate_select_button')
save_button_track_log_view_candidate = (By.ID, 'CC_Candidate_Track_Log_subpanel_save_button')
option_select_track_log_view_candidate = (By.XPATH, '//a[text()="QA TEST TRACK"]')
    #SUBPANEL SKILLS
skills_view_candidate = (By.ID, 'subpanel_title_cc_candidate_cc_skill')
create_skills_view_candidate = (By.ID, 'formformcc_candidate_cc_skill')
select_skills_view_candidate = (By.ID, 'cc_candidate_cc_skill_select_button')
option_select_skills_view_candidate = (By.XPATH, '//a[text()=".net"]')
save_button_skills_view_candidate = (By.ID, 'CC_Skill_subpanel_save_button')
    #SUBPANEL SPECIAL NOTES
special_notes_view_candidate = (By.ID, 'subpanel_title_cc_candidate_notes')
create_special_notes_view_candidate = (By.ID, 'formformcc_candidate_notes')
display_portal_special_notes_view_candidate = (By.ID, 'portal_flag')
select_special_notes_view_candidate = (By.ID, 'cc_candidate_notes_select_button')
option_select_special_notes_view_candidate = (By.XPATH, '//a[text()="PDF created from system"]')
save_button_special_notes_view_candidate = (By.ID, 'Notes_subpanel_save_button')
    #SUBPANEL PERSONALITY TEST
personality_test_view_candidate = (By.ID, 'subpanel_title_cc_candidate_cc_personality_test')
create_personality_view_candidate = (By.ID, 'cc_candidate_cc_personality_test_create_button')
select_personality_view_candidate = (By.ID, 'cc_candidate_cc_personality_test_select_button')
option_select_personality_view_candidate = (By.XPATH, '//*[@id="MassUpdate"]/table[2]/tbody/tr[1]/td[1]/input')
save_button_personality_view_candidate = (By.ID, 'CC_Personality_Test_subpanel_save_button')
    #SUBPANEL QUALIFICATIONS
qualifications_view_candidate = (By.ID, 'subpanel_title_cc_candidate_cc_qualification')
create_qualifications_view_candidate = (By.ID, 'cc_candidate_cc_qualification_create_button')
select_qualifications_view_candidate = (By.ID, 'cc_candidate_cc_qualification_select_button')
option_select_qualifications_view_candidate = (By.XPATH, '//a[text()="Licenciatura en Sistemas Computacionales"]')
save_button_qualifications_view_candidate = (By.ID, 'CC_Qualification_subpanel_save_button')
#SUBPANELS FROM THE VIEW CANDIDATE

security_groups_view_candidate = (By.ID, 'subpanel_title_securitygroups')

#EDIT CANDIDATE
title_edit_walden = ('Edit » Walden, Schmidt » Candidate » CecropiaCRM')
title_view_waldina = ('Waldina, Schmidtita » Candidate » CecropiaCRM')
first_name_candidate_edit = (By.ID, 'first_name')
last_name_candidate_edit = (By.ID, 'last_name')
document_candidate_edit = (By.ID, 'document_number')
email_candidate_edit = (By.ID, 'email')
mobile_candidate_edit = (By.ID, 'mobile')
country_candidate_edit = (By.XPATH, '//div/input[@id="country"]')
city_candidate_edit = (By.XPATH, '//div/input[@id="city"]')
state_province_candidate_edit = (By.XPATH, '//div/input[@id="state_province"]')
    #EXPERIENCE & EDUCATION
employed_candidate_edit = (By.ID, 'currently_employed')
employer_candidate_edit = (By.ID, 'current_employer')
years_of_experience_candidate_edit = (By.ID, 'years_of_experience')
cancel_btn_candidate_edit = (By.XPATH, '//div[@class="buttons"]/input[@title="Cancel [Alt+l]"]')
upload_btn_candidate_edit = (By.XPATH, '//div[@class="buttons"]/button[text()="Upload Candidate"]')
#EDUCATION DROPDOWN
educa_candidate_diploma_edit = (By.XPATH, '//*[@id="education"]/option[1]')
educa_candidate_adgd_edit = (By.XPATH, '//*[@id="education"]/option[2]')
educa_candidate_babs_edit = (By.XPATH, '//*[@id="education"]/option[3]')
educa_candidate_mamsmba_edit = (By.XPATH, '//*[@id="education"]/option[4]')
educa_candidate_md_edit = (By.XPATH, '//*[@id="education"]/option[5]')
educa_candidate_jd_edit = (By.XPATH, '//*[@id="education"]/option[6]')
educa_candidate_phd_edit = (By.XPATH, '//*[@id="education"]/option[7]')
educa_candidate_doc_edit = (By.XPATH, '//*[@id="education"]/option[8]')