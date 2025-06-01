import spacy
from langdetect import detect
from spacy.tokens import Doc

SUPPORTED_LANGUAGES = {
    "en": "en_core_web_sm",
    "ru": "ru_core_news_sm",
}


def processing_text(text: str) -> Doc:
    """Возвращает результат анализа текста с помощью spaCy.

    Args:
        text: Текст для анализа.

    Returns:
        Объект Doc с результатами анализа текста.

    Raises:
        ValueError: Если язык не поддерживается.
        RuntimeError: Если модель не установлена.
    """
    cleaned_text = " ".join(text.split())
    language = detect(cleaned_text)
    nlp = load_spacy_model(language)
    return nlp(cleaned_text)


def load_spacy_model(language: str) -> spacy.language.Language:
    """Загружает модель spaCy для указанного языка.

    Args:
        language: Код языка (например, 'en' или 'ru').

    Returns:
        Загруженная модель spaCy.

    Raises:
        ValueError: Если язык не поддерживается.
        RuntimeError: Если модель не установлена.
    """
    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Язык '{language}' не поддерживается")

    model_name = SUPPORTED_LANGUAGES[language]

    try:
        return spacy.load(model_name)
    except OSError:
        raise RuntimeError(
            f"Модель для языка '{language}' не установлена!\n"
            f"Для загрузки выполните: python -m spacy download {model_name}"
        )


def analyze(text: str) -> tuple[list[dict[str, str | bool]], list[dict[str, str]] | None]:
    """Анализирует текст и возвращает информацию о токенах и именованных сущностях.

    Args:
        text: Текст для анализа.

    Returns:
        Кортеж из:
        1. Список словарей с информацией о токенах
        2. Список словарей с именованными сущностями или None

    Raises:
        ValueError: Если текст пустой или не может быть обработан.
        RuntimeError: Если возникли проблемы при анализе текста.
    """
    tokens = processing_text(text)

    result_of_analyze = [{
        "text": token.text,
        "lemma": token.lemma_,
        "pos": token.pos_,
        "tag": token.tag_,
        "dep": token.dep_,
        "is_stop": token.is_stop
    } for token in tokens]

    entities = [{
        "text": entity.text,
        "label": entity.label_,
    } for entity in tokens.ents]

    return result_of_analyze, entities