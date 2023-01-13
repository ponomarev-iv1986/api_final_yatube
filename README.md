### Описание проекта:

Backend для проекта YaTube

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ponomarev-iv1986/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Эндопоинты и примеры запросов:

* /api/v1/posts/

> GET - получение публикаций

> POST - создание публикации
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

* /api/v1/posts/{id}/

> GET - получение публикации

> PUT - обновление публикации
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

> PATCH - частичное обновление публикации
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

> DELETE - удаление публикации

* /api/v1/posts/{post_id}/comments/

> GET - получение комментариев

> POST -добавление комментария
```
{
  "text": "string"
}
```

* /api/v1/posts/{post_id}/comments/{id}/

> GET - получение комментария

> PUT - обновление комментария
```
{
  "text": "string"
}
```

> PATCH - частичное обновление комментария
```
{
  "text": "string"
}
```

> DELETE - удаление комментария

* /api/v1/groups/

> GET - список сообществ

* /api/v1/groups/{id}/

> GET - информация о сообществе

* /api/v1/follow/

> GET - подписки

> POST - подписаться
```
{
  "following": "string"
}
```

* /api/v1/jwt/create/

> POST - получить JWT-токен
```
{
  "username": "string",
  "password": "string"
}
```

* /api/v1/jwt/refresh/

> POST - обновить JWT-токен
```
{
  "refresh": "string"
}
```

* /api/v1/jwt/verify/

> POST - проверить JWT-токен
```
{
  "token": "string"
}
```