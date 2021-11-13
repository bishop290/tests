
# Примеры некоторых тестов

## директория /postman
- содержит пробные тесты api сервиса [rbaskets.in](https://rbaskets.in)
- запустить тесты: newman run rbaskets.in.postman_collection.json -e rbaskets.in-env.postman_environment.json

## директория /selen
- содержит пробные скрипты тестирования нескольких ссылок UI при помощи python selenium для сайта [selenium.dev/api](https://www.selenium.dev/selenium/docs/api/py/api.html)
- попробовать запустить тесты: python3 selen/test/test_selen.py
- примеры логов прохождения тестов: selen/log*.txt

## директория /sql
- Cодержит файл "data-sql-train". В нем расположены примеры моих запросов sql (тренировка на сайте: [sql-ex.ru](https://www.sql-ex.ru/)).
- Содержит файл "computers.sql". Это схема одной из тренировочных баз с сайта [sql-ex.ru](https://www.sql-ex.ru/), которую я соствил сам для MySql. Можно создать свою базу и писать тренировочные запросы локально. 