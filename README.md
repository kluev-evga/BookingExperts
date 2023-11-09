# BookingExperts

### Адрес веб-сайта: [BookingExperts](http://kluev.dynnamn.ru/hotels)

## Стек проекта

![Python](https://img.shields.io/badge/python-3.10-blue.svg?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/fastapi-0.103.2-blue.svg?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-2.0.21-blue.svg?style=for-the-badge)
![Alembic](https://img.shields.io/badge/alembic-1.12.0-blue.svg?style=for-the-badge)
![asyncpg](https://img.shields.io/badge/asyncpg-0.28.0-blue.svg?style=for-the-badge)
![python-jose](https://img.shields.io/badge/python--jose-3.3.0-blue.svg?style=for-the-badge)
![passlib](https://img.shields.io/badge/passlib-1.7.4-blue.svg?style=for-the-badge)
![fastapi-cache2](https://img.shields.io/badge/fastapi--cache2-0.2.1-blue.svg?style=for-the-badge)
![celery](https://img.shields.io/badge/celery-5.3.4-blue.svg?style=for-the-badge)
![flower](https://img.shields.io/badge/flower-2.0.1-blue.svg?style=for-the-badge)
![pillow](https://img.shields.io/badge/pillow-10.1.0-blue.svg?style=for-the-badge)
![sqladmin](https://img.shields.io/badge/sqladmin-0.15.2-blue.svg?style=for-the-badge)
![pytest](https://img.shields.io/badge/pytest-7.4.3-blue.svg?style=for-the-badge)
![pytest-asyncio](https://img.shields.io/badge/pytest--asyncio-0.21.1-blue.svg?style=for-the-badge)
![gunicorn](https://img.shields.io/badge/gunicorn-21.2.0-blue.svg?style=for-the-badge)
![Nginx](https://img.shields.io/badge/nginx-1.19.3-blue.svg?style=for-the-badge&logo=nginx&logoColor=11FF44)
![PostgreSQL](https://img.shields.io/badge/postgreSQL-15.0-blue.svg?style=for-the-badge&logo=postgresql&logoColor=66EEFF)
![Docker](https://img.shields.io/badge/docker-24.0.5-blue.svg?style=for-the-badge&logo=docker&logoColor=33AAFF)
[![Docker-compose](https://img.shields.io/badge/Docker%20compose-2.10.0-blue?style=for-the-badge&logo=Docker&logoColor=white)](https://www.docker.com/)
[![Лицензия](https://img.shields.io/github/license/kluev-evga/BookingExperts?color=blue&style=for-the-badge&labelColor=333333&logo=github)](https://github.com/kluev-evga/BookingExperts/blob/master/LICENSE)
[![Размер кода](https://img.shields.io/github/languages/code-size/kluev-evga/BookingExperts?style=for-the-badge&labelColor=333333&logo=github)](https://github.com/kluev-evga/BookingExperts)

## О проекте:

BookingExperts - это веб-приложение, предназначенное для удобного бронирования и управления бронями в гостиницах. Проект
создан с целью предоставить надежное и эффективное решение для управления бронями и бронирования номеров.

Особенности:

* Современные Технологии: BookingExperts построен на основе высокопроизводительного фреймворка FastAPI и использует
  PostgreSQL в качестве надежной базы данных, взаимодействуя с мощным SQLAlchemy.

* Мгновенные Резервации: приложение предоставляет клиентам быстрый и удобный способ бронирования номеров и
  дополнительных услуг.

* Аутентификация и Безопасность: уделено большое внимание безопасности данных и используются современные методы
  аутентификации, чтобы обеспечить защиту информации.

Для запуска необходим файл .env в корневой директории с указанными переменными:

```plaintext
DB_HOST=                               # Например, localhost
DB_PORT=                               # Например, 5432
DB_USER=                               # Например, postgres
DB_PASS=                               # Например, postgres
DB_NAME=                               # Например, booking

SECRET_KEY=                            # Можно сгенерировать с помощью команды: openssl rand -base64 32
ALGORITHM=                             # Например, HS256

TEST_DB_HOST=localhost
TEST_DB_PORT=5432
TEST_DB_USER=booking
TEST_DB_PASS=admin
TEST_DB_NAME=test

REDIS_HOST='localhost'
REDIS_PORT=6379

SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_USER=
SMTP_PASSWORD= 
```

Для начала работы, создайте указанную базу данных в PostgreSQL, например, с именем "booking". Выполните следующие шаги:

1. Запустите PostgreSQL с пользователем, указанным в .env:
   ```
   sudo -u postgres psql
   ```

2. Создайте базу данных "booking":
   ```
   CREATE DATABASE booking;
   ```

3. Проверьте, что база данных успешно создана:
   ```
   \l
   ```

4. Выйдите из psql:
   ```
   \q
   ```

5. Выполните миграции, используя Alembic:
   ```
   alembic revision --autogenerate -m 'initial'    # Генерация миграций
   alembic upgrade head                           # Применение миграций
   ```

## Лицензия 📜

Этот проект распространяется под лицензией `Apache License`. Дополнительную информацию можно найти
в [LICENSE](https://github.com/kluev-evga/BookingExperts/blob/master/LICENSE).