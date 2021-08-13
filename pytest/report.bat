pytest -s -q --alluredir ./report/result_allure
allure generate report/result_allure -o report/allure_html