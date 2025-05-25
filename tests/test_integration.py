import pytest
from test_paths import TestFiles
from main import process_input

PATHS = TestFiles()

def test_parse_nonevalid_format():
    with pytest.raises(ValueError):
        process_input(PATHS.INVALID_FORMAT)