from pathlib import Path


class TestFiles:
    # Корневая папка с тестовыми файлами
    TEST_DATA_DIR = Path(__file__).parent / "data"

    # PDF
    VALID_EN_PDF = TEST_DATA_DIR / "valid_en.pdf"
    VALID_RU_PDF = TEST_DATA_DIR / "valid_ru.pdf"
    EMPTY_PDF = TEST_DATA_DIR / "empty.pdf"

    # DOCX
    VALID_EN_DOCX = TEST_DATA_DIR / "valid_en.docx"
    VALID_RU_DOCX = TEST_DATA_DIR / "valid_ru.docx"
    EMPTY_DOCX = TEST_DATA_DIR / "empty.docx"

    # DOC
    VALID_EN_DOC = TEST_DATA_DIR / "valid_en.doc"
    VALID_RU_DOC = TEST_DATA_DIR / "valid_ru.doc"
    EMPTY_DOC = TEST_DATA_DIR / "empty.doc"

    # DJVU
    VALID_EN_DJVU = TEST_DATA_DIR / "valid_en.djvu"
    VALID_RU_DJVU = TEST_DATA_DIR / "valid_ru.djvu"
    EMPTY_DJVU = TEST_DATA_DIR / "empty.djvu"

    # HTML
    VALID_EN_HTML = TEST_DATA_DIR / "valid_en.html"
    VALID_RU_HTML = TEST_DATA_DIR / "valid_ru.html"
    EMPTY_HTML = TEST_DATA_DIR / "empty.html"

    # INVALID_FORMAT
    INVALID_FORMAT = TEST_DATA_DIR / "invalid_format.txt"

    # NON_EXISTENT_DOC
    NON_EXISTENT_DOC = TEST_DATA_DIR / "nonexistent.doc"

    # FULL_PIPELINE_WITH_ENTITIES
    FULL_PIPELINE_WITH_ENTITIES = TEST_DATA_DIR / "full_pipeline_with_entities.docx"


