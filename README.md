
# Test task for "Python Developer (Fullstack)" position

<br/>

## Requirements

* docker with docker-compose
* libraries from requirements.txt

<br/>

## Building the containers

```sh
make build         # create docker image
make up            # bring containers up
make firstbdsetup  # run migrations, add user groups and create super user
# or
make all           # builds, brings containers up, run migration, add user groups and create super user
```

<br/>

# Task description

Написать Веб-приложение для просмотра изображений.  
На главном экране можно просмотреть все сохранённые изображения, а также найти нужные изображения с помощью фильтров и поиска.  
Предусмотреть получение определенного объёма изображений от сервера (пагинация/lazy loading).  
При нажатии на изображение увеличить его и показать детали.

Список деталей:
* Описание картинки
* Размер картинки
* Преобладающий цвет
* Средний цвет изображения
* Цветовая палитра

Должна быть возможность добавлять новые изображения. Каждое изображение можно заменить или удалить.  
Реализовать аутентификацию и авторизацию, на основе ролей.  
Роли User доступны все вышеописанные взаимодействия с изображениями, а также смена личного пароля.  
Роли Admin, доступно всё что доступно роли Employee, а также возможность добавлять, изменять и удалять пользователей

Для фронтенда можно использовать React, Angular, Vue.js  
Для бэкенда можно использовать Django, Flask, FastApi или другие технологии  
Базы: SQLite, PostgreSQL, MySQL или другие
