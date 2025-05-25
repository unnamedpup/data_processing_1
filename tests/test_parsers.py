import pytest
from utils.parsers import parse_pdf, parse_docx, parse_doc, parse_djvu, parse_html
from test_paths import TestFiles
import requests

PATHS = TestFiles()

def test_parse_pdf_success():
    assert parse_pdf(PATHS.VALID_PDF) == "Hello world!!!"

def test_parse_docx_success():
    assert parse_docx(PATHS.VALID_DOCX) == "Hello world!!!"

def test_parse_doc_success():
    assert parse_doc(PATHS.VALID_DOC) == "Hello world!!!"

def test_parse_djvu_success():
    assert parse_djvu(PATHS.VALID_DJVU) == "Hello world!!!"

def test_parse_url_success():
    assert parse_html(PATHS.VALID_URL) is not None

def test_parse_url_error():
    with pytest.raises(requests.exceptions.HTTPError):
        assert parse_html(PATHS.NON_VALID_URL)

def test_parse_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        parse_doc(PATHS.NON_EXISTENT_DOC)
