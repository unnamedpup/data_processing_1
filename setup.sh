#!/bin/bash

# Скрипт установки зависимостей для проекта
set -e  # Прерывать выполнение при ошибках

OS=""
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
else
    echo "Неподдерживаемая ОС: $OSTYPE"
    exit 1
fi

# Установка системных пакетов
if [[ "$OS" == "linux" ]]; then
    sudo apt-get update
    sudo apt-get install -y antiword djvulibre-bin
elif [[ "$OS" == "macos" ]]; then
    brew install antiword djvulibre
fi

# Создание и активация venv (опционально)
#read -p "Создать виртуальное окружение Python? [y/n] " -n 1 -r
#echo
#if [[ $REPLY =~ ^[Yy]$ ]]; then
#    python -m venv venv
#    source venv/bin/activate
#fi

# Установка Python-зависимостей
pip install --upgrade pip
pip install -r requirements.txt

# Загрузка моделей spaCy
python -m spacy download en_core_web_sm
python -m spacy download ru_core_news_sm
