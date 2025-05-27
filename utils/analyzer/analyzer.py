import spacy
from langdetect import detect
from spacy.tokens import Doc

SUPPORTED_LANGUAGES = {
    "en": "en_core_web_sm",
    "ru": "ru_core_news_sm",
}

def processing_text(text: str) -> Doc | Exception:
    """
    Функция возращающая рузльтат анализа текста

    Args:
        text (str): текст файла

    Returns:
         Doc | Exception: рузльтат анализа текста или исключение
   """
    cleaned_text = " ".join(text.split())
    language = detect(cleaned_text)
    nlp = load_spacy_model(language)
    return nlp(cleaned_text)

def load_spacy_model(language: str) -> spacy.language.Language | Exception:
    """
    Функция возращающая соответствующую языку модель анализатора

    Args:
        language (str): язык текста

    Returns:
         spacy.language.Language | Exception: модель для анализа текста или исключение
   """
    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Данный язык ('{language}') не поддерживается")

    model_name = SUPPORTED_LANGUAGES[language]

    try:
        model = spacy.load(model_name)
    except OSError:
        raise RuntimeError(
            f"Модель для языка ('{language}') не установлена!\n"
            f"Для ее загрузки выполните команду: python -m spacy download {model_name}",
        )

    return model

def analyze(text: str) -> tuple[list[dict[str, str | bool]], list[dict[str, str]] | None] | Exception:
    """
    Функция возращающая соответствующую языку модель анализатора

    Args:
        text (str): текст файла

    Returns:
        tuple[list[dict[str, str | bool]], list[dict[str, str]] | None] | Exception:
        - Кортеж из:
          * Списка словарей (ключ: str, значение: str или bool) - результат анализа текста по токенам
          * Списка словарей (ключ: str, значение: str) или None - сущности по токенам или None
        - Или исключение в случае ошибки
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
