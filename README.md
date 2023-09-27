# PetsDemoProject
Тестовое задание по REST API. Тест-кейсы описаны в файле тест_кейсы.xlsx. 

Все тесты кроме одного проходят. Нестабильно ведет себя один тест test_update_category_false_id - обновление категории животного по несуществующему id. Этот тест иногда проходит, а иногда нет.

**Запуск проекта:**

**1. Установить зависимости**

- Python Framework для pytest (https://docs.pytest.org/en/7.4.x/)
- Библиотека отчетов pytest-html (https://pytest-html.readthedocs.io/en/latest/) 
- Библиотека requests (`pip install requests`)
- Библиотека jsonschema (`pip install jsonschema`)
- Фреймворк отчетов Yandex Allure (https://github.com/allure-framework)
- Allure-Pytest adapter (`pip install allure-pytest`)

**2. Клонировать проект** (`git clone https://github.com/biikter/PetsDemoProject.git`)

**3. Прописать логин и пароль в файле data/config_data.json. Если тестируете сервис, который запущен локально, то заменить url.**

**4. Запустить тест с командной строки. Набрать в папке проекта:** 
```
pytest --html=report.html --alluredir=allure-results PetsDemoProject.py
```
**5. Посмотреть отчет pytest-html -> открыть файл report.html** 

**6. Посмотреть отчет Allure -> набрать в командной строке:**
```
allure serve allure-results
```


