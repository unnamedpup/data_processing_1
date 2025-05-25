from utils.analyzer import Analyzer
import pytest

ANALYZER = Analyzer()

def test_analyzer_unsupported_language():
    with pytest.raises(RuntimeError):
        ANALYZER.analyze("このテキストは日本語です")

def test_analyzer_empty_text():
    with pytest.raises(RuntimeError):
        ANALYZER.analyze("")

def test_analyzer_grammar_errors():
    analyzer = Analyzer()
    result, _ = analyzer.analyze("Привет мир!!! Александр Пушкин великий русский поэт.")
    assert len(result) > 0


def base_form(token):
    return token["text"] == "основатель" and token["lemma"] == "основатель"

def part_of_speech(token):
    return token["text"] == "основатель" and token["pos"] == "NOUN"

def dependency_type(token):
    return token["text"] == "основатель" and token["dep"] == "ROOT"

@pytest.mark.parametrize(
    "cond",
    [
        base_form,
        part_of_speech,
        dependency_type,
    ]
)
def test_stats(cond):
    stats = ANALYZER.analyze("Стив Джобс основатель очень крупной компании")
    print(stats[0][2])
    assert cond(stats[0][2])

def test_entities():
    stats = ANALYZER.analyze("Стив Джобс основатель очень крупной компании")
    entity = stats[1][0]
    print(entity)
    assert entity["text"] == "Стив Джобс" and entity["label"] == "PER"

