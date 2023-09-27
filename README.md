# PetsDemoProject
Тестовое задание по REST API

##Запуск проекта:

###1. Установить зависимости

- Python Framework для pytest (https://docs.pytest.org/en/7.4.x/)
- Библиотека отчетов pytest-html (https://pytest-html.readthedocs.io/en/latest/) 
- Библиотека requests ('pip install requests')
- Библиотека jsonschema ('pip install jsonschema')
- Фреймворк отчетов Yandex Allure (https://github.com/allure-framework)
- Allure-Pytest adapter ('pip install allure-pytest')

###2. Клонировать проект ('git clone https://github.com/biikter/PetsDemoProject.git')

###3. Прописать логин и пароль в файле data/config_data.json. Если тестируете сервис, который запущен локально, то заменить url.

###4. Запустить тест с командной строки ('pytest --html=report.html --alluredir=allure-results PetsDemoProject.py')

