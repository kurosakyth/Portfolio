from selenium.webdriver.common.by import By

#URL
url = "http://develop.devcrm.site/"
url_candidate = "https://develop.devcrm.site/index.php?module=CC_Candidate&action=index&parentTab=All"
url_profile = "https://develop.devcrm.site/index.php?module=CC_Profile&action=index&parentTab=All"

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
candidate_option_all_dropdown = (By.XPATH, '//div[@id="toolbar"]/ul/li[@class="topnav all"]/span[@class="notCurrentTab"]/ul/li/a[text()="Candidate"]')
profile_option_all_dropdown = (By.XPATH, '//div[@id="toolbar"]/ul/li[@class="topnav all"]/span[@class="notCurrentTab"]/ul/li/a[text()="Profile"]')

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
title_waldina_candidate_view = ('Waldina, Schmidtita » Candidate » CecropiaCRM')
edit_button_view_candidate = (By.ID, 'edit_button')
duplicate_button_view_candidate = (By.ID, 'duplicate_button')
delete_button_view_candidate = (By.ID, 'delete_button')
find_button_duplicate_view_candidate = (By.ID, 'merge_duplicate_button')
view_change_log_button_view_candidate = (By.ID, 'btn_view_change_log')

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



#PROFILE
title_profile = "Profile » CecropiaCRM"
create_profile = (By.XPATH,'//*[@id="actionMenuSidebar"]/ul/li[1]/a/div[2]')
view_profile = (By.XPATH,'//*[@id="actionMenuSidebar"]/ul/li[2]/a/div[2]')
import_profile = (By.XPATH,'//*[@id="actionMenuSidebar"]/ul/li[3]/a/div[2]')
recently_viewed_profile = (By.XPATH,'//*[@id="recentlyViewedSidebar"]/h2')
    #PROFILE - Columns of table
system_only_column_profile = (By.XPATH, '//a[contains(text(), "System Only")]')
name_column_profile = (By.XPATH, '//a[contains(text(), "Name")]')
published_column_profile = (By.XPATH, '//a[contains(text(), "Published")]')
    #PROFILE - Second row of the table
