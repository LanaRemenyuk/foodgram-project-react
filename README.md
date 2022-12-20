![foodgram_workflow](https://github.com/LanaRemenyuk/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

# Foodgram

Проект доступен по адресу http://158.160.55.155
Доступы от admin:
- lan2828@yandex.ru
- cut12cut123

## Продуктовый помощник: сервис с рецептами

Авторизованные пользователи могут подписываться на понравившихся авторов, 
добавлять рецепты в избранное, в покупки, а также скачивать список покупок. 
Неавторизованным пользователям доступна регистрация, авторизация, просмотр рецептов других 
пользователей.

### Стек технологий
Python 3.7, Django 2.2.19, Django REST Framework 3.12, PostgresQL

###### Установка проекта в dev-режиме:
- Клонируйте репозиторий на Ваш компьютер
- Создайте и активируйте виртуальное окружение
```

python -m venv venv

source venv/Scripts/activate
``` 
-  Установите все зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Выполните миграции
```
python manage.py migrate
``` 
- Запустите сервер :
```
python manage.py runserver
```
###### Запуск с использованием CI/CD:
- Установите docker, docker-compose на сервере ВМ Yandex.Cloud:

```ssh username@ip```

```sudo apt update && sudo apt upgrade -y && sudo apt install curl -y```

```sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh```

```sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose```

```sudo chmod +x /usr/local/bin/docker-compose```

- Создайте папку infra:

```mkdir infra```

- Перенесите файлы docker-compose.yml и default.conf на сервер:

```scp docker-compose.yml username@server_ip:/home/<username>/infra```

```scp default.conf <username>@<server_ip>:/home/<username>/infra```

- Создайте файл .env в дериктории infra:

```touch .env```

- Заполните в настройках репозитория секреты .env:

DB_ENGINE="ваш тип модуля управления БД"
DB_NAME="имя БД"
POSTGRES_USER="имя пользователя БД"
POSTGRES_PASSWORD="пароль пользователя БД"
DB_HOST="хост БД, напимер localhost или db"
DB_PORT="5432"

- Для доступа к контейнеру выполните следующие команды:

```udo docker-compose exec backend python manage.py makemigrations```

```sudo docker-compose exec backend python manage.py migrate --noinput```

```sudo docker-compose exec backend python manage.py createsuperuser```

```sudo docker-compose exec backend python manage.py collectstatic --no-input```

###### Запуск проекта через Docker:

- В папке infra выполните команду, чтобы собрать контейнер:

```sudo docker-compose up -d```

Для доступа к контейнеру выполните следующие команды:

```sudo docker-compose exec backend python manage.py makemigrations```

```sudo docker-compose exec backend python manage.py migrate --noinput```

```sudo docker-compose exec backend python manage.py createsuperuser```

```sudo docker-compose exec backend python manage.py collectstatic --no-input```

- Дополнительно можно наполнить базу данных ингредиентами:

```sudo docker-compose exec backend python manage.py ingred```


### Автор:
Светлана Ременюк



