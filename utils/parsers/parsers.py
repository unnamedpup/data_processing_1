import os
from functools import wraps
from bs4 import BeautifulSoup
import requests
import subprocess
from docx import Document
import pymupdf

def handle_parsing_errors(func):
    @wraps(func)
    def wrapper(file_path):
        try:
            if not os.path.exists(file_path) and func.__name__ != "parse_html":
                raise FileNotFoundError
            return func(file_path)
        except UnicodeDecodeError as e:
            raise ValueError(f"Проблемы с файлом: {e}")
    return wrapper

@handle_parsing_errors
def parse_html(url):
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    return ' '.join(p.get_text(" ", strip=True) for p in soup.find_all("p"))

@handle_parsing_errors
def parse_pdf(file_path):
    with pymupdf.open(file_path) as doc:
        return "\n".join(page.get_text().strip() for page in doc)

@handle_parsing_errors
def parse_docx(file_path):
    doc = Document(file_path)
    return "\n".join(paragraph.text.strip() for paragraph in doc.paragraphs)

@handle_parsing_errors
def parse_doc(file_path):
    text = subprocess.run(
        ["antiword", "-m", "utf-8.txt", str(file_path)],
        capture_output=True,
        text=True,
        check=True,
        errors="replace"
    )
    return text.stdout.strip()

@handle_parsing_errors
def parse_djvu(file_path):
    text = subprocess.run(
        ["djvutxt", str(file_path)],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
        check=True
    )
    return text.stdout.strip()