import pytest
from test_paths import TestFiles
from main import process_input

PATHS = TestFiles()

def test_parse_nonvalid_format():
    with pytest.raises(ValueError):
        process_input(PATHS.INVALID_FORMAT)

def test_full_pipeline():
    result = process_input(PATHS.VALID_DOCX)
    assert result[0] == "Hello world!!!" and result[1]