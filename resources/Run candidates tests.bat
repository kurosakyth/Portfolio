cd ..
pipenv run python -m pytest -s --html=reports/report.html .\tests\runner\test_candidates.py -n 2
pause