checkbox_dropdown_profile = (By.XPATH, '//ul[@id="selectLinkTop"]/li/label/span')
select_this_page_checkbox_option_profile = (By.ID, 'button_select_this_page_top')
select_all_checkbox_option_profile = (By.ID, 'button_select_all_top')
deselect_checkbox_option_profile = (By.ID, 'button_deselect_top')
bulk_button_profile = (By.ID, 'select_actions_disabled_top')
filter_button_profile = (By.XPATH, '//*[@id="pagination"]/td/table/tbody/tr/td/ul[3]/li//a')
column_chooser_button_profile = (By.XPATH, '//*[@id="pagination"]/td/table/tbody/tr/td/ul[5]/li//a')
start_arrow_profile = (By.ID, 'listViewStartButton_top')
previous_arrow_profile = (By.ID, 'listViewPrevButton_top')
next_arrow_profile = (By.ID, 'listViewNextButton_top')
end_arrow_profile = (By.ID, 'listViewEndButton_top')
option_on_the_table_profile = (By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr[1]/td[4]/b')

#CREATE PROFILE
title_create_profile = "CREATE » Profile » CecropiaCRM"
save_btn_create_profile = (By.XPATH, '//div/input[@title="Save"]')
error_message_create_profile = (By.XPATH, '//div[@id="detailpanel_-1"]/div/div/div/div/div[text()="Missing required field: Name"]')
name_create_profile = (By.ID, 'name')

#VIEW PROFILE
automation_profile_created = "Automation_profile » Profile » CecropiaCRM"
title_contains_view_profile = "» Profile » CecropiaCRM"
edit_button_view_profile = (By.ID, 'edit_button')
duplicate_button_view_profile = (By.ID, 'duplicate_button')
delete_button_view_profile = (By.ID, 'delete_button')
find_button_duplicate_view_profile = (By.ID, 'merge_duplicate_button')
view_change_log_button_view_profile = (By.ID, 'btn_view_change_log')
previous_arrow_view_profile = (By.XPATH, '//*[@id="pagecontent"]/table[1]/tbody/tr/td[2]/table/tbody/tr/td/span/a[1]')
next_arrow_view_profile = (By.XPATH, '//*[@id="pagecontent"]/table[1]/tbody/tr/td[2]/table/tbody/tr/td/span/a[2]')

    #BASIC SUBPANEL
basic_sub_view_profile = (By.XPATH, '//*[@id="pagecontent"]/div[2]/div[4]/div[2]/div[1]/a/div')
name_basic_view_profile = (By.XPATH, '//div[contains(text(), "Name")]') 
system_only_basic_view_profile = (By.XPATH, '//div[contains(text(), "System Only")]')

    #SKILLS & QUALIFICATIONS SUBPANEL
skills_quallifications_sub_view_profile = (By.XPATH, '//*[@id="pagecontent"]/div[3]/div[1]/div/a/div')
            #SKILLS
h3_sk_view_profile = (By.XPATH, '//*[@id="pagecontent"]/div[3]/div[1]/div/a/div')
show_entries_sk_view_profile = (By.XPATH, '//*[@id="dataTableSkills_length"]')
                    #SKILLS DROPDOWN
select_a_sk_view_profile = (By.XPATH, '//span[contains(text(), "Select a Skill")]') 
options_list_sk_view_profile = (By.XPATH, '//ul[@id="select2-skill_list-results"]/li')

name_sk_view_profile = (By.XPATH, '//*[@id="dataTableSkills"]/thead/tr/th[1]')
expected_rating_sk_view_profile = (By.XPATH, '//th[contains(text(), "Expected Rating")]')
experience_sk_view_profile = (By.XPATH, '//th[contains(text(), "Experience")]')
showing_entries_sk_view_profile = (By.XPATH, '//*[@id="dataTableSkills_info"]')
previous_sk_view_profile = (By.XPATH, '//*[@id="dataTableSkills_previous"]')
next_sk_view_profile = (By.XPATH, '//*[@id="dataTableSkills_next"]')
            #QUALIFICATIONS
h3_quali_view_profile = (By.XPATH, '//*[@id="mainQualificationsDiv"]/div/div[1]/h3')
show_entries_quali_view_profile = (By.XPATH, '//*[@id="mainQualificationsDiv"]/div/div[1]/h3')
favourites_quali_view_profile = (By.ID, "justFavouritesDiv")
                    #QUALIFICATIONS DROPDOWN
select_quali_view_profile = (By.XPATH, '//span[contains(text(), "Select a Qualification")]')
options_list_quali_view_profile = (By.XPATH, '//ul[@id="select2-qualification_list-results"]/li')

name_quali_view_profile = (By.XPATH, '//*[@id="mainQualificationsDiv"]/div/div[1]/h3')
level_quali_view_profile = (By.XPATH, '//*[@id="mainQualificationsDiv"]/div/div[1]/h3')
suport_requiered_quali_view_profile = (By.XPATH, '//*[@id="mainQualificationsDiv"]/div/div[1]/h3')
showing_entries_quali_view_profile = (By.XPATH, '//*[@id="mainQualificationsDiv"]/div/div[1]/h3')
previous_quali_view_profile = (By.XPATH, '//*[@id="mainQualificationsDiv"]/div/div[1]/h3')
next_quali_view_profile = (By.XPATH, '//*[@id="mainQualificationsDiv"]/div/div[1]/h3')
    
    #PROFILE MATCHES SUBPANEL 
profile_match_sub_view_profile = (By.XPATH, '//*[@id="pagecontent"]/div[4]/div[1]/div/a/div')
employees_prof_match_view_profile = (By.XPATH, '//nav/a[contains(text(), "Employees")]')
candidates_prof_match_view_profile = (By.XPATH, '//nav/a[contains(text(), "Candidates")]')
active_only_prof_match_view_profile = (By.XPATH, '//*[@id="tab-employees"]/div/div/div[1]/label[1]')
unassigned_only_prof_match_view_profile = (By.XPATH, '//*[@id="tab-employees"]/div/div/div[1]/label[2]')
copy_btn_prof_match_view_profile = (By.XPATH, '//*[@id="dataTableEmployeesMatchingInformation_wrapper"]//span[contains(text(), "Copy")]') #Enseñar a meli
pdf_btn_prof_match_view_profile = (By.XPATH, '//*[@id="dataTableEmployeesMatchingInformation_wrapper"]//span[contains(text(), "PDF")]')
csv_btn_prof_match_view_profile = (By.XPATH, '//*[@id="dataTableEmployeesMatchingInformation_wrapper"]//span[contains(text(), "CSV")]')
excel_btn_prof_match_view_profile = (By.XPATH, '//*[@id="dataTableEmployeesMatchingInformation_wrapper"]//span[contains(text(), "Excel")]')
show_rows_btn_prof_match_view_profile = (By.XPATH, '//*[@id="dataTableEmployeesMatchingInformation_wrapper"]//span[contains(text(), "Show")]')
name_column_prof_match_view_profile = (By.XPATH, '//table[@id="dataTableEmployeesMatchingInformation"]//th[contains(text(), "Name")]')
country_law_column_prof_match_view_profile = (By.XPATH, '//table[@id="dataTableEmployeesMatchingInformation"]//th[contains(text(), "Country Law")]')
english_column_prof_match_view_profile = (By.XPATH, '//table[@id="dataTableEmployeesMatchingInformation"]//th[contains(text(), "English Level")]')
profile_rating_column_prof_match_view_profile = (By.XPATH, '//table[@id="dataTableEmployeesMatchingInformation"]//th[contains(text(), "Profile Rating")]')
active_column_prof_match_view_profile = (By.XPATH, '//table[@id="dataTableEmployeesMatchingInformation"]//th[contains(text(), "Active")]')
is_assigned_column_prof_match_view_profile = (By.XPATH, '//table[@id="dataTableEmployeesMatchingInformation"]//th[contains(text(), "Is Assigned")]')
chart_column_prof_match_view_profile = (By.XPATH, '//table[@id="dataTableEmployeesMatchingInformation"]//th[contains(text(), "Chart")]')

    # OPTIONS
all_sub_view_profile = (By.ID, 'All_sp_tab')
careers_sub_view_profile = (By.ID, 'Careers_sp_tab')
hr_sub_view_profile = (By.ID, 'HR_sp_tab')
other_sub_view_profile = (By.ID, 'Other_sp_tab')

    #RECUITMENT REQUEST SUBPANEL
recruitment_request_sub_view_profile = (By.XPATH, '//ul[@id="subpanel_list"]/li[@id="whole_subpanel_cc_recruitment_request_cc_profile"]')
create_recruit_req_view_profile = (By.XPATH, '//*[@id="cc_recruitment_request_cc_profile_create_button"]')
name_create_recruit_req_view_profile = (By.XPATH, '//input[@id="name"]')
save_btn_create_recruit_req_view_profile = (By.ID, "CC_Recruitment_Request_subpanel_save_button")
select_recruit_req_view_profile = (By.XPATH, '//*[@id="cc_recruitment_request_cc_profile_select_button"]')
option_select_recruit_req_view_profile = (By.XPATH, '//*[@id="MassUpdate"]/table[2]/tbody/tr[2]/td[3]/a')

    #JOB DESCRIPTION
job_description_sub_profile = (By.XPATH, '//ul[@id="subpanel_list"]/li[@id="whole_subpanel_cc_job_description_cc_profile"]')
create_job_description_view_profile = (By.XPATH, '//*[@id="cc_job_description_cc_profile_create_button"]')
name_create_job_description_view_profile = (By.XPATH, '//input[@id="name"]')
save_btn_create_job_description_view_profile = (By.ID, "CC_Job_Description_subpanel_save_button")
select_job_description_view_profile = (By.XPATH, '//*[@id="cc_job_description_cc_profile_select_button"]')
option_select_job_description_view_profile = (By.XPATH, '//*[@id="MassUpdate"]/table[2]/tbody/tr[1]/td[3]/a')

    #JOB OFFER
job_offer_view_profile = (By.XPATH, '//ul[@id="subpanel_list"]/li[@id="whole_subpanel_cc_profile_cc_job_offer"]')
create_job_offer_view_profile = (By.XPATH, '//*[@id="cc_profile_cc_job_offer_create_button"]')
name_create_job_offer_view_profile = (By.XPATH, '//input[@id="name"]')
save_btn_create_job_offer_view_profile = (By.ID, "CC_Job_Offer_subpanel_save_button")
select_job_offer_view_profile = (By.XPATH, '//*[@id="cc_profile_cc_job_offer_select_button"]')
option_select_job_offer_view_profile = (By.XPATH, '//*[@id="MassUpdate"]/table[2]/tbody/tr[1]/td[3]/a')

security_groups_view_profile = (By.XPATH, '//ul[@id="subpanel_list"]/li[@id="whole_subpanel_securitygroups"]')