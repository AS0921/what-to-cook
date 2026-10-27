# Сервис - "Что приготовить"

Сервис подбирает блюда, для приготовления которых используются продукты введенные Пользователем. 
Также показывает, каких ингредиентов не хватает.
Пригодится, если есть продукты в холодильнике, но не знаете, что приготовить. 


## Возможности

| Маршрут | Описание |
|---|---|
| `GET /health` | проверка работоспособности |
| `GET /version` | версия приложения |
| `GET /recipes` | список всех блюд |
| `GET /recipes/{id}` | одно блюдо по номеру (404, если нет) |
| `GET /ingredients` | все продукты, которые знает сервис |
| `GET /match?products=яйца,молоко` | подбор блюд по продуктам |

Рецепты хранятся в файле `recipes.csv`.

## Запуск

Для разработки:

```bash
python -m uvicorn app_final:app --reload
```

Для обычной работы:

```bash
python -m uvicorn app_final:app --host 127.0.0.1 --port 8000
```

Документация с формой для запросов: http://127.0.0.1:8000/docs

## Тесты

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

Тесты автоматически запускаются в GitHub Actions при каждом push и pull request (`.github/workflows/ci.yml`).
После успешных тестов собирается artifact `what-to-cook` с файлами приложения.

## Диагностика

Проверить, что сервис работает:

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/version
```

Ожидается `{"status":"ok"}` и номер версии.

**Логи** выводятся в терминал, где запущен uvicorn: загрузка рецептов при старте, каждый запрос подбора, ненайденные блюда (WARNING).

| Проблема | Решение |
|---|---|
| `No module named uvicorn` | не включено окружение: `source .venv/bin/activate`, затем `python -m pip install -r requirements.txt` |
| `Address already in use` | порт занят другим запуском: остановить его (`Ctrl+C`) или найти через `ss -ltnp \| grep 8000` и завершить `kill PID`; либо запустить с `--port 8001` |
| `FileNotFoundError: recipes.csv` | неверный путь в `RECIPES_FILE` или файл отсутствует |
| `curl: Failed to connect` | приложение не запущено |
