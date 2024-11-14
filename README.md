# Модуль обратной связи для Django
Этот проект предоставляет модуль обратной связи для сбора заявок от пользователей. Пользователи могут отправлять заявки через специальную форму, введя заголовок, текст сообщения, ФИО и контактную информацию. После отправки заявки пользователь видит сообщение об успешной отправке, а данные сохраняются в базе данных. Статус обработки заявки пользователь может посмотреть на главной странице.

## Функционал
- Форма для отправки заявки: Пользователь может ввести заголовок, текст заявки, ФИО и контактную информацию.
- Сообщение об успешной отправке: После отправки пользователь видит сообщение «Ваша заявка принята».
- Сохранение данных: Введенные данные сохраняются в базе данных для дальнейшей обработки администрацией.
- Все заявки и статус их обработки достпуны на главной странице.

## Установка и настройка
### Требования
- Python 3.6+
- Django 3.2+

### Установка проекта
1. Клонируйте репозиторий.
2. Установите зависимости: `pip install -r requirements.txt`
4. Выполните миграции для настройки базы данных: `python manage.py migrate`
5. Запустите сервер: `python manage.py runserver`

## Использование
Для получения подробной информации об эндпоинтах и других аспектах использования, пожалуйста, ознакомьтесь с [документацией в Wiki](https://github.com/Misha-creato/django_feedback/wiki).