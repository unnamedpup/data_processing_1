from bs4 import BeautifulSoup
import subprocess
from docx import Document
import pymupdf
from pathlib import Path

def return_not_empty_text(text: str) -> str:
    if not text or not text.strip():
        raise ValueError("Пустой текст")
    return text

def parse_html(url: Path) -> str:
    with open(url, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    return return_not_empty_text(" ".join(p.get_text(" ", strip=True) for p in soup.find_all("p")))

def parse_pdf(file_path: Path) -> str:
    with pymupdf.open(file_path) as doc:
        return return_not_empty_text("\n".join(page.get_text().replace("\u200b", " ").strip() for page in doc))

def parse_docx(file_path: Path) -> str:
    doc = Document(str(file_path))
    return return_not_empty_text("\n".join(paragraph.text.strip() for paragraph in doc.paragraphs))

def parse_doc(file_path: Path) -> str:
    text = subprocess.run(
        ["antiword", "-m", "UTF-8.txt", str(file_path)],
        capture_output=True,
        text=True,
        check=True,
        errors="replace"
    )
    return return_not_empty_text(text.stdout.strip())

def parse_djvu(file_path: Path) -> str:
    text = subprocess.run(
        ["djvutxt", str(file_path)],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
        check=True
    )
    return return_not_empty_text(text.stdout.strip())