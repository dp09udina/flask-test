# flask-test

## Запуск через docker

В папке blazegraph должен лежать JAR-файл с СУБД Blazegraph: https://github.com/blazegraph/database/releases/tag/BLAZEGRAPH_2_1_6_RC

```docker compose up```

## Запуск вручную

Запускаем БД:

```java -server -Xmx4g -jar blazegraph.jar```

Запускаем flask

```python test-app\app.py --port 5000```

По умолчанию приложение запускается на порту 5000.
Порт указывается в .env. Пример в .env_test

Файл конфигурации с подключением БД: [config.json](https://github.com/dp09udina/flask-test/blob/main/test-app/config/config.json)

## API

Описание api: [openapi.yaml](https://github.com/dp09udina/flask-test/blob/main/openapi/openapi.yaml)