from bs4 import BeautifulSoup
import subprocess
from docx import Document
import pymupdf
from pathlib import Path


def return_not_empty_text(text: str) -> str:
    """Проверяет, содержит ли текст информацию или является пустым.

    Args:
        text: Текст для проверки.

    Returns:
        Исходный текст, если он не пустой.

    Raises:
        ValueError: Если текст пустой или состоит только из пробельных символов.
    """
    if not text or not text.strip():
        raise ValueError("Пустой текст")
    return text

def parse_html(file_path: Path) -> str:
    """Извлекает текст из HTML-файла.

    Парсит HTML-файл, извлекая текст из всех тегов <p>.

    Args:
        file_path: Путь к HTML-файлу.

    Returns:
        Текст, извлеченный из файла.

    Raises:
        ValueError: Если текст пустой или состоит только из пробельных символов.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    return return_not_empty_text(" ".join(p.get_text(" ", strip=True) for p in soup.find_all("p")))

def parse_pdf(file_path: Path) -> str:
    """Извлекает текст из PDF-файла.

    Args:
        file_path: Путь к PDF-файлу.

    Returns:
        Текст, извлеченный из файла.

    Raises:
        ValueError: Если текст пустой или состоит только из пробельных символов.
    """
    with pymupdf.open(file_path) as doc:
        return return_not_empty_text("\n".join(page.get_text().replace("\u200b", "  ").strip() for page in doc))

def parse_docx(file_path: Path) -> str:
    """Извлекает текст из DOCX-файла.

    Args:
        file_path: Путь к DOCX-файлу.

    Returns:
        Текст, извлеченный из файла.

    Raises:
        ValueError: Если текст пустой или состоит только из пробельных символов.
    """
    doc = Document(str(file_path))
    return return_not_empty_text("\n".join(paragraph.text.strip() for paragraph in doc.paragraphs))

def parse_doc(file_path: Path) -> str:
    """Извлекает текст из DOC-файла с помощью antiword.

    Args:
        file_path: Путь к DOC-файлу.

    Returns:
        Текст, извлеченный из файла.

    Raises:
        ValueError: Если текст пустой или состоит только из пробельных символов.
    """
    text = subprocess.run(
        ["antiword", "-m", "UTF-8.txt", str(file_path)],
        capture_output=True,
        text=True,
        check=True,
        errors="replace"
    )
    return return_not_empty_text(text.stdout.strip())


def parse_djvu(file_path: Path) -> str:
    """Извлекает текст из DJVU-файла с помощью djvutxt.

    Args:
        file_path: Путь к DJVU-файлу.

    Returns:
        Текст, извлеченный из файла.

    Raises:
        ValueError: Если текст пустой или состоит только из пробельных символов..
    """
    text = subprocess.run(
        ["djvutxt", str(file_path)],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
        check=True
    )
    return return_not_empty_text(text.stdout.strip())