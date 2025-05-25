from utils.analyzer import Analyzer
import pytest

ANALYZER = Analyzer()

def test_analyzer_unsupported_language():
    with pytest.raises(RuntimeError):
        ANALYZER.analyze("このテキストは日本語です")

def test_analyzer_empty_text():
    with pytest.raises(RuntimeError):
        ANALYZER.analyze("")

def test_analyzer_responce():
    analyzer = Analyzer()
    result, _ = analyzer.analyze("Привет мир!!! Александр Пушкин великий русский поэт.")
    assert len(result) > 0

def text(token):
    return token["text"] == "основатель"

def lemma(token):
    return token["lemma"] == "основатель"

def part_of_speech(token):
    return token["pos"] == "NOUN"

def tag(token):
    return token["tag"] == "NOUN"

def dependency(token):
    return token["dep"] == "ROOT"

def is_stop(token):
    return token["is_stop"] == False

@pytest.mark.parametrize(
    "cond",
    [
        text,
        lemma,
        part_of_speech,
        tag,
        dependency,
        is_stop
    ]
)
def test_stats(cond):
    stats = ANALYZER.analyze("Стив Джобс основатель очень крупной компании")
    assert cond(stats[0][2])

def test_entities():
    stats = ANALYZER.analyze("Стив Джобс основатель очень крупной компании")
    entity = stats[1][0]
    assert entity["text"] == "Стив Джобс" and entity["label"] == "PER"

def test_language_detection():
    assert ANALYZER._detect_language("wow it's work fast") == "en"



