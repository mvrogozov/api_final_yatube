## Проект Yatube_api.
Проект для доступа к yatube через API.

Yatube_api предоставляет программный интерфейс для связи с различными приложениями.

## Возможности

- Доступ к постам
- Доступ к комментариям
- Доступ к подпискам
- Контроль прав доступа

## Установка

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:mvrogozov/api_final_yatube.git
```
```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

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

### Примеры запросов

Получение публикаций:
```
GET http://127.0.0.1:8000/api/v1/posts/
```
Создание публикации:
```
POST http://127.0.0.1:8000/api/v1/posts/
{
    "text": "Post text"
}
```
Получение комментариев:
```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Добавление комментария:
```
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
{
    "text": "Coment text"
}
```

