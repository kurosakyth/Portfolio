Paste this code on the resources/"Run test.bat"

run all the tests:

cd ..
pipenv run python -m pytest -s --html=reports/report.html .\tests\runner\test_all.py -n 3 
pause

run invoices tests:

cd ..
pipenv run python -m pytest -s --html=reports/report.html .\tests\runner\test_invoices.py -n 1
pause