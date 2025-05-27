from utils.analyzer import analyze
import pytest

def test_analyzer_unsupported_language():
    with pytest.raises(ValueError):
        analyze("このテキストは日本語です")

def test_analyze():
    res = analyze("Стив Джобс основатель очень крупной компании")[0][2]
    assert res["text"] == "основатель"
    assert res["lemma"] == "основатель"
    assert res["pos"] == "NOUN"
    assert res["tag"] == "NOUN"
    assert res["dep"] == "ROOT"
    assert res["is_stop"] == False

def test_entities():
    stats = analyze("Стив Джобс основатель очень крупной компании")
    entity = stats[1][0]
    assert entity["text"] == "Стив Джобс" and entity["label"] == "PER"

# def test_language_detection():
#     assert detect_language("wow it's work fast") == "en"



