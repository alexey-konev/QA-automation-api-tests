
# QA Automation Pet-Project
## ENG

## About

This project was created to practice writing automated tests.

For API and database testing an educational application based on FastAPI 
and PostgreSQL was created.

For UI testing the project uses the publicly available SauceDemo demo website.

## Tech Stack

Python, pytest, Playwright, FastAPI, PostgreSQL, REST API, Docker, GitHub Actions, Allure

## Project Structure

1. `app/` - FastAPI application
2. `clients/` - clients for working with the API and database
3. `tests/`
   1. `api` - tests for HTTP methods (GET, POST, PUT, PATCH, DELETE)
   2. `db` - CRUD tests for the `User` entity in the database (read, create, delete)
   3. `ui` - tests for login and the main user flow
      1. `pages/` - Page Object classes for the pages used in tests
4. `.env.example` - example file with the required environment variables. `.env` is used 
for local execution and is not committed to Git
5. `Dockerfile`, `compose.yaml` - files for running the project in Docker
6. `requirements.txt` - project dependencies

## Requirements

To install all required dependencies, run:

```bash
pip install -r requirements.txt
```

## Local Setup

1. Clone the repository:

```bash
git clone https://github.com/alexey-konev/QA-automation-api-tests.git
```

2. Create a `.env` file in the project root with the required environment variables. 
See `.env.example` for an example and a list of required variables.

3. Create a PostgreSQL database named `qa_api_db` and initialize the `users` table. 
The SQL query for creating the table is provided in `sql/init.sql`.

4. Start the FastAPI application:

```bash
uvicorn app.app:app --reload
```

The project is now ready to run the tests.

## Environment Variables

`API_ACCESS_TOKEN` — authentication token. Since this is an educational application, 
the expected authorization token is hardcoded in the application as `secret-token`.

`TEST_USERNAME` — username for logging in to the SauceDemo website. 
The publicly available username is `standard_user`.

`TEST_PASSWORD` — password for logging in to the SauceDemo website. 
The publicly available password is `secret_sauce`.

`DB_HOST` — database host. Default: `localhost`.

`DB_PORT` — database port. Default: `5432`.

`DB_NAME` — database name. Default: `qa_api_db`.

`DB_USER` — database username. Default: `postgres`.

`DB_PASSWORD` — database user password. Default: `postgres`.

## Running Tests

Use the corresponding command to run the tests:

```bash
# API tests
python -m pytest tests/api

# Database tests
python -m pytest tests/db

# UI tests
python -m pytest tests/ui

# All tests
python -m pytest tests
```

## Docker

API and database tests are run in Docker. UI tests are not run in Docker.

To run the API and database tests in Docker, start Docker and run:

```bash
docker compose up --build
```

## CI/CD

The project's CI is configured to run tests on every push.

Tests can also be triggered manually in GitHub via:

`Actions > Run workflow`

UI and API+DB tests are executed in separate jobs.

After the tests are completed, Allure results from both jobs are merged, 
an Allure Report is generated, and the report is published to GitHub Pages.

## Allure Report

The latest CI test report is available on GitHub Pages.

To generate an Allure Report locally, add `--alluredir=allure-results` 
to the test command, for example:

```bash
python -m pytest tests/ui --alluredir=allure-results
```

Then run:

```bash
allure.cmd serve allure-results
```

The report will open in your browser.

#

## RU
## О проекте 
Проект для практики написания автотестов. 

Для тестов API и базы данных было создано учебное приложение на основе FastAPI + 
PostgreSQL. 

Для UI тестов используется общедоступный сайт-песочница https://www.saucedemo.com

## Стэк технологий 
Python, pytest, Playwright, FastAPI, PostgreSQL, REST API, Docker, 
GitHub Actions, Allure

## Структура проекта 
1. `app/` - приложение на основе FastAPI + PostgreSQL
2. `clients/` - клиенты для работы с API и базой данных
3. `tests/`
   1. `api/` - тесты на методы HTTP-запросов (get, post, put, patch, delete)
   2. `db/` - CRUD тесты по сущности "user" в базе данных (получить, создать, удалить)
   3. `ui/` - тесты на логин и основной путь пользователя
      1. `pages/` - Page Object классы используемых в тестах страниц
4. `.env.example` - пример файла с необходимыми переменными окружения. .env 
используется для локального запуска и не добавляется в Git
5. `Dockerfile`, `compose.yaml` - файлы для запуска проекта в Docker
6. `requirements.txt` - зависимости, необходимые для работы проекта
   
## Зависимости 
Чтобы установить все необходимые зависимости, запустите команду:

```bash
pip install -r requirements.txt
```

## Локальная настройка проекта 
1. Склонируйте репозиторий 

```bash
git clone https://github.com/alexey-konev/QA-automation-api-tests.git
```

2. Создайте файл .env в корне проекта с необходимыми переменными окружения. 
Пример и список нужных переменных в файле `.env.example`
3. Через PostgreSQL создайте базу данных `qa_api_db` с таблицей `users` 
(SQL запрос для создания таблицы представлен в файле проекта `sql/init.sql`)
4. Запустите приложение FastAPI с помощью команды: 

```bash
uvicorn app.app:app --reload
```

Проект готов к запуску тестов

## Переменные окружения 
`API_ACCESS_TOKEN`: токен аутентификации. Так как это учебное приложение, 
ожидаемый токен авторизации захардкожен в приложении - `secret-token`

`TEST_USERNAME`: имя пользователя для логина на сайте SauceDemo. 
Предоставляется в открытом доступе - `standard_user`

`TEST_PASSWORD`: пароль пользователя для логина на сайте SauceDemo. 
Предоставляется в открытом доступе - `secret_sauce`

`DB_HOST`: сервер вашей базы данных с таблицей users. По умолчанию - `localhost`

`DB_PORT`: порт вашей базы данных с таблицей users. По умолчанию - `5432`

`DB_NAME`: наименование вашей базы данных с таблицей users. По умолчанию - `qa_api_db`

`DB_USER`: имя пользователя базы данных. По умолчанию - `postgres`

`DB_PASSWORD`: пароль пользователя базы данных. По умолчанию - `postgres`

## Запуск тестов 
Для прогона тестов воспользуйтесь соответствующей командой:

```bash
# API tests
python -m pytest tests/api

# Database tests
python -m pytest tests/db

# UI tests
python -m pytest tests/ui

# All tests
python -m pytest tests
```

## Docker
В докере запускаются API и DB тесты, UI тесты не запускаются. 
Для прогонов API и DB тестов в докере запустите сам Docker и воспользуйтесь командой:

```bash
docker compose up --build   
```

## CI/CD
CI проекта настроен так, что тесты запускаются при каждом push. 

Тесты также можно запустить вручную в GitHub: `Actions > Run Workflow`

UI и API+DB тесты запускаются в отдельных jobs.
После их выполнения Allure results объединяются,
генерируется отчёт и публикуется в GitHub Pages.

## Allure Report
Последний отчёт CI по прогону тестов можно найти в GitHub Pages. 

Чтобы получить отчет при локальном прогоне тестов, добавьте `--alluredir=allure-results` к запуску тестов, например:

```bash
python -m pytest tests/ui --alluredir=allure-results
```

Затем выполните команду:

```bash
allure.cmd serve allure-results
```

Отчет откроется в вашем браузере