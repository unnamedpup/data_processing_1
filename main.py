from utils.parsers.parsers import parse_html, parse_pdf, parse_docx, parse_doc, parse_djvu
from utils.analyzer import Analyzer
from pathlib import Path
from urllib.parse import urlparse
import pandas as pd

PARSERS = {
    ".pdf": parse_pdf,
    ".docx": parse_docx,
    ".doc": parse_doc,
    ".djvu": parse_djvu
}

ANALYZER = Analyzer()

def is_url(input_str):
    url = urlparse(str(input_str))
    return all([url.scheme, url.netloc])

def process_input(input_path):
    if is_url(input_path):
        parser = parse_html
    else:
        input_path = Path(input_path)

        if not input_path.exists():
            raise FileNotFoundError(f"Ошибка: файла {input_path} не существует")

        if not input_path.is_file():
            raise ValueError(f"Ошибка: {input_path} не является файлом")

        extension = input_path.suffix.lower()
        if extension not in PARSERS:
            raise ValueError(f"Ошибка: неподдерживаемый формат {extension}")

        parser = PARSERS[extension]

    text = parser(input_path)
    return text, *ANALYZER.analyze(text)


def main():
    print("Файловый парсер.\n"
          "Поддерживаемые форматы: url, 'pdf, 'docx', 'doc', 'djvu'.\n"
          "Введите путь к файлу/ссылку (для выхода введите пустую строку):")

    while True:
        try:
            user_input = input("> ").strip()

            if not user_input:
                print("Завершение работы...")
                break

            text, stats, entities = process_input(user_input)

            print(f"Текст:\n{text}")
            print(f"Анализ:\n{pd.DataFrame(stats)}")
            if entities:
                print(f"Сущности:\n{pd.DataFrame(entities)}")

        except FileNotFoundError as e:
            print(f"Файл не найден: {str(e)}")
            continue

        except ValueError as e:
            print(f"Некорректные данные: {str(e)}")
            continue

        except RuntimeError as e:
            print(f"Ошибка анализа: {str(e)}")
            continue

        except Exception as e:
            print(f"Неожиданная ошибка: {str(e)}")
            import traceback
            traceback.print_exc()
            if input("Продолжить? (y/n) ").lower() != 'y':
                break


if __name__ == "__main__":
    main()