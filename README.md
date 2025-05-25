
# First task (Parser)

## Описание

Проект реализует синтаксический анализатор для обработки html страниц и документов разных форматов (pdf, doc, docx, djvu)


## Настройка

1. Склонируйте репозиторий:
    ```
    git clone <repository-url>
    cd data_processing_1
    ```
2. Создайте виртуальное окружение:

    ```
    python -m venv <venv_name>
    ```
3. Активируйте виртуальное окружение:

   На Windows: ```<venv_name>\Scripts\activate```

   На Linux/macOS: ```source <venv_name>/bin/activate```
4. Установите зависимотси:

   ```
    pip install -r requirements.txt
   ```
## Запуск
Для запуска проекта выполните команду:
```
python main.py
```

## Тестирование
Для запуска тестов выполните команду:
```
python -m pytest tests/
```

## Системные зависимости

Для работы с некоторыми форматами файлов требуются:

- DOC файлы:  
  Установите `antiword`:
  ```
  # Linux
  sudo apt-get install antiword

  # macOS
  brew install antiword
  ```

- DJVU файлы:  
  Установите `djvutxt` (из пакета DjVuLibre):
  ```
  # Linux
  sudo apt-get install djvulibre-bin

  # macOS
  brew install djvulibre
  ```
  
## Языковые модели для spaCy

Для работы с текстами на разных языках необходимо установить соответствующие модели spaCy:

```
python -m spacy download en_core_web_sm  # Английский
python -m spacy download ru_core_news_sm  # Русский
python -m spacy download de_core_news_sm  # Немецкий
python -m spacy download fr_core_news_sm  # Французский
python -m spacy download es_core_news_sm  # Испанский
