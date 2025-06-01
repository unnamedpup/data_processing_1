from utils.parsers.parsers import parse_html, parse_pdf, parse_docx, parse_doc, parse_djvu
from utils.analyzer import analyze
from pathlib import Path
import pandas as pd
import argparse

PARSERS = {
    ".pdf": parse_pdf,
    ".docx": parse_docx,
    ".doc": parse_doc,
    ".djvu": parse_djvu,
    ".html": parse_html,
}


def process_input(input_path: Path) -> tuple[str, pd.DataFrame, pd.DataFrame | None]:
    """Обрабатывает входной файл: парсит текст и выполняет лингвистический анализ.

    Args:
        input_path: Путь к файлу для обработки.

    Returns:
        Кортеж из:
        1. Текст файла
        2. DataFrame с анализом токенов
        3. DataFrame с сущностями или None

    Raises:
        FileNotFoundError: Если файл не существует.
        ValueError: Если путь не является файлом или формат не поддерживается.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Файл {input_path} не существует")

    if not input_path.is_file():
        raise ValueError(f"{input_path} не является файлом")

    extension = input_path.suffix.lower()
    if extension not in PARSERS:
        raise ValueError(f"Неподдерживаемый формат {extension}")

    text = PARSERS[extension](input_path)
    result_of_analyze, entities = analyze(text)
    result_df = pd.DataFrame(result_of_analyze)
    entities_df = pd.DataFrame(entities) if entities else None
    return text, result_df, entities_df


def parse_args() -> argparse.Namespace:
    """Парсит аргументы командной строки.

    Returns:
        Объект с разобранными аргументами.
    """
    parser = argparse.ArgumentParser(
        description="Файловый парсер\n"
                    "Поддерживаемые форматы: url, 'pdf', 'docx', 'doc', 'djvu'\n"
                    "Поддерживаемые языки: 'ru' и 'en'\n",
        epilog="Пример использования:\n"
               "  python main.py input.pdf\n",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("path", type=Path, help="Путь до файла (обязательный)")
    return parser.parse_args()


def main():
    """Основная функция для запуска парсера из командной строки."""
    args = parse_args()
    path_to_file = args.path

    try:
        text, result_of_analyze, entities = process_input(path_to_file)
        print(f"Текст:\n{text}")
        print(f"Анализ:\n{result_of_analyze}")
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