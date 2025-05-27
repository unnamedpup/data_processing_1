import pytest
from utils.parsers import parse_pdf, parse_docx, parse_doc, parse_djvu, parse_html
from test_paths import TestFiles

PATHS = TestFiles()

# PDF
def test_parse_pdf_en_success():
    assert parse_pdf(PATHS.VALID_EN_PDF) == "Hello world!!!"

def test_parse_pdf_ru_success():
    assert parse_pdf(PATHS.VALID_RU_PDF) == "Привет мир!!!"

def test_parse_pdf_empty():
    with pytest.raises(ValueError):
        assert parse_pdf(PATHS.EMPTY_PDF)

# DOCX
def test_parse_docx_en_success():
    assert parse_docx(PATHS.VALID_EN_DOCX) == "Hello world!!!"

def test_parse_docx_ru_success():
    assert parse_docx(PATHS.VALID_RU_DOCX) == "Привет мир!!!"

def test_parse_docx_empty():
    with pytest.raises(ValueError):
        assert parse_docx(PATHS.EMPTY_DOCX)

# DOC
def test_parse_doc_en_success():
    assert parse_doc(PATHS.VALID_EN_DOC) == "Hello world!!!"

def test_parse_doc_ru_success():
    assert parse_doc(PATHS.VALID_RU_DOC) == "Привет мир!!!"

def test_parse_doc_empty():
    with pytest.raises(ValueError):
        assert parse_doc(PATHS.EMPTY_DOC)

# DJVU
def test_parse_djvu_en_success():
    assert parse_djvu(PATHS.VALID_EN_DJVU) == "Hello world!!!"

def test_parse_djvu_ru_success():
    assert parse_djvu(PATHS.VALID_RU_DJVU) == "Привет мир!!!"

def test_parse_djvu_empty():
    with pytest.raises(ValueError):
        assert parse_djvu(PATHS.EMPTY_DJVU)

# HTML
def test_parse_html_en_success():
    assert parse_html(PATHS.VALID_EN_HTML) == "Hello world!!!"

def test_parse_html_ru_success():
    assert parse_html(PATHS.VALID_RU_HTML) == "Привет мир!!!"

def test_parse_html_empty():
    with pytest.raises(ValueError):
        assert parse_html(PATHS.EMPTY_HTML)
