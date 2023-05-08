#-- Paste this code on the resources/"Run test.bat"

#-- Run all the tests:

cd ..
pipenv run python -m pytest -s --html=reports/report.html .\tests\runner\test_all.py -n 3 
pause

#-- Run Candidates tests:

cd ..
pipenv run python -m pytest -s --html=reports/report.html .\tests\runner\test_candidates.py -n 3
pause

#-- Run invoices tests:

cd ..
pipenv run python -m pytest -s --html=reports/report.html .\tests\runner\test_invoices.py -n 3
pause

IMPORTANT: Is required to run the tests/candidates/test_SCRM_82_create_candidate.py two times before run the Run_tests.bat
(pipenv run python -m pytest -s --html=reports/report.html .\tests\candidates\test_SCRM_82_create_candidate.py)

Links:
Test Plan: https://docs.google.com/document/d/197eMvxysvSs55MB4OCdI0cQqOIPal2aUbkVv2RUy6vo/edit
Automation test cases: https://docs.google.com/spreadsheets/d/1yjJANykVDHbdJdjOpfb5uUzxse2yU0KH-xcSwyYXl5M/edit#gid=0
Dev:  http://develop.devcrm.site/
Test repository: https://app.qase.io/project/SCRM
Github repository: https://github.com/asantamariamultiplied/AutomationSuiteCRM
Requirements:
ChromeDriver:
Set the Chrome driver’s path, create a Selenium file on this following direction:
Windows: C:\Selenium
Mac: pathFinder > shift + command + g : look for /usr/ > local > bin : paste chromedriver there.
The Chrome driver should have the name “chromedriver”.
Install python on the system from the https://www.python.org/downloads/
Download the Visual Studio Code (VSC): https://code.visualstudio.com/download
Pipenv:
On the terminal of VSC
pip install pipenv
pipenv install
pipenv install selenium
pipenv install pytest
pipenv install pytest-xdist (is to run tests on parallel)
pipenv install pytest-html
pipenv run python -m pytest (if this displays an error you must..)
pipenv --python #pythonVersionInstalled
pipenv update
Pytest important information:
While using pytest is important to follow a specific structure, there should always be a file “tests”, where the tests will be located. Also the name of the tests to run should contain the name “test_name.py”.

 Inside the test_name.py should contain a def function which also should be named as “test_name():”.


Github:
Credential manager: delete the credentials for github on windows, only if you have issues with the github account.
Make sure you have access to the repository - Ask the lead for access.

Open the Visual Studio code.
Open your terminal in the local repository destination.
git clone https://github.com/asantamariamultiplied/AutomationSuiteCRM.git
Change to the branch assigned (The lead should give you the branch to work).
git branch (to display the list of branches).
git checkout name_of_the_branch (to change to the branch assigned).
Now you have the automation project for SuiteCRM.

Push something to the repository on the branch assigned.
Make sure you have changes on your local repository.
Save the files.
Open the terminal.
git status (to check the files modified which are color red).
git add name_of_the_file (this adds the file selected to commit).
git status (now the file added is color green, that means the file was added).
Repeat the git add command the times necessary to add the files desired.
Create a commit: git commit -m “example of a commit”
Upload the changes to your branch: git push -u origin name_of_your_branch
Go to the github repository and check your branch.
Note that the branch says “updated # minutes ago”.

Create a pull request.
On the repository on github.
Click on the Pull requests tab.
Click on New pull request.
Select your branch.
Note that you are going to merge the branch selected (the one assigned to you) to the main.
Add a message for the pull request.
Click on create pull request.
Wait for the merge or the rejection of the pull request.


Standards:
For files:
credentials.
pages (logic).
reports.
resources.
tests.
Module_1 (invoice).
Module_2 (skills).
runners.

For functions (defs):
open_page 
compare_title
get_clickable_element
click_button 
find_element 
send_keys_to_element 
hover_and_click_element 
verify_text
get_elements_from_page 
verify_elements_exist

For credentials name:
username_invalid_1
password_invalid_1
username_valid
password_valid