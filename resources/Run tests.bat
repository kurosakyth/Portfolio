cd ..
pipenv run python -m pytest -s --html=reports/report.html .\tests\runner\test_all.py -n 4
pause