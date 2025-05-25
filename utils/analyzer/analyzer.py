import spacy
from langdetect import detect, LangDetectException

class Analyzer:
    SUPPORTED_LANGUAGES = {
        "en": "en_core_web_sm",
        "ru": "ru_core_news_sm",
        "de": "de_core_news_sm",
        "fr": "fr_core_news_sm",
        "es": "es_core_news_sm"
    }

    def __init__(self):
        self._loaded_models = {}

    @staticmethod
    def _clean_text(text):
        return " ".join(text.split())

    @staticmethod
    def _detect_language(text):
        try:
            return detect(text)
        except LangDetectException:
            raise ValueError("Язык текста не опредлен")
        except Exception as e:
            raise ValueError(f"При анализе языка текста возникла ошибка: {str(e)}")

    def _processing_text(self, text):
        cleaned_text = self._clean_text(text)
        language = self._detect_language(cleaned_text)
        nlp = self._load_spacy_model(language)
        return nlp(cleaned_text)


    def _load_spacy_model(self, language):
        if language not in self.SUPPORTED_LANGUAGES:
            raise ValueError(f"Данный язык ('{language}') не поддерживается")


        model_name = self.SUPPORTED_LANGUAGES[language]

        if language not in self._loaded_models:
            try:
                self._loaded_models[language] = spacy.load(model_name)
            except OSError:
                raise RuntimeError(
                    f"Модель для языка ('{language}') не установлена!\n"
                    f"Для ее загрузки выполните команду: python -m spacy download {model_name}",
                )
            except Exception as e:
                raise RuntimeError(f"При загрузке модели возникла ошибка: {str(e)}")

        return self._loaded_models[language]

    def analyze(self, text):
        try:
            if not text or not text.strip():
                raise ValueError("Анализ пустого текста не поддерживается")

            tokens = self._processing_text(text)

            analyzed = [{
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

            return analyzed, entities
        except ValueError as e:
            raise RuntimeError(f"При анализе текста возникла ошибка: {str(e)}")
