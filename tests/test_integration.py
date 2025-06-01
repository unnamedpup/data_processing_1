import pytest
from test_paths import TestFiles
from main import process_input

PATHS = TestFiles()

def test_parse_non_valid_format():
    with pytest.raises(ValueError):
        process_input(PATHS.INVALID_FORMAT)

def test_full_pipeline():
    text, result_df, _ = process_input(PATHS.VALID_EN_DOCX)
    assert text == "Hello world!!!" and not result_df.empty

def test_parse_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        process_input(PATHS.NON_EXISTENT_DOC)

def test_full_pipeline_with_entities():
    text, result_of_analyze, entities = process_input(PATHS.FULL_PIPELINE_WITH_ENTITIES)
    result_of_analyze_token = result_of_analyze.iloc[5]
    entity = entities.iloc[0]
    assert text == "Стив Джобс основатель очень крупной компании\nАлександр Сергеевич - великий русский поэт"
    assert result_of_analyze_token["text"] == "компании"
    assert result_of_analyze_token["lemma"] == "компания"
    assert result_of_analyze_token["pos"] == "NOUN"
    assert result_of_analyze_token["tag"] == "NOUN"
    assert result_of_analyze_token["dep"] == "nmod"
    assert result_of_analyze_token["is_stop"] == False
    assert entity["text"] == "Стив Джобс"
    assert entity["label"] == "PER"

