
Устанавливаем зависимости

pip install -r requirements.txt

Запуск тестов с отчетом Allure

py -m pytest --alluredir=test_results

Вывод отчета
allure serve test_results