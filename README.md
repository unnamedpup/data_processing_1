
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
4. Запустите установочный скрипт:

   ```
    chmod +x setup.sh  # Даем права на выполнение
    ./setup.sh         # Запускаем скрипт
   ```
## Запуск
Для запуска проекта выполните команду (указывать путь до файла обязательно):
```
python main.py <path/to/file>
```

## Тестирование
Для запуска тестов выполните команду:
```
python -m pytest tests/
```

## Структура проекта

```
data_processing_1/
├── utils/                 # Исходный код
│   ├── parsers/           # Парсеры
│   │   ├── __init__.py 
│   │   └── parsers.py       
│   └── analyzer/          # Анализатор текста
│       ├── __init__.py
│       └── analyzer.py
│
├── tests/                 # Тесты
│   ├── data/              # Данные для тестов
│   ├── test_parsers.py
│   ├── test_analyzer.py
│   └── ...
│
├── main.py                # Основной скрипт обработки
├── requirements.txt       # Зависимости Python
├── setup.sh               # Скрипт установки
└── README.md              
```


