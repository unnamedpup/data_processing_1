from pathlib import Path


class TestFiles:
    # Корневая папка с тестовыми файлами
    TEST_DATA_DIR = Path(__file__).parent / "data"

    # PDF
    VALID_PDF = TEST_DATA_DIR / "valid.pdf"

    # DOCX
    VALID_DOCX = TEST_DATA_DIR / "valid.docx"

    # DOC
    VALID_DOC = TEST_DATA_DIR / "valid.doc"

    # DJVU
    VALID_DJVU = TEST_DATA_DIR / "valid.djvu"

    # INVALID_DORMAT
    INVALID_FORMAT = TEST_DATA_DIR / "invalid_format.txt"

    # NON_EXISTENT_DOC
    NON_EXISTENT_DOC = TEST_DATA_DIR / "noneexistent.doc"

    # URL
    VALID_URL = "https://vk.com/therealtriples"
    NON_VALID_URL = "https://vk.com/pmpu"

