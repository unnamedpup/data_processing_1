from typing import Union
from utils.parsers.parsers import parse_html, parse_pdf, parse_docx, parse_doc, parse_djvu
from utils.analyzer import analyze
from pathlib import Path
from urllib.parse import urlparse
import pandas as pd
import argparse

PARSERS = {
    ".pdf": parse_pdf,
    ".docx": parse_docx,
    ".doc": parse_doc,
    ".djvu": parse_djvu,
    ".html": parse_html,
}

def process_input(input_path: Path) -> Union[
    tuple[str, pd.DataFrame, pd.DataFrame | None],
    Exception
    ]:
    if not input_path.exists():
        raise FileNotFoundError(f"Ошибка: файла {input_path} не существует")

    if not input_path.is_file():
        raise ValueError(f"Ошибка: {input_path} не является файлом")

    extension = input_path.suffix.lower()
    if extension not in PARSERS:
        raise ValueError(f"Ошибка: неподдерживаемый формат {extension}")

    parser = PARSERS[extension]
    text = parser(input_path)
    result_of_analyze, entities = analyze(text)
    return text, result_of_analyze, entities

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Файловый парсер\n"
                    "Поддерживаемые форматы: url, 'pdf', 'docx', 'doc', 'djvu'\n"
                    "Поддерживаемые языки: 'ru' и 'en'\n",
        epilog="Пример использования:\n"
               "  python main.py input.pdf\n",
        formatter_class=argparse.RawTextHelpFormatter  # чтобы \n работали в epilog
    )
    parser.add_argument("path", type=Path, help="Путь до файла (обязательный)")
    return parser.parse_args()

def main():
    args = parse_args()
    path_to_file = args.path
    try:
        text, result_of_analyze, entities = process_input(path_to_file)
        print(f"Текст:\n{text}")
        print(f"Анализ:\n{result_of_analyze}")
        if entities:
            print(f"Сущности:\n{entities}")
    except FileNotFoundError as e:
        print(f"Файл не найден: {str(e)}")
    except ValueError as e:
        print(f"Некорректные данные: {str(e)}")
    except RuntimeError as e:
        print(f"Ошибка анализа: {str(e)}")
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")

if __name__ == "__main__":
    main